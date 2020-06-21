import time
import discord
from discord.ext import commands
import random

class Fun(commands.Cog):


  def __init__(self, bot):
    self.bot = bot

  
  poulets=["https://cdn.discordapp.com/attachments/609504927907315743/701089648851550299/575252fbea6f2580d4f10a0644627df5.jpg","https://cdn.discordapp.com/attachments/609504927907315743/701089649841668146/EVY5YWPXkAE3VzH.jpg","https://cdn.discordapp.com/attachments/609504927907315743/701089650630066307/image003_1.jpg","https://cdn.discordapp.com/attachments/609504927907315743/701089698998911026/booted-bantam-14b1c8ca-4925-4acf-a167-769805efd71-resize-750.jpeg",
  "https://cdn.discordapp.com/attachments/609504927907315743/701089698998911026/booted-bantam-14b1c8ca-4925-4acf-a167-769805efd71-resize-750.jpeg","https://cdn.discordapp.com/attachments/609504927907315743/701090151387889699/bd83755717bbb245026edd9bc0fb4a3c.jpg","https://cdn.discordapp.com/attachments/609504927907315743/701090151639548054/2dfaa9ecb248337c2c6dc4d8675d512f.jpg","https://cdn.discordapp.com/attachments/609504927907315743/701090151857913866/chicken-1.png"]



  @commands.command()
  async def say(self,ctx,*args):
    #creation d'un variable output qui contient ce que le bot doit renvoyer
    output = ''

    #pour chaque mot dans les arguments de la commande , on ajoute ce mot+ un espace a la var output
    for word in args:
      output += word
      output += ' '

    #si : dans la var output il y a @here , le bot envoie un message au lieu de renvoyer @here
    if "@here " in output:
      await ctx.send("non petit malin :^)")

    #et si : @everyone est dans la var output , le bot envoie un message au lieu de renvoyer @everyone
    elif "@everyone" in output:
      await ctx.send("non petit malin :^)")
    #sinon : execution normale du reste de la commande
    else:
      await ctx.send(output)
      messa = ctx.message
      await messa.delete()

  @commands.command()
  async def jaja(self,ctx,target):
    #Y A PAS MOYEN JAJA
    await ctx.send("t'as pas ded ça !")
    await ctx.send(f"c'est pas comme ça qu'on fait le choses , {target} !")

  @commands.command()
  async def figth(self,ctx,combatan):
    chalenjer = ctx.message.author.id
    await ctx.send(f"un combat sans mercie s'enclenche entre <@!{chalenjer}> et {combatan}")
    await ctx.send("qui va gagner......")
    gagnant = [combatan,chalenjer,"personne , vous etes tous nuls"]
    random.shuffle(gagnant)
    random.shuffle(gagnant)
    await ctx.send(f"le gagnant du combat est :")
    if gagnant[0] == chalenjer:
      await ctx.send("<@!{chalenjer}>")
    elif gagnant[0] == combatan:
      await ctx.send(combatan)
    else:
      gagnant[0]


  @commands.command()
  async def poulet(self,ctx):
    poulets=["https://cdn.discordapp.com/attachments/609504927907315743/701089648851550299/575252fbea6f2580d4f10a0644627df5.jpg","https://cdn.discordapp.com/attachments/609504927907315743/701089649841668146/EVY5YWPXkAE3VzH.jpg","https://cdn.discordapp.com/attachments/609504927907315743/701089650630066307/image003_1.jpg","https://cdn.discordapp.com/attachments/609504927907315743/701089698998911026/booted-bantam-14b1c8ca-4925-4acf-a167-769805efd71-resize-750.jpeg",
    "https://cdn.discordapp.com/attachments/609504927907315743/701089698998911026/booted-bantam-14b1c8ca-4925-4acf-a167-769805efd71-resize-750.jpeg","https://cdn.discordapp.com/attachments/609504927907315743/701090151387889699/bd83755717bbb245026edd9bc0fb4a3c.jpg","https://cdn.discordapp.com/attachments/609504927907315743/701090151639548054/2dfaa9ecb248337c2c6dc4d8675d512f.jpg","https://cdn.discordapp.com/attachments/609504927907315743/701090151857913866/chicken-1.png"]
    random.shuffle(poulets)
    poulembed=discord.Embed(title="Un poulet",description="Un magnifique poulet :",color=0x00ffae)
    poulembed.set_image(url=poulets[1])
    await ctx.send(embed=poulembed)

  @commands.command()
  async def homicide(self,ctx,per):
    hh = ctx.message.author.id
    await ctx.send(f"<@!{hh}> a mis fin aux jours de {per}")

    
  









def setup(client):
  client.add_cog(Fun(client))