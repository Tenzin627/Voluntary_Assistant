# 📚 Volunteer Knowledge Assistant

An AI-powered assistant that allows volunteers to ask questions about handbook documents using natural language.

The application uses a simple RAG (Retrieval-Augmented Generation) workflow:
- Upload a PDF handbook
- Extract and search relevant information
- Generate answers using AI

---

## Features

- Upload PDF documents
- Extract text from handbooks
- Search relevant document sections
- Ask questions in natural language
- Generate AI-based answers from the uploaded document

---

## Tech Stack

**Backend**
- Python
- Flask

**AI**
- Groq API (Llama)

**Document Processing**
- PyPDF2

**Frontend**
- HTML / CSS / JavaScript

---

## Project Structure

```
Volunteer-Knowledge-Assistant/

├── app.py
├── pdf_reader.py
├── search.py
├── groq_ai.py
├── requirements.txt
│
├── template/
│   └── index.html
│
└── uploads/
```

---

## Setup

### 1. Clone the project

```bash
git clone <repository-url>
cd Volunteer-Knowledge-Assistant
```

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add API Key

Create a `.env` file:

```powershell
New-Item .env -ItemType File

```
GROQ_API_KEY=your_api_key_here
```

---

### 5. Run

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

## Example Questions

- What training is required?
- What are volunteer responsibilities?
- What should I do during an emergency?
- What is the privacy policy?

---

## How It Works

```
PDF Upload
     |
     v
Text Extraction
     |
     v
Relevant Section Search
     |
     v
AI Answer Generation
     |
     v
User Response
```

---

## Future Improvements

- Multiple document support
- Better semantic search
- Document citations
- Cloud deployment

---

## Author

Tenzin Melongkharpa
