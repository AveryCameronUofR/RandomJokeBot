import discord
from discord.ext import commands
import random
from random import randint
question = ' '
answer = ' '

'''These arrays hold the index of jokes used recently'''
recentCS = []
recentBar = []
recentKnock= []

'''this is for the token of the discord bot'''
token = 'PLace token here'

client = discord.Client()

bot = commands.Bot(command_prefix='#', description='A bot that randomly posts a joke to a discord channel')
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)

'''
***Splits the joke into Question and Answer, based on input of full joke in string
***This is done by the arbitrary flag Answer123
***it will check if it is a knock knock joke and send extra aspects accordinly
'''
async def splitJoke(fullJoke):
    splitVersion = fullJoke.split('Answer123')
    question = splitVersion[0]
    answer = splitVersion[1]
    #Checks for KnockKnock keyword indicating knock knock joke
    if 'KnockKnock' not in fullJoke:
        await bot.say(question)
        await bot.say(answer)
    else:
        questionk = question.split('KnockKnock')
        #splits the joke with knockknock and then splits it again byt answer 
        question = questionk[1]
        await bot.say('Knock Knock')
        await bot.say('Who\'s there?')
        await bot.say(question)
        await bot.say(question + ' who?')
        await bot.say(answer)

'''
***Retrieves a random joke based on command choice
***ensures the joke is not in the appropriate recent array
***this array holds an arbitrary value, less than or equal to max
***this means the joke will not repeat for at least that many calls or a reset
***opens individual file based on call
***loops through to get the joke on the line
'''
def getJoke(choice):
    #base number of jokes in each file (could be in the if statements)
    num = random.randint(1,20)
    #Checks the choice sent to the function
    if choice == 1:
        #checks to see if the number is in the recent array
        if num not in recentCS:
            recentCS.append(num)
        else:
            #if length of array is 15 it removes an entry
            if len(recentCS) == 15:
                recentCS.pop(0)
            #loops through and generates number until it is not in the recent array
            while (num in recentCS):
                num = random.randint(1,20)
            #adds the new number to the recent index
            recentCS.append(num)
        #assigns the jokesCS text file to general variable jokes
        jokes = open("jokesCS.txt")
    elif choice == 2:
        if num not in recentKnock:
            recentKnock.append(num)
        else:
            if len(recentKnock) == 15:
                recentKnock.pop(0)
            while (num in recentKnock):
                num = random.randint(1,20)
            recentKnock.append(num)
        jokes = open("jokesKnock.txt")
    elif choice == 3:
        num = random.randint(1,10)
        if num not in recentBar:
            recentBar.append(num)
        else:
            if len(recentBar) == 10:
                recentBar.pop(0)
            while (num in recentBar):
                num = random.randint(1,10)
                recentBar.append(num)
        jokes = open("jokesBar.txt")
        print(num)
    counter = 0
    while counter < num:
        fullJoke = jokes.readline()
        counter = counter+1
    return fullJoke


'''
*** gives basic list of commands
'''
@bot.command()
async def info():
    await bot.say("Welcome to the Joke Bot" "\nThis Bot is used for Random Jokes\
    \n\nSome simple commands are:\
    \n#joke to have a random joke sent to the channel\
    \n#jokeCS to have a random Computer Science joke sent to the channel\
    \n#jokeKnock to have a random KnockKnock joke sent to the channel\
    \n#JokeBar to have a random Bar joke sent to the channel")

'''
***All general commands and can easily be added or removed
***sends a number based on command to getJoke call
'''
@bot.command()
async def joke():
    #picks a random category if not stated in the command
    category = random.randint(1,3)
    #gets the joke based on the category
    jokeToSplit = getJoke(category)
    #splits the joke for message to chat
    await splitJoke(jokeToSplit)

@bot.command()
async def jokeCS():
    jokeToSplit = getJoke(1)
    await splitJoke(jokeToSplit)

@bot.command()
async def jokeKnock():
    jokeToSplit = getJoke(2)
    await splitJoke(jokeToSplit)

@bot.command()
async def jokeBar():
    jokeToSplit = getJoke(3)
    await splitJoke(jokeToSplit)

bot.run(token)
