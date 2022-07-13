# disnake-boilerplate
![disnake-boilerplate-banner](https://github.com/tarranprior/disnake-boilerplate/blob/main/assets/banner.png?raw=true)

Yet another Discord bot template written in Python using the Disnake API wrapper. For kick-starting future projects and commissions. 🍽️

## Prerequisites
- Python 3.8 +
- [Poetry](https://python-poetry.org/docs) (or the [pip](https://pypi.org/project/pip/) package management tool.)

## Features

## Disclaimer
This template serves as a basic, barebones template for Discord bot development. You should have some knowledge of Python, asynchronous programming and the Disnake syntax.

For more information on Disnake, check out the [docs](https://docs.disnake.dev/en/latest/index.html).

### Slash Commands
Slash commands can take some time to register on guilds (usually an hour or two.) If you'd like to test a slash command beforehand, use `guild_ids` in the command decorator to register them instantly.
   ```python
@commands.slash_command(
    name="command",
    description="Command description",
    guild_ids=[GUILD_ID1, GUILD_ID2] # The ID(s) of the guild(s) you wish to test.
)
   ```

Alternatively, you can define the `guild_id` globally in `main.py`.
   ```python
   bot = commands.Bot(
      test_guilds=[GUILD_ID1, GUILD_ID2],
   )
   ```

## Configuration
1. Update the values in `SAMPLE.env` and rename to `.env`.

   ```s
   DISCORD_TOKEN = YOUR_BOT_TOKEN
   DISCORD_ADMIN = YOUR_USER_ID
   ```
2. *Optional*: Update the values in `config.json`.

   ```json
   {
      "activity": "Bot",
      "prefix": "!"
   }
   ```

## Support
If you have any questions about this template, please submit an issue [here](https://github.com/tarranprior/disnake-boilerplate/issues).

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.

## References & Resources
- Disnake Docs https://docs.disnake.dev/en/latest/index.html
- Discord Developer Applications https://discord.com/developers/applications