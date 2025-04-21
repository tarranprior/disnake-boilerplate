#! /usr/bin/env python3

from os import environ as env
from dotenv import load_dotenv

import disnake
from templates.bot import Bot
from src.utils.helpers import load_configuration


load_dotenv()

if __name__ == "__main__":

    bot = Bot(
        activity=disnake.Game(
            name=load_configuration()["configuration"]["activity"]
        ),
        help_command=None,
        intents=disnake.Intents.all(),
        owner_id=int(env["BOT_OWNER"])
    )

bot.load_extensions(exts=[
    "cogs.developer.purge"
])

bot.run(env["BOT_TOKEN"])
