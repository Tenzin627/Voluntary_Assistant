from flask import Flask, render_template, request
import os

from pdf_reader import extract_text
from search import search_text
from groq_ai import ask_groq


app = Flask(
    __name__,
    template_folder="template"
)


UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# Stores the uploaded handbook text
document_text = ""


def ensure_upload_folder():
    """Create uploads folder if it doesn't exist."""
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    """Home page."""
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    """Upload and process a PDF handbook."""

    global document_text

    if "file" not in request.files:
        return "No file uploaded."

    file = request.files["file"]

    if file.filename == "":
        return "Please select a PDF."

    if not file.filename.lower().endswith(".pdf"):
        return "Only PDF files are supported."

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    try:
        document_text = extract_text(filepath)

    except Exception as e:
        return f"Unable to read PDF: {e}"

    if not document_text.strip():
        return "The PDF contains no readable text."

    print("=" * 50)
    print("Volunteer handbook uploaded")
    print(file.filename)
    print(f"{len(document_text)} characters extracted")
    print("=" * 50)

    return render_template(
        "index.html",
        upload_success=True
    )


@app.route("/ask", methods=["POST"])
def ask():
    """Answer questions using the uploaded handbook."""

    global document_text

    if not document_text:
        return "Please upload a handbook before asking questions."

    question = request.form.get(
        "question",
        ""
    ).strip()

    if not question:
        return "Please enter a question."

    context = search_text(
        document_text,
        question
    )

    if not context:
        return (
            "I couldn't find relevant information "
            "in the handbook."
        )

    try:
        answer = ask_groq(
            context,
            question
        )

        return answer

    except Exception as e:
        return f"AI Error: {e}"


if __name__ == "__main__":

    ensure_upload_folder()

    app.run(
        debug=True
    )