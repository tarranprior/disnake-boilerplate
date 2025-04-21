#! /usr/bin/env python3

import platform
import os
import disnake

from disnake.ext import commands, tasks
from disnake import ApplicationCommandInteraction
from loguru import logger

from utils import *
from exceptions import *


class Bot(commands.InteractionBot):
    """
    A class which represents a Discord bot instance.
    """

    def __init__(self, config = None, *args, **kwargs) -> None:
        """
        Initialises a new instance of the Bot class.

        :param self: -
            Represents this object.
        :param config: (Optional[Dictionary]) -
            A dictionary containing configuration details.

        :return: (None)
        """

        super().__init__(*args, **kwargs)
        self.config = config or configuration()
        self.bot = Bot


    def load_extensions(self, exts: list) -> None:
        """
        Loads all extensions (cogs) for the bot.

        :param self: -
            Represents this object.
        :param exts: (List) -
            A list of file paths for the extensions.

        :return: (None)
        """

        count = 0
        for ext in exts:
            try:
                self.load_extension(ext)
                logger.success(ext)
                count += 1
            except Exception as exc:
                exception = f'{type(exc).__name__}: {exc}'
                logger.error(
                    f"Unable to load extension: {ext}\n{exception}."
                )

        logger.info(f"{count} extension(s) have loaded successfully.\n")


    async def on_connect(self) -> None:
        """
        A coroutine that is called when the bot has connected to
        the Discord gateway.

        :param self: -
            Represents this object.

        :return: (None)
        """

        logger.success("Bot is connected to the gateway.")
        logger.info(f"Logged in as {self.user.name} ({self.user.id})")
        logger.info(f"API Version: {disnake.__version__}")
        logger.info(
            f"Platform: {platform.system()} "
            f"{platform.release()} {os.name}\n"
        )


    async def on_ready(self) -> None:
        """
        A coroutine that executes when the bot is fully initialised
        and ready to respond to events.

        :param self: -
            Represents this object.

        :return: (None)
        """

        await self.wait_until_ready()

        logger.success('Bot is ready.')
        logger.info('For more information on usage, see the README.')


    async def on_slash_command_error(
        self,
        inter: ApplicationCommandInteraction,
        error: Exception
    ) -> None:
        """
        A coroutine that is called when a slash command encounters
        an error.

        :param self: -
            Represents this object.
        :param inter: (ApplicationCommandInteraction) -
            The interaction that resulted in the error.
        :param error: (Exception) -
            The error that was raised.

        :return: (None)
        """

        if isinstance(error, commands.errors.CommandNotFound):
            return

        elif isinstance(error, commands.errors.NotOwner):
            embed = EmbedFactory().create(
                title="Missing Permissions",
                description=f"{str(error).capitalize()}",
                colour=disnake.Colour.red()
            )
            return await inter.response.send_message(embed=embed)

        logger.error(
            f"Ignoring exception in slash command {inter.application_command.name}: {error}")


    @tasks.loop(minutes=10.0)
    async def status() -> None:
        await Bot.change_presence(
            activity=disnake.Game(
                name=Bot.config["configuration"]["activity"]
            )
        )
