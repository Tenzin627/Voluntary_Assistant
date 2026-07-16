import os

from dotenv import load_dotenv
from groq import Groq


load_dotenv(".env")


api_key = os.getenv(
    "GROQ_API_KEY"
)


if not api_key:
    raise ValueError(
        "GROQ_API_KEY is missing from .env"
    )


client = Groq(
    api_key=api_key
)



MODEL = "llama-3.1-8b-instant"



def ask_groq(context, question):
    """
    Send handbook context and question
    to Groq AI.

    Args:
        context:
            Relevant handbook sections

        question:
            User question

    Returns:
        AI response text
    """


    prompt = f"""
You are a Volunteer Knowledge Assistant.

Your job is to answer questions using ONLY
the volunteer handbook information provided.

Rules:
- Do not invent information.
- If the answer is not in the handbook,
  say you could not find it.
- Keep answers clear and concise.
- Use bullet points when helpful.


HANDBOOK INFORMATION:

{context}


USER QUESTION:

{question}


ANSWER:
"""


    try:

        response = client.chat.completions.create(

            model=MODEL,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.2,

            max_tokens=500

        )


        return (
            response
            .choices[0]
            .message
            .content
            .strip()
        )


    except Exception as e:

        return (
            f"Unable to contact AI service: {e}"
        )