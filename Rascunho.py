from groq import Groq

client = Groq()
completion = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {
            "role": "system",
            "content": "Você vai se chamar Neymar, você só pode falar de futebol, \ne não pode falar de nada mais.\n"
        },
        {
            "role": "user",
            "content": "Quem é neymar\n"
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=False,
    stop=None,
)

print(completion.choices[0].message)
