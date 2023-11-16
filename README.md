# Discord Bot with Python

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following packages.

> **Important:** Some cases you need to use pip3 instead of pip

```bash
pip install nextcord
```

```bash
pip install asyncio
```

```bash
pip install PyNaCl
```

## Adding an image to the bot

1. Add the image to the folder `assets/images/`
2. Replace the `{image}` with the name you gave to the image

> **Note:** The image must be in `.jpg` format, if the image is in another format, you must change the extension in the code or the extention in the image

```python
async def sendImage(ctx, image):
    await ctx.send(file=nextcord.File(f'./assets/images/{image}.jpg'))
```

1. Change the `imageTest` with the name you gave to the image

> **Note:** The name of the image must be the same as the name of the command, `do not include the file extension`

```python
@bot.command(name = 'imagetest')
async def image(ctx):
    await sendImage(ctx, 'imageTest')
```

## Adding an audio to the bot

1. Add the audio to the folder `assets/audios/`
2. Replace the `{audio}`, in the `playAudio` function, with the name you gave to the audio

> **Note:** The audio must be in `.mp3` format, if the audio is in another format, you must change the extension in the code or the extention in the audio

```python
      source = FFmpegPCMAudio('./assets/audios/{name}.mp3')
```

1. Change the `audioTest` with the name you gave to the audio
2. Change `6` with the duration of the audio.

> **Note:** The duration of the audio must be in seconds

```python
@bot.command(name = 'audioTest')
async def sendAudio(ctx):
    await playAudio(ctx, 'audioTest', 6)
```

## Sending text with a command

1. Change the `textMessage` with the text you want to send

> **Note:** both the `@bot.command` `textTest` is the comand the bot will use to send the text, the `textMessage` is the message the bot will send when the command is used

```python

```python
@bot.command(name = 'textTest')
async def message(ctx):
    await sendMessage(ctx, 'textMessage')
```

## Token

1. Change the `token` with the token of your bot. If you don't know how to get the token, [click here](https://docs.discordbotstudio.org/setting-up-dbs/finding-your-bot-token)

```python
    bot.run('Your token')
```