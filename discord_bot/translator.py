import discord
import os

from data.baseball import mlb



client = discord.Client()
discord_api = os.environ['DISCORD_API']


@client.event
async def on_message(message):

    if message.content.lower().startswith('al west standings'):
        final_form = mlb.ALWestDiscord()


        await message.channel.send(final_form)  

    if message.content.lower().startswith('al east standings'):
        final_form = mlb.ALEastDiscord()


        await message.channel.send(final_form)


    if message.content.lower().startswith('al central standings'):
        final_form = mlb.ALCentralDiscord()


        await message.channel.send(final_form)


    if message.content.lower().startswith('nl west standings'):
        final_form = mlb.NLWestDiscord()


        await message.channel.send(final_form)



    if message.content.lower().startswith('nl east standings'):
        final_form = mlb.NLEastDiscord()


        await message.channel.send(final_form)


    if message.content.lower().startswith('nl central standings'):
        final_form = mlb.NLCentralDiscord()


        await message.channel.send(final_form)


    if message.content.lower().startswith('mlb ba leader'):
        final_form = mlb.LLBattingAvg()


        await message.channel.send(final_form)



    if message.content.lower().startswith('mlb era leader'):
        final_form = mlb.LLERALeader()


        await message.channel.send(final_form)



    if message.content.lower().startswith('mlb homerun leader'):
        final_form = mlb.HomeRunsLeaders()

        await message.channel.send(final_form)


    if message.content.lower().startswith('mlb saves leader'):
        final_form = mlb.SavesLeader()


        await message.channel.send(final_form)


    if message.content.lower().startswith('mlb obps leader'):
        final_form = mlb.OnBasePlusSlugingLeaders()


        await message.channel.send(final_form)

    if message.content.lower().startswith('mlb wins leader'):
        final_form = mlb.WinsLeader()


        await message.channel.send(final_form)


client.run(discord_api)
