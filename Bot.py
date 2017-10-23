import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
	if message.author.id != client.user.id:
	    if('heck' in message.content or 'hell' in message.content or 'fuck' in message.content or 'shit' in message.content or 'cunt' in message.content or 'bitch' in message.content or 'ass' in message.content or 'butt' in message.content or 'bum' in message.content or 'frick' in message.content or 'damn' in message.content or 'darn' in message.content or 'dang' in message.content or 'bastard' in message.content or 'anus' in message.content or 'gosh' in message.content or 'fart' in message.content or 'stupid' in message.content or 'idiot' in message.content):
	       await client.send_message(message.channel, 'Sorry sir, this is a christian server, so no swearing')
	    elif('@' in message.content):
	    	await client.send_message(message.channel, 'I would rather @ the lord with my prayers')
client.run('MzcwMjg2MTAzMjkyNDExOTA3.DM_ZDQ.Lif3NSbl4aCBecwJ2qZl-6yuLV4')
