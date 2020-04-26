import discord
from discord.ext import commands


client = commands.Bot(command_prefix='<')





@client.event
async def on_ready():
  print("bot is ready !")
  game = discord.Game("corriger des SyntaxError | <aide | W.I.P")
  await client.change_presence(status=discord.Status.do_not_disturb, activity=game)


@client.event
async def on_member_join(member):
  wlcmchannel = client.get_channel(702949674583195739)
  await wlcmchannel.send(f"bienvenue a toi @{member} dans le serveur TechNewsFR.   un serveur regroupant une communauté grandissante de développeurs et passionnés d'informatique et technologie ! , un serveur tres amusant ou tu ne t'enuiras jamais , et ou tu trouveras la reponse a tes questions ;). ")
  await wlcmchannel.send(f"`-et toi tki ? tkoi ?`")
  await wlcmchannel.send(f" je suis le bot de la TechNewsFR serveur codé par kross.  il suffit de faire `/aide` pour en savoir plus sur comment m'utiliser ! ")

@client.event
async def on_member_remove(member):
	wlcmchannel = client.get_channel(702949674583195739)
	await wlcmchannel.send(f"{member} a quitté le serveur , bon depart ! ")



@client.command()
async def aide(ctx):
  embed=discord.Embed(title="voici la liste des commandes normales (utilisables par les membres)", color=0xdd00c7)
  embed.set_author(name="Tech News Fr bot")
  embed.add_field(name="<aide", value="envoies ceci en mp", inline=True)
  embed.add_field(name="<say [message] ", value="faites dire nimporte quoi au bot", inline=True)
  embed.add_field(name="<", value=".", inline=True)
  embed.add_field(name="<", value=".", inline=True)
  embed.add_field(name="<", value=".", inline=True)
  embed.add_field(name="<", value=".", inline=True)
  embed.add_field(name="<", value=".", inline=True)
  embed.add_field(name="<", value=".", inline=True)
  embed.add_field(name="<", value=".", inline=True)
  embed.add_field(name="<",value=".")
  embed.add_field(name="<", value=".", inline=True)
  embed.add_field(name="<", value=".", inline=True)
  embed.add_field(name="<", value=".", inline=True)
  embed.set_footer(text="[obligatoire] / {facultatif} / (valeur par defaut)")
  
  embed2=discord.Embed(title="voici la liste des commandes staff (utilisables que par le staff)", color=0x03aada)
  embed2.set_author(name="Tech News Fr bot")
  embed2.add_field(name="<clear {nombre de msg(10)}", value="supprime {nombre de msg} messages , si {nombre de msg} est vide , supp 10", inline=True)
  embed2.add_field(name="<ban [user] {raison}", value="ban une personne", inline=True)
  embed2.add_field(name="<kick [user] {raison} ", value="kick une personne", inline=True)
  embed2.add_field(name="le reste comming soon", value=";)", inline=True)
  embed2.set_footer(text="[obligatoire] / {facultatif} / (valeur par defaut)")
  

  channel = await ctx.message.author.create_dm()
  await channel.send(embed=embed)
  await channel.send(embed=embed2)
  await ctx.send("message d'aide *envoyé* ! (regarde tes mp ^^)")


@client.command()
async def code(ctx):
	await ctx.send("pour envoyer ton code , fait ceci")
	await ctx.send("```ton_langage")
	await ctx.send("ton code")
	await ctx.send("```")
	await ctx.send("exemple :\n ```python \n print('exemple') \n ```")



@client.command()
async def say(ctx,*args):
  output = ''
  for word in args:
    output += word
    output += ' '
  await ctx.send(output)
  messa = ctx.message
  await messa.delete()


@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount = 10):
  await ctx.channel.purge(limit=amount)
  await ctx.send(f"{amount} messages supprimés !")

@client.command()
@commands.has_permissions(kick_members=True, ban_members=True)
async def kick(ctx, member : discord.Member, *, reason="pas de raison"):
    await member.kick(reason=reason)
    bb = ctx.message.author
    kembed=discord.Embed(title=f"KOK KE KO , {member} s'est fait jarter du serveur",color=0xff1100)
    kickpar = f"kick bar {bb}"
    kembed.add_field(name="raison :",value=reason)
    kembed.add_field(name="kick par :",value=bb)
    await ctx.send(embed = kembed)

@client.command()
@commands.has_permissions(kick_members=True, ban_members=True)
async def ban(ctx, member : discord.Member, *, reason="pas de raison"):
    await member.ban(reason=reason)
    bd = ctx.message.author
    banpar = f"ban par : {bd}"
    bembed=discord.Embed(title=f"{member} s'est pris le ban hammer",color=0xff1100 )
    bembed.add_field(name="raison :",value=reason)
    bembed.add_field(name="ban par :",value=bd)
    await ctx.send(embed = bembed)




client.run("NzA0MDk3MTA1NjE4MTQxMTg1.XqYWrg.WULpxknMxv8SW4Bha7vPmX9YnJY")
