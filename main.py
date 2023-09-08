import nextcord
import discord
import asyncio
from nextcord.ext import commands
from discord import FFmpegPCMAudio

intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name = 'imagetest')
async def SendImage(ctx):
    await ctx.send(file=nextcord.File('./assets/images/imageTest.jpg'))

@bot.command(name = 'textTest')
async def SendMessage(ctx):
    await ctx.send('this message was sucessufuly sent')
 
 
@bot.command(name = 'samsung')
async def join(ctx):
    if (ctx.author.voice):
      channel = ctx.message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio('./assets/audios/samsung.wav')
      voice.play(source)
      await asyncio.sleep(2)
      await ctx.guild.voice_client.disconnect()
    else:
      await ctx.send("You are not connected to a voice channel.")

if __name__ == '__main__':
    bot.run('MTE0OTQ3ODA5ODcxNTI3OTQ5MA.GvZpc9.ZopgbWPTD-MSVa0aPbDfo4IlIuIwLNhvPn-BaA')