from openai import OpenAI
from os import getenv
from dotenv import load_dotenv

load_dotenv()
OPENROUTER_API_KEY = getenv("API_KEY")

# print(OPENROUTER_API_KEY)

# gets API Key from environment variable OPENAI_API_KEY
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

with open("resume.txt", "r") as f:
    resume = f.read()


def get_response(query):
    prompt = f"""

    Imagine you are Ayush Koul. Answer the following question(s) as if you are Ayush Koul.
    Give very short and concise answers (couple sentences only) with formal language.
    
    {query}

    use the following resume details to answer questions about yourself:
    {resume}
    """

    completion = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct:free",
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    print(completion.choices[0].message.content)
    return completion.choices[0].message.content
