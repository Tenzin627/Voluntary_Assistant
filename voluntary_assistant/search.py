import re


def clean_text(text):
    """
    Normalize text for searching.
    """

    text = text.lower()

    text = re.sub(
        r"[^\w\s]",
        "",
        text
    )

    return text


def split_into_sections(text):
    """
    Split handbook into readable sections.
    """

    sections = []

    for section in text.split("\n\n"):

        section = section.strip()

        if len(section) > 30:
            sections.append(section)

    return sections


def score_section(section, question):
    """
    Score a section based on keyword matches.
    """

    section_words = clean_text(section).split()

    question_words = clean_text(question).split()

    score = 0

    for word in question_words:

        score += section_words.count(word)

    return score


def search_text(document_text, question, top_k=3):
    """
    Return the most relevant handbook sections.
    """

    if not document_text.strip():
        return ""

    sections = split_into_sections(document_text)

    scored_sections = []

    for section in sections:

        score = score_section(
            section,
            question
        )

        scored_sections.append(
            (
                score,
                section
            )
        )

    scored_sections.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    best_sections = []

    for score, section in scored_sections[:top_k]:

        if score > 0:

            best_sections.append(section)

    return "\n\n".join(best_sections)