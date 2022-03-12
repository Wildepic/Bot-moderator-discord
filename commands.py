import asyncio
import nextcord
import json

with open("properties.json") as file:
    data = json.load(file)

data2 = (data["Token"])
discord = nextcord
client = nextcord.Client()

@client.event
async def on_message(message):
 if message.content =="/help" :
      await message.channel.send("when you have a proplem with this bot write here a ticket https://discord.gg/eJCeCwArGj when with the server /server")
 if message.content =="/server" :
      await message.channel.send("Contact the Staff of the server when there is a ticket option make a ticket")

      
      

client.run(data2)