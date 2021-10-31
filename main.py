# 904287797865766913 app id
# OTA0Mjg3Nzk3ODY1NzY2OTEz.YX5Vow.Yi6HnbTn9abFnyUsh9dIUWKsoNw tpken
#481036818496 permission
#https://discord.com/api/oauth2/authorize?client_id=904287797865766913&permissions=412317349952&scope=bot aut

import discord
client = discord.Client()

#bot online
@client.event
async def on_ready():
    print(f"Logged in as{client.user}")

#bot interact message
@client.event
async def on_message(message):
    if message.content == "!Hello":
        print(message.channel)
        await  message.channel.send('Hello ' + str(message.author.name))

    elif message.content == '!bye':
        print(message.channel)
        await message.channel.send('Good bye')

client.run('OTA0Mjg3Nzk3ODY1NzY2OTEz.YX5Vow.Yi6HnbTn9abFnyUsh9dIUWKsoNw')