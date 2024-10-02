import google.generativeai as genai
from flask import current_app

def generate_explanation(query):
    genai.configure(api_key=current_app.config['GOOGLE_API_KEY'])

    prompt = f"""
    Explain the concept of '{query}' using a parable or a story and provide a simple, intuitive explanation and a clear illustration.
    """

    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    
    if response.text is None:
        return f"Error: Unable to generate explanation"

    explanation = response.text
    return explanation