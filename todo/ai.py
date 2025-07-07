import openai
openai.api_base = "http://localhost:1234/v1"
openai.api_key = "lm-studio"

def get_task_ai_suggestions(title, context):
    prompt = f"""
    Task: {title}
    Context: {context}
    Return a JSON with: description, priority (1–5), deadline (YYYY-MM-DD), and category.
    """
    res = openai.ChatCompletion.create(
        model="Qwen",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return res['choices'][0]['message']['content']
