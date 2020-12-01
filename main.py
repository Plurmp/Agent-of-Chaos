import random
from os import environ as cred

import discord

client = discord.Client()
TOKEN = cred['DISCORD_TOKEN']


@client.event
async def on_message(message):
	for r in message.role_mentions:
		if r.int == 783392898619408425:  # @someone
			members = message.guild.members
			victim = members[random.randrange(len(members) - 1)]
			await message.channel.send(victim.mention())
			return

client.run(TOKEN)
