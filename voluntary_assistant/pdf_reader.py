import PyPDF2


def extract_text(pdf_path):
    """
    Extract text from a PDF file.

    Args:
        pdf_path: Location of the PDF file

    Returns:
        Extracted text as a string
    """

    text = ""


    try:

        with open(
            pdf_path,
            "rb"
        ) as file:


            reader = PyPDF2.PdfReader(
                file
            )


            for page in reader.pages:

                page_text = page.extract_text()


                if page_text:

                    text += page_text + "\n\n"



    except Exception as e:

        raise Exception(
            f"PDF extraction failed: {e}"
        )



    return text.strip()