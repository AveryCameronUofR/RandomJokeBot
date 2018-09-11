import discord
from discord.ext import commands
import random
from random import randint
recent = [101]
question = ' '
answer = ' '

token = 'MzgyOTkxNjA1MDcxNzQwOTI4.DPdwXQ.6dmaGr5xNTPifZW9Lci1IoCOTrc'
client = discord.Client()

bot = commands.Bot(command_prefix='#', description='A bot that randomly posts a joke to a discord channel')
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)


async def splitJoke(fullJoke):
    splitVersion = fullJoke.split('Answer123')
    question = splitVersion[0]
    answer = splitVersion[1]
    if 'KnockKnock' not in fullJoke:
        await bot.say(question)
        await bot.say(answer)
    else:
        questionk = question.split('KnockKnock')
        question = questionk[1]
        await bot.say('Knock Knock')
        await bot.say('Who\'s there?')
        await bot.say(question)
        await bot.say(question + ' who?')
        await bot.say(answer)

def randomJoke():
    """Gets a random Joke"""
    joke = getJoke()
    return joke

def getJoke():
    num = random.randint(1,10)
    if num not in recent:
        recent.append(num)
    else:
        if len(recent) == 10:
            recent.pop(0)
        while (num in recent):
            num = random.randint(1,10)
        recent.append(num)
    counter = 0
    jokes = open("jokes.txt")
    while counter <num:
        fullJoke = jokes.readline()
        counter = counter+1
    return fullJoke

@bot.command()
async def info():
    await bot.say("Welcome to the Joke Bot" "\nThis Bot is used for Random Jokes\
    \n\nSome simple commands are:\
    \n#suggest *text* to suggest a new joke to implement\
    \n#joke to have a random joke sent to the channel")

@bot.command()
async def joke():
    """Gets a random Joke"""
    jokeToSplit = getJoke()
    await splitJoke(jokeToSplit)

bot.run(token)
#https://discordapp.com/api/oauth2/authorize?client_id=382991605071740928&scope=bot&permissions=0
