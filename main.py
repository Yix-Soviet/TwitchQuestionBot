from twitchio.ext import commands

# Read env file library
from os import getenv
from dotenv import load_dotenv

# Import Commands
from commands import question

# Load env file
load_dotenv()


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            token=getenv("TWITCH_ACCESS_TOKEN"),
            initial_channels=[getenv("CHANNEL")],
            prefix=getenv("PREFIX"),
        )

    async def event_ready(self):
        print(f"Logged into Twitch | {self.nick}")


twitchBot = Bot()

# Add Commands
twitchBot.add_command(question.CommandQuestion())

if __name__ == "__main__":
    twitchBot.run()
