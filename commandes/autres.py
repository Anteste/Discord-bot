import time
import discord
from discord.ext import commands
import random

class Autres(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def gr(self,ctx,arg):
    print(arg)






def setup(client):
  client.add_cog(Autres(client))