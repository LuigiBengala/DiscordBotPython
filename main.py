import nextcord
import asyncio

from nextcord.ext import commands
from nextcord import FFmpegPCMAudio

intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

async def sendImage(ctx, image):
    await ctx.send(file=nextcord.File(f'./assets/images/{image}.jpg'))
    
@bot.command(name = 'imagetest')
async def image(ctx):
    await sendImage(ctx, 'imageTest')

@bot.command(name = 'imagetest')
async def image(ctx):
  await sendImage(ctx, 'imageTest')
  
    
async def sendMessage(ctx, message):
    await ctx.send(message)
    
@bot.command(name = 'textTest')
async def message(ctx):
    await sendMessage(ctx, 'textMessage')
 
async def playAudio(ctx, name, duration):
    if (ctx.author.voice):
      channel = ctx.message.author.voice.channel
      voice = await channel.connect()
      source = FFmpegPCMAudio('./assets/audios/{name}.mp3')
      voice.play(source)
      await asyncio.sleep(duration)
      await ctx.guild.voice_client.disconnect()
    else:
      await ctx.send("You are not connected to a voice channel.")
      
@bot.command(name = 'audioTest')
async def sendAudio(ctx):
    await playAudio(ctx, 'audioTest', 6)

if __name__ == '__main__':
    bot.run('Your token')
