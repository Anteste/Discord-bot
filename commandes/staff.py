import time
import discord
from discord.ext import commands
import random

class Staff(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


  #commande d'expulsion
  @commands.command()
  @commands.has_permissions(kick_members=True, ban_members=True)
  async def kick(self,ctx, member : discord.Member, *, reason="pas de raison"):
    #recup. de l'id de l'executeur de la commande
    bb = ctx.message.author.id

    #creation de l'embed pour le message du ban
    kembed=discord.Embed(title=f"{member} s'est fait expulser du serveur",color=0xff1100)
    kembed.add_field(name="raison :",value=reason)
    kembed.add_field(name="kick par :",value=f"<@!{bb}>")

    #creation d'un channel mp
    a = await member.create_dm()

     #envoi d messages au membre kick
    await a.send("tu a été kick du serveur !")
    await a.send(embed= kembed)

    #kick du membre et envoi du message de ban
    await member.kick(reason=reason)
    await ctx.send(embed = kembed)

  #commande de banissement
  @commands.command()
  @commands.has_permissions(kick_members=True, ban_members=True)
  async def ban(self,ctx, member : discord.Member, *, reason="pas de raison"):

    #recup. de l'id de l'executeur de la commande
    bd = ctx.message.author.id

    #creation de l'embed pour le message de ban
    bembed=discord.Embed(title=f"{member} s'est fait bannir du serveur",color=0xff1100 )
    bembed.add_field(name="raison :",value=reason)
    bembed.add_field(name="ban par :",value=f"<@!{bd}>")

    #creation d'un chanell mp
    b = await member.create_dm()

    #envoi de messages au membre banni
    await b.send("tu a été ban du server !")
    await b.send(embed = bembed)

    #banissement du membre
    await member.ban(reason=reason)

    #envoi de l'embed
    await ctx.send(embed = bembed)

  @commands.command(pass_context=True)
  @commands.has_permissions(manage_messages=True)
  async def clear(self,ctx, amount = 10):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"{amount} messages supprimés !")
    time.sleep(0.5)
    await ctx.channel.purge(limit=1)

  #commande d'annonce
  @commands.command()
  async def announce(self,ctx, *,args):
    #creation de l'embed de l'annonce avec l'argument de la commande
    ann = discord.Embed(description="__**ANNONCE :**__",color=0x24d12f)
    ann.add_field(name=":",value=args)

    #envoi de l'embed
    await ctx.send(embed= ann)



def setup(client):
    client.add_cog(Staff(client))