import ollama

resume = input("Apna resume yaha paste karo:\n")

prompt = f"""
Analyze this resume and give:

1. Strengths
2. Weaknesses
3. Missing Skills
4. Suggestions
5. Score out of 100

Resume:
{resume}
"""

response = ollama.chat(
    model='llama3',
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print("\nAI Analysis:\n")
print(response['message']['content'])
response = ollama.chat(
    model='llama3',
    messages=[{"role": "user", "content": prompt}],
    stream=True
)

for chunk in response:
    print(chunk['message']['content'], end="", flush=True)