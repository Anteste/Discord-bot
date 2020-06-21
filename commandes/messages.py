
import discord
from discord.ext import commands
import random
import time
class Messages(commands.Cog):
  def __init__(self, bot):
    self.bot = bot






def setup(client):
  client.add_cog(Messages(client))