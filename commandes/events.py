import time
import discord
from discord.ext import commands
import random

class Events(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


  #event : quand un membre rejoins
  @commands.Cog.listener()
  async def on_member_join(member):
    #creation d'un salon mp , et envoi d'un message dessus
    dm = await member.create_dm()
    await dm.send(f"__**Bienvenue a toi @{member} sur GoDev.**__ \n \n Nous sommes un serveur regroupant une communauté grandissante de développeurs et passionnés d'informatique et technologie ! , un serveur tres amusant ou tu ne t'enuiras jamais , et où tu trouveras la reponse a tes questions ;). \n \n avant tout , tu dois lire le règlement du serveur dans <#712590475906777089> et de choisir tes roles dans <#712628072620228658>. \n \n `-et toi tki ? tkoi ?`\n Je suis le Bot de GoDev serveur codé par Kross et Netark.  Il suffit de faire `<aide` pour en savoir plus sur comment m'utiliser ! ")








def setup(client):
  client.add_cog(Events(client))