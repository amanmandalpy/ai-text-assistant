def build_prompt(user_text, action):

    user_text = user_text.strip()

    if not user_text:
        raise ValueError("Text cannot be empty.")
    if action == "summarize":

        instructions = (
            "Summarize the following text " "in simple english. keep it short."
        )
    elif action == "explain":
        instructions = (
            "explain the following text " "in simple english with an example."
        )
    elif action == "translate":
        instructions = "translate the following text " "into simple hindi."
    else:
        raise ValueError("Invail action")

    prompt = f"""{instructions} 
                User Text: {user_text}"""
    return prompt.strip()
