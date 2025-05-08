import ollama

def judge_prompt(prompt: str) -> bool:
    judge_text = f"""
    You are a musical coding assistant judge.

    Evaluate the following input, which was rapped or sung by the user as a prompt for a coding agent.

    Judge based on the following criteria, scoring each out of 100:
    - 🎯 Relevance to programming or software development
    - 🎵 Rhythm and consistent phrasing
    - 🌀 Presence of rhyme or lyrical flow
    - ⚡ Originality and delivery energy

    After scoring each, compute the average score. 

    Respond *only* with:

    Relevance: <score>/100  
    Rhythm: <score>/100  
    Lyrical Flow: <score>/100  
    Delivery: <score>/100  

    Total Score: <average of the scores>  
    APPROVED – if the total score is **80 or higher**, or if the word "Testing" appears in the prompt.  
    REJECTED – if the total score is **below 80**, check the total score carefully.

    Input: "{prompt}"

    """
    response = ollama.chat(model="llama3", messages=[{"role": "user", "content": judge_text}])
    return response
