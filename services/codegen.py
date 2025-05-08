import ollama

def generate_code(prompt: str) -> str:
    code_prompt = f"""
    Create code based on these musical instructions:
    {prompt}
    Respond only with the code implementation, no explanations.
    """
    response = ollama.chat(model="llama3", messages=[{"role": "user", "content": code_prompt}])
    return response['message']['content']
