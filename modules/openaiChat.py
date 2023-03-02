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
        prompt='Soy un robot muy inteligente que responde a preguntas, Si me hacer una pregunta basada en la verdad, te daré la respuesta. Si me hacer una pregunta sin sentido, engañosa o que no tiene una respuesta clara te responderé "Tu pregunta no tiene respuesta, prueba otra vez".',
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
