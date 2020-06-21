import time
import discord
from discord.ext import commands
import random

class Utils(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def suggest(self,ctx, *,args):
    mem = ctx.message.author.id
    blbl = ctx.channel
    no = 1
    sugg = self.bot.get_channel(712593474834137173)
    sembed = discord.Embed(description=":bulb: __**--SUGGESTION--**__ :bulb: ",color=0x00FFAE)
    sembed.add_field(name=":incoming_envelope: |**Suggeré par** : ",value=f"<@!{mem}>",inline=False)
    sembed.add_field(name=":bulb: |**Suggestion** :",value=args,inline=False)
    message = await sugg.send(embed=sembed)
    await message.add_reaction("<:yes:715477940367917056>")
    await message.add_reaction("<:no:715477940288094248>")
    await ctx.send("**__ :white_check_mark: | Suggestion envoyée dans le salon prevu a cet effet !__**")


  






def setup(client):
  client.add_cog(Utils(client))