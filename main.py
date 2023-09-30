import nextcord
import asyncio

from nextcord.ext import commands
from nextcord import FFmpegPCMAudio

intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

async def sendImage(ctx, image):
    await ctx.send(file=nextcord.File(f'./assets/images/{image}.jpg')) # Choose the image this command will send
    
@bot.command(name = 'imagetest')
async def image(ctx):
    await sendImage(ctx, 'imageTest')

@bot.command(name = 'imagetest')
async def image(ctx):
  await SendImage(ctx, 'imageTest')
  
    
async def sendMessage(ctx, message):
    await ctx.send(message) # Choose the message this command will send
    
@bot.command(name = 'textTest')
async def message(ctx):
    await sendMessage(ctx, 'textMessage')
 
async def playAudio(ctx, name):
    if (ctx.author.voice):
      channel = ctx.message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio('./assets/audios/{name}.mp3') # Path to your audio file
      voice.play(source)
      await asyncio.sleep(source.duration) # Set the time to sleep the same as the audio you want to play
      await ctx.guild.voice_client.disconnect()
    else:
      await ctx.send("You are not connected to a voice channel.")
      
@bot.command(name = 'audioTest')
async def sendAudio(ctx):
    await playAudio(ctx, 'audioTest') # Choose the audio this command will play

if __name__ == '__main__':
    bot.run('Your token')
