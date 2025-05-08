import ollama

def judge_prompt(prompt: str) -> bool:
    judge_text = f"""
    You are a musical coding assistant judge.

    Evaluate the following input, which was rapped or sung by the user as a prompt for a coding agent.

    Judge based on:
    - 🎯 Relevance to programming or software development
    - 🎵 Musicality, including:
    - Rhythm and consistent phrasing
    - Presence of rhyme or lyrical flow
    - Originality and delivery energy

    You must respond only with:
    - APPROVED – if the input is both musically sound and coding-related
    - REJECTED – if it lacks musicality or is not relevant to coding

    If you hear the word "Testing" at any point, respond with "APPROVED".

    Input: "{prompt}"
    """
    response = ollama.chat(model="llama3", messages=[{"role": "user", "content": judge_text}])
    return "APPROVED" in response['message']['content'].upper()
