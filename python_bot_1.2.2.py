import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot
import pyjokes
from discord_bot_secret import super_secret_secret
from google import google

BOT_PREFIX = ("-")
TOKEN = super_secret_secret
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


@client.command(name='google',
                description="format: -google <optional: [(number of results) <= 9]> <query>",
                brief="Googles Stuff",
                aliases=["search"],
                pass_context=True)
async def googler(context):
    a = context.message.content
    stuff = ""
    try:
        b = int(a[8])
    except:
        query = a[7:]
        num = 2
    else:
        query = a[9:]
        num = b
    search_results = google.search(query)
    for i in search_results[:num]:
        name = i.name[:i.name.index("/")-6]
        stuff += f"**{name}**\n{i.description} \n(<{i.link}>)\n\n"
    if len(stuff) > 2000:
        await client.say("Bro your request size is to **big**, try and tone it down maybe a little bit")
    else:
        await client.say(stuff)


@client.command(name='joke',
                description="pulls a random joke from the pyjoke module",
                brief="tells a joke",
                pass_context=True)
async def joke(context):
    await client.say(pyjokes.get_joke())


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
                description="format: -chastise @<anyone you want>",
                brief="verbally beats you up!",
                aliases=[],
                pass_context=True)
async def chastise(context):
    print(context.message.content[10:32] == "<@!359794541257162753>")
    print(context.message.content[10:32])
    print("<@!359794541257162753>")
    if context.message.content[10:32] == "<@!359794541257162753>":
        possible_responses = [
            f"Did you really think you could turn me against my master {context.message.author.mention}? Or are you jus"
            f"t dumb? Either way <@!359794541257162753> is my creater and I won't disrespect him"
        ]
    else:
        possible_responses = [
            f"Were you being bad {context.message.content[10:]}? or are you just slow?",
            f"How many times have I told you {context.message.content[10:]}! Don't be slow and eat your cereal!",
            f"When I looked up a picture of bad people who don't do their homework, I see a p"
            f"icture of you! {context.message.content[10:]}"
        ]
    await client.delete_message(context.message)
    await client.send_message(context.message.channel, random.choice(possible_responses))


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with my mixtape (check my soundcloud!)"))
    print("Logged in as " + client.user.name)


@client.command(name='Math',
                description="Does any math you could possible want, make sure to use many parenthesis",
                brief="Does math",
                aliases=['m', 'mathematics', "digits", "math"])
async def math(number):
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
