import time
import discord
from discord.ext import commands
import random

class Infos(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command()
  async def code(self,ctx):
    #envoi de messages pour expliquer comment envoyer un code sur discord
	  await ctx.send("pour envoyer ton code , fait ceci")
	  await ctx.send("```ton_langage")
	  await ctx.send("ton code")
	  await ctx.send("```")
	  await ctx.send("exemple :\n ```python\nprint('exemple') \n```")


  @commands.command()
  async def aidemp(self,ctx):
    #envoie un message expliquant pourquoi l'aide en mp est deconseillée
    await ctx.send("l'aide en mp est fortement déconseillée !\ncar elle nuit a l'aprentissage collectif , si vous aidez une personne ne mp les autres ne pourront pas profiter de cette aide.")







def setup(client):
  client.add_cog(Infos(client))