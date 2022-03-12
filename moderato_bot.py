import asyncio
import nextcord
import json



discord = nextcord

with open("properties.json") as file:
    data = json.load(file)



data2 = (data["Token"])
data3 = (data["bannedwords"]["First"])
data4 = (data["bannedwords"]["Two"])
data5 = (data["bannedwords"]["Harom"])
data6 = (data["bannedwords"]["Negy"])
data7 = (data["bannedwords"]["5"])
data8 = (data["bannedwords"]["6"])
data9 = (data["bannedwords"]["7"])
data10 = (data["bannedwords"]["8"])
data11 = (data["bannedwords"]["9"])
data12 = (data["bannedwords"]["10"])
data13 = (data["bannedwords"]["11"])
data14 = (data["bannedwords"]["12"])
data15 = (data["bannedwords"]["13"])
data16 = (data["bannedwords"]["14"])
data17 = (data["bannedwords"]["15"])
data18 = (data["bannedwords"]["18"])
data19 = (data["bannedwords"]["19"])
data20 = (data["bannedwords"]["20"])



client = nextcord.Client()



@client.event
async def on_ready():
    print('Wir sind eingeloggt als User {}'.format(client.user.name))


@client.event
async def on_message(message):
 if data3 in message.content:
      await message.delete()
      print(message.author, "has speaked black word")
 if data4 in message.content:
      await message.delete()
      print(message.author, "has speaked black word") 
 if data5 in message.content:
      await message.delete()
      print(message.author, "has speaked black word")       
 if data6 in message.content:
      await message.delete()
      print(message.author, "has speaked black word")
 if data7 in message.content:
      await message.delete()
      print(message.author, "has speaked black word")
 if data8 in message.content:
      await message.delete()
      print(message.author, "has speaked black word")                                        
 if data9 in message.content:
      await message.delete()
      print(message.author, "has speaked black word")  
 if data10 in message.content:
      await message.delete()
      print(message.author, "has speaked black word") 
 if data11 in message.content:
      await message.delete()
      print(message.author, "has speaked black word")
 if data12 in message.content:
      await message.delete()
      print(message.author, "has speaked black word") 
 if data13 in message.content:
      await message.delete()
      print(message.author, "has speaked black word") 
 if data14 in message.content:
      await message.delete()
      print(message.author, "has speaked black word")
 if data15 in message.content:
      await message.delete()
      print(message.author, "has speaked black word")   
 if data16 in message.content:
      await message.delete()
      print(message.author, "has speaked black word")                              
 if data17 in message.content:
      await message.delete()
      print(message.author, "has speaked black word") 
 if data18 in message.content:
      await message.delete()
      print(message.author, "has speaked black word") 
 if data19 in message.content:
      await message.delete()
      print(message.author, "has speaked black word")  
 if data20 in message.content:
      await message.delete()
      print(message.author, "has speaked black word")
                

                            
                             

      
client.run(data2)