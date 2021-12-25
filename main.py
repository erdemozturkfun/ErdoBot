from discord.ext import commands

class ErdoBot(commands.Bot):
  async def __init__(self, botPrefix):
    self.command_prefix = botPrefix
    await self.login()
    