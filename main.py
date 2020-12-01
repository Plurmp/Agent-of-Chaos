import random
from os import environ as cred

import discord

client = discord.Client()
TOKEN = cred['DISCORD_TOKEN']


@client.event
async def on_message(message):
	print('message')
	for r in message.role_mentions:
		if r.id == 783392898619408425:  # @someone
			print('detected thing')
			members = message.guild.members
			victim = members[random.randrange(len(members))]
			await message.channel.send(f"{victim.mention()}")
			return

client.run(TOKEN)
