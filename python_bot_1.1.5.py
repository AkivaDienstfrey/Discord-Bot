import random
import asyncio
import aiohttp
import json
import os
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("?", "!", "-")
TOKEN = "<PUT YOUR TOKEN HERE>"

client = Bot(command_prefix=BOT_PREFIX)


@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
        "No you're just bad, plus you owe me money"
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.event
async def on_message(message):
    if message.author != client.user and message.content[:9] == "-chastise":
        if message.content[10:] != "@Johnny Wobble#1085":
            print("confirmed stage 2")
            responses = [
                f"Were you being bad {message.content[10:]}? or are you just slow?",
                f"How many time have I told you {message.content[10:]}! Don't be slow and eat your cereal!",
                f"When I looked up a picture of bad people who don't do their homework, I see a p"
                f"icture of you! {message.content[10:]}"
            ]
            await client.delete_message(message)
            await client.send_message(message.channel, random.choice(responses))
        else:
            print("confirmed stage 3")
            await client.send_message(message.channel, f"Ah, I see you {message.author.mention}, trying to turn me agai"
            f"nst my master eh? Well I say no! I cannot believe you would think that I would ever do that to the all-po"
            f"werful Max (Gordon)!")


@client.command(name='yeet',
                description="type it and find out",
                brief="yeet.",
                pass_context=True)
async def yeet(context):
    possible_responses = [
        'Ha, you got yeeted',
        'Was that a plane, nope it was a flying yeet',
        'Thats a yeet',
        'Nope take that "L"'
    ]
    await  client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.command(name='chastise',
                description="Chastises someone if you @ them after the command",
                brief="verbally beats you up!",
                aliases=[],
                pass_context=True)
async def chastise(context):
    possible_responses = [
        # message.content[10:]\
        " "
    ]
    await client.say(random.choice(possible_responses))


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with my mixtape (check my soundcloud!)"))
    print("Logged in as " + client.user.name)


@client.command(name='Math',
                description="Does any math you could possible want, make sure to use many parenthesis",
                brief="Does math",
                aliases=['m', 'mathematics', "digits", "math"])
async def square(number):
    mathy = number.replace("^", "**")
    mathy1 = eval(mathy)
    await client.say(str(number) + " mathed is " + str(mathy1))


@client.command(name='bitcoin',
                description="gives the bitcoin price in USD (in case you wanted to know)",
                brief="Bitcoin price in $$",
                aliases=['gimmethatbit'])
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("Bitcoin price is: $" + response['bpi']['USD']['rate'])


async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        print("-----------------")
        await asyncio.sleep(6000)


client.loop.create_task(list_servers())
client.run(TOKEN)
