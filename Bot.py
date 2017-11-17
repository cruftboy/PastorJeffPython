import discord
import asyncio
import random
from Backend import * 
import pandas as pd
import os

csv_training_df = pd.read_csv('nice_mean_v4.csv',header=None)
df = build_training_set(csv_training_df)

model, model_lemmas = build_model(df)




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
		prediction = predict(model, model_lemmas, message.content)
		if(prediction[0] == 1):
			await client.send_message(message.channel, 'You mean, stop.')
		else:
			await client.send_message(message.channel, 'You is nice, keep it up!')

client.run('MzcwMjg2MTAzMjkyNDExOTA3.DM_ZDQ.Lif3NSbl4aCBecwJ2qZl-6yuLV4')
