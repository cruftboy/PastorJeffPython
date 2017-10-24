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
	if('lord' in  message.author.display_name):
		lord = message.author
		await client.change_nickname(lord, "sinner")

	if(message.author.id != client.user.id):
	    messagelower = message.content
	    messagelower = messagelower.lower()
	    if('heck' in messagelower or 'hell' in messagelower or 'fuck' in messagelower or 'shit' in messagelower or 'cunt' in messagelower or 'bitch' in messagelower or 'ass' in messagelower or 'butt' in messagelower or 'bum' in messagelower or 'frick' in messagelower or 'damn' in messagelower or 'darn' in messagelower or 'dang' in messagelower or 'bastard' in messagelower or 'anus' in messagelower or 'gosh' in messagelower or 'fart' in messagelower or 'stupid' in messagelower or 'idiot' in messagelower):
	    	await client.send_message(message.channel, 'Sorry sir, this is a christian server, so no swearing')
	    elif('@' in messagelower):
	    	await client.send_message(message.channel, 'I would rather @ the lord with my prayers!')
client.run('MzcwMjg2MTAzMjkyNDExOTA3.DM_ZDQ.Lif3NSbl4aCBecwJ2qZl-6yuLV4')
