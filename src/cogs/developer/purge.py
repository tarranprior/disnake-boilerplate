#! /usr/bin/env python3

import asyncio

from disnake.ext import commands
from disnake import ApplicationCommandInteraction, Option, OptionType

from templates.bot import Bot
from utils import *


class Purge(commands.Cog, name="purge"):
    """
    A class which represents the "Purge" class.
    """

    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @commands.slash_command(name="purge", description="Permanently deletes a specified number of messages.", options=[
            Option(
                name="number",
                description="Specify a number of messages to purge.",
                type=OptionType.integer,
                required=True
            )
        ]
    )
    @commands.is_owner()
    async def purge_slash(self, inter: ApplicationCommandInteraction, number: int):
        messages = await inter.channel.purge(limit=int(number))
        await inter.send(f"{len(messages)} messages have been purged.")
        await asyncio.sleep(1)
        await inter.delete_original_message()

def setup(bot) -> None:
    bot.add_cog(Purge(bot))
