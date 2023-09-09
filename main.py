import nextcord
import asyncio

from nextcord.ext import commands
from nextcord import FFmpegPCMAudio

intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name = 'imagetest')
async def SendImage(ctx):
    await ctx.send(file=nextcord.File('./assets/images/imageTest.jpg')) # Choose the image this command will send

@bot.command(name = 'textTest')
async def SendMessage(ctx):
    await ctx.send('this message was sucessufuly sent') # Choose the message this command will send
 
@bot.command(name = 'textAudio')
async def join(ctx):
    if (ctx.author.voice):
      channel = ctx.message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio('./assets/audios/samsung.wav') # Path to your audio file
      voice.play(source)
      await asyncio.sleep(2) # Set the time to sleep the same as the audio you want to play
      await ctx.guild.voice_client.disconnect()
    else:
      await ctx.send("You are not connected to a voice channel.")

if __name__ == '__main__':
    bot.run('Your token')
