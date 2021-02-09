import discord
import os
import json
import random
import requests
from dotenv import load_dotenv

client = discord.Client()

def get_quote():
    url = "https://matchilling-tronald-dump-v1.p.rapidapi.com/random/quote"
    headers = {
    'accept': "application/hal+json",
    'x-rapidapi-key': "6f9b6c45dfmsh2a34dcc15468702p15bd50jsnf6e1c8194a6c",
    'x-rapidapi-host': "matchilling-tronald-dump-v1.p.rapidapi.com"
    }
    quote = requests.request('GET', url, headers=headers)
    json_data = json.loads(quote.text)
    response = json_data['value']
    return(response)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Trump?'):
        quote = get_quote()
        await message.author.send("Trump is watching you")
        await message.author.send(file=discord.File('file.jpg'))
        await message.channel.send(quote)

load_dotenv()

client.run(os.getenv('TOKEN'))