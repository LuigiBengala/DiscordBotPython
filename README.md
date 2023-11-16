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

