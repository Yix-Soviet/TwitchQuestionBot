from twitchio.ext import commands

from modules.openai_question import resolveQuestion


async def questionFunction(ctx: commands.Context):
    message = ctx.message.content
    question = message.replace("?question", "")
    answer = resolveQuestion(question=question)

    await ctx.reply(f"Respuesta: {answer}")


class CommandQuestion(commands.Command):
    def __init__(self):
        super().__init__(name="question", func=questionFunction)
