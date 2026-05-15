import discord
from discord.ext import commands
from config import TOKEN
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='$', intents=intents)
@client.event 
async def on_ready():
    print(f'Giriş yapıldı {client.user}')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(client.command_prefix):
        await client.process_commands(message)
    else:
        await message.channel.send(message.content)
        
@client.command()
async def about(ctx):
    await ctx.send("Ben bir eko botum!")
   
client.run(TOKEN)
