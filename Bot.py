import discord
import asyncio
import random


client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')



@client.event
async def on_message(message):
	if(message.author.id != client.user.id):


		#Mak member list
		members = []

		for member in client.get_all_members():
			members.append(member)

		#Lord check
		if('lord' in  message.author.display_name or 'Lord' in  message.author.display_name):
			lord = message.author
			await client.change_nickname(lord, 'sinner')
			await client.send_message(message.channel, 'Impersonating the lord is a sin, so you are a sinner')

		messagelower = message.content
		messagelower = messagelower.lower()


		#Answers
		if('heck' in messagelower or 'hell' in messagelower or 'fuck' in messagelower or 'shit' in messagelower or 'cunt' in messagelower or 'bitch' in messagelower or 'ass' in messagelower or 'butt' in messagelower or 'bum' in messagelower or 'frick' in messagelower or 'damn' in messagelower or 'darn' in messagelower or 'dang' in messagelower or 'bastard' in messagelower or 'anus' in messagelower or 'gosh' in messagelower or 'fart' in messagelower or 'stupid' in messagelower or 'idiot' in messagelower):
			await client.send_message(message.channel, 'Sorry sir, this is a christian server, so no swearing')
		elif('@' in messagelower):
			await client.send_message(message.channel, 'I would rather @ the lord with my prayers!')
		elif("who's here" in messagelower or "who is here" in messagelower):
			await client.send_message(message.channel, members)

		#Password
		elif(message.content == 'MzcwMjg2MTAzMjkyNDExOTA3.DM_ZDQ.Lif3NSbl4aCBecwJ2qZl-6yuLV4'):
			await client.delete_message(message)

			#New Lucky Boy
			role = discord.utils.get(message.server.roles, name="Lucky boy")

			for member in members:
				for allroles in member.roles:
					if(role in member.roles):
						await client.remove_roles(member, role)


			added = False

			while(added != True):
				lucky = random.choice(members)
				try:
					await client.add_roles(lucky, role)
					added = True
				except discord.Forbidden:
					added = False

client.run('MzcwMjg2MTAzMjkyNDExOTA3.DM_ZDQ.Lif3NSbl4aCBecwJ2qZl-6yuLV4')
