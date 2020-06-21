import discord
from discord.ext import commands
import os
import asyncio
import webserver
from webserver import keepalive
import os
import time
import random


client = commands.Bot(command_prefix='<')

@client.event
async def on_ready():
    #affiche un message dans la console
    print("bot is ready !")
    #change le statut du bot
    game = discord.Game("Corriger des SyntaxError | <help | W.I.P")
    await client.change_presence(status=discord.Status.online, activity=game)


#--------------------------------MESSAGES-------------------------
@client.command()
async def r1(ctx):
  embed=discord.Embed(description="❯ `Tu es débutant, amateur, expert ou étudiant en informatique ?`",color=0x0d92ff)
  embed.add_field(name="-------------------------------------------------------------------------", value="Clique sur la réaction 🚀  si tu es débutant en informatique.",inline=False)
  embed.add_field(name="-------------------------------------------------------------------------", value="Clique sur la réaction 👌  si tu es amateur en informatique.",inline=False)
  embed.add_field(name="-------------------------------------------------------------------------", value="Clique sur la réaction  💼  si tu es expert en informatique.",inline=False)
  embed.add_field(name="-------------------------------------------------------------------------", value="Clique sur la réaction 🎓  si tu es étudiant en informatique.",inline=False)
  await ctx.send(embed=embed)


@client.command()
async def r2(ctx):
  embed=discord.Embed(description="❯ `Que fais-tu dans ta vie ?`",color=0x0d92ff)
  embed.add_field(name="-------------------------------------------------------------------------", value="Clique sur la réaction 💻 si tu es un développeur",inline=False)
  embed.add_field(name="-------------------------------------------------------------------------", value="Clique sur la réaction 🎮  si tu es un un gamer.",inline=False)
  embed.add_field(name="-------------------------------------------------------------------------", value="Clique sur la réaction 🔧  si tu es un un passioné d' hardware.",inline=False)
  embed.add_field(name="-------------------------------------------------------------------------", value="Clique sur la réaction ☠️ si tu es un un expert en cyber-sécurité \n ou un ethical hacker ",inline=False)
  embed.set_footer(text="les roles dev hacker hardware ont des salons speciaux , choisissez les pour y acceder")
  await ctx.send(embed=embed)

@client.command()
async def r3(ctx):
  embed=discord.Embed(description="❯ `Quelles notifications souhaites-tu recevoir ?`",color=0x0d92ff)
  embed.add_field(name="-------------------------------------------------------------------------", value="Clique sur la réaction 🔎 si tu souhaites recevoir des Notif. Annonces.",inline=False)
  embed.add_field(name="-------------------------------------------------------------------------", value="Clique sur la réaction 📊 si tu souhaites recevoir des Notif. Sondages.",inline=False)
  embed.add_field(name="-------------------------------------------------------------------------", value="Clique sur la réaction 🎉 si tu souhaites recevoir des Notif. Animations.",inline=False)
  embed.add_field(name="-------------------------------------------------------------------------", value="Clique sur la réaction 🔔 si tu souhaites recevoir des Notif. Recrutements.",inline=False)
  embed.add_field(name="-------------------------------------------------------------------------", 
  value="Clique sur la réaction 🤝 si tu souhaites recevoir des Notif. Partenairiats.",inline=False)
  embed.set_footer(text="il y'aura quand meme des @€veryone de temps en temps")
  await ctx.send(embed=embed)

@client.command()
async def r(ctx):
  rembed=discord.Embed(description="**__Règlement du serveur GoDev__**",color=0x0d92ff)
  rembed.add_field(name="règle n°1", value="Le manque de respect, les insultes à caractère raciste, haineux, homophobe, religieux ou encore sexiste sont strictement interdites.", inline=False)
  rembed.add_field(name="règle n°2", value="Le spam , flood , spam emoji , et tout autre comportement pouvant gêner la conversation , est interdit. ", inline=False)
  rembed.add_field(name="règle n°3", value="Respectez l'utilité des salons , les commandes par exemple , se font dans #terminal-bots", inline=False)
  rembed.add_field(name="règle n°4", value="Concernant l'aide : l'aide en mp et le spoonfeed , sont très sévèrement punies car nuisent a l'apprentissage. essayez d’être utiles , pas de juste balancer un 'lis les docs'.", inline=False)
  rembed.add_field(name="règle n°5", value="Concernant les demandes d'aide : structurez correctement votre question , et essayez de chercher un minimum une réponse (sur internet/stackoverflow ect) , ne faites pas de demandes foireuses , ou illégales ex : 'tristan il ma hak je vé vanjai sal , koman on daidaiosaisse ?'", inline=False)
  rembed.add_field(name="règle n°6", value="La publicité en mp , ou dans autre que le salon prevu a cet effet , sera sévèrement sanctionnée ", inline=False)
  rembed.add_field(name="règle n°7", value="Le contenu not safe for work (gore/porno ou tout contenu choquant) est interdit.", inline=False)
  rembed.add_field(name="règle n°8", value="Respectez le Conditions d’utilisations de Discord : https://discordapp.com/guidelines", inline=False)
  rembed.set_footer(text="La Modération et l'Administration se réserve le droit de prendre les mesures appropriées afin de préserver une ambiance conviviale, et ce sans avoir à se justifier.")
  await ctx.send(embed=rembed)

@client.command()
async def i(ctx):
  iembed=discord.Embed(description="**__Informations__**",color=0x0d92ff)
  iembed.add_field(name="** **",value="-n'oubliez pas de choisir vos rôles dans <#712628072620228658>", inline=True)
  iembed.add_field(name="** **",value="-les règles si dessus sont a lire obligatoirement (ou ça risque de pas bien finir)", inline=True)
  iembed.add_field(name="** **", value="n'oubliez pas de <@&712696023343955989> et de lire la description des salons (vous y trouverez des infos tres utiles ! )", inline=True)
  await ctx.send(embed=iembed)

@client.command()
async def p(ctx):
  pembed=discord.Embed(description="**__Présentation__**",color=0x0d92ff)
  pembed.set_thumbnail(url="https://media.discordapp.net/attachments/707931268024762388/712695631470264350/imgonline-com-ua-Color-filter-one-tone-LcPNxqy5l5De.jpg?width=406&height=406")
  pembed.add_field(name="Bienvenue sur GoDev", value="Un serveur basé sur l'informatique , et l'entraide. un serveur ou vous trouverez des développeurs , des hackers et des passionnés d'informatique en tout genre ! ", inline=True)
  await ctx.send(embed=pembed)

@client.command()
async def b(ctx):
  bembed=discord.Embed(description=":warning: Attention :warning:",color=0xff550d)
  bembed.add_field(name="** **",value="Vous avez 5 minutes pour répondre au Captcha.", inline=False)
  bembed.add_field(name="** **",value="Sinon le FIREWALL va vous exclure du serveur discord", inline=False)
  bembed.set_footer(text="")
  await ctx.send(embed=bembed)


for file in os.listdir("commandes"):
    if file.endswith(".py"):
        name = file[:-3]
        client.load_extension(f"commandes.{name}")



keepalive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)




