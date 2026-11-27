def generate_ai_response(user_text, action):
    """
    Temporary ai service.
    This simulates the ai response flow without calling an LLM.
    """

    user_text = user_text.strip()

    if not user_text:
        raise ValueError("Text cannot be empty")

    if action == "summarize":
        words = user_text.split()

        summary = " ".join(words[:15])

        return f"MOCK SUMMARY: {summary}"

    elif action == "explain":
        return "MOCK EXPLANATION: " f"You asked to explain this text: {user_text}"
    else:
        raise ValueError("Unsupported action.")
