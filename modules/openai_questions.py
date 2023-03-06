# OpenAI Library
import openai

# .env file library
from dotenv import load_dotenv
from os import getenv

# Load .env file
load_dotenv()

# OpenAI API Key
openai.api_key = getenv("OPENAI_API_KEY")


def resolveQuestion(question):
    getAnswer = "\nA:"
    makeQuestion = "\n\nQ: "

    # Initial message
    openai.Completion.create(
        model="text-davinci-003",
        prompt='I am a very intelligent robot that answers questions. If you ask me a question based on truth, I will give you the answer. If you ask me a question that is nonsensical, misleading, or doesn\'t have a clear answer, I will respond with "Your question has no answer, try again." If the answer is longer than 488 characters, I will summarize it to stay within 485 characters.',
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"],
    )
    # Send Question
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{makeQuestion}{question}{getAnswer}",
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"],
    )

    return response["choices"][0]["text"][1:]  # For only get the answer
