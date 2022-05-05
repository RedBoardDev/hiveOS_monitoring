import discord
import asyncio
import requests
from dotenv import dotenv_values
from get_request import get_workers_metrics
from checking_temperature import checking_temperature

####################INITS_VARIABLE####################
client = discord.Client()
secrets = dotenv_values(".env")
token_discord = secrets["DISCORD_TOKEN"]
######################MAIN#################################

@client.event
async def on_ready():
    len_temp = len(get_workers_metrics()['temp'])
    toggle_temp:list = [False] * len_temp
    toggle_memtemp:list = [False]* len_temp
    print("The bot is ready !")
    checking_temperature.start(client, toggle_temp, toggle_memtemp)
client.run(token_discord)
