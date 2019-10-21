import asyncio
import logging
from datetime import datetime

from logging.handlers import RotatingFileHandler
import discord
from discord.ext import commands

#from games import Game
import config as props
import users

LOGGER = logging.getLogger('refbot_logger')
LOGGER.setLevel(logging.DEBUG)

FORMATTER = logging.Formatter('%(asctime)s: %(levelname)s: %(module)s: %(message)s')
ROTATING_FILE_HANDLER = RotatingFileHandler('Refbot.log', maxBytes=1024*1000, backupCount=10)
ROTATING_FILE_HANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(ROTATING_FILE_HANDLER)
LOGGER.info("Logger initialized and running.")

REFBOT = commands.Bot(command_prefix="!")

ACTIVE_PLAYERS = []


@REFBOT.command(pass_context=True)
async def aye(context, summoner_name=None):
    username = context.message.author.name
    #user = users.get(username)
    if username not in ACTIVE_PLAYERS:
        ACTIVE_PLAYERS.append(username)
        response = f"{username} has been added to the list of active players."
    else:
        response = "Wait. You're already in the game."

    await context.message.channel.send(response)


@REFBOT.command(pass_context=True)
async def bye(context, summoner_name=None):
    username = context.message.author.name
    #user = users.get(username)
    if username in ACTIVE_PLAYERS:
        ACTIVE_PLAYERS.remove(username)
        response = f"{username} has been removed from the list of active players."
    else:
        response = "Shut up, you're not even in this game."
    
    await context.message.channel.send(response)


@REFBOT.command(pass_context=True)
async def draft(context, game=1, draft_type='auto'):
    # validate the draft type
    draft_types = ['auto', 'manual', 'random']
    if draft_type not in draft_types:
        response = "I didn\'t recognize that draft type so I did what I wanted. Enjoy."
        draft_type = 'random'

    # find the game in the list of active games

    # call the correct draft method

    # generate the response
        
    await context.message.channel.send(response)


@REFBOT.command(pass_context=True)
async def hello(context):
    username = context.message.author.name
    user = users.get(username)
    recent_commands = user.recent_commands()
    previous_hellos = recent_commands.count('hello')

    if previous_hellos > 5:
        return
    elif previous_hellos == 5:
        msg = "..."
    elif previous_hellos == 4:
        msg = "Kid, if you are just going to keep saying it I am NOT responding to you anymore."
    elif previous_hellos == 3:
        msg = "Okay! Really, I\'m done with the hellos. You can stop now."
    elif previous_hellos == 2:
        msg = "\"Hello\" three times? That\'s uh... Weird."
    elif previous_hellos == 1:
        msg = "Hello to you again! Sorry, but I wasn\'t joking when I said that I don\'t have much to say."
    elif previous_hellos == 0:
        msg = f"Hi, {username}! I don\'t have much to say right now but we\'ll have more to talk about once I\'m back fulltime."

    user.log_command('hello')

    await context.message.channel.send(msg)


@REFBOT.command(pass_context=True)
async def open(context):
    # username = context.message.author.name
    # now = datetime.now()
    # Game(username, now)
    response = "@everyone Little League is happening! Aye in to get your spot."
    await context.message.channel.send(response)


@REFBOT.command(pass_context=True)
async def rollcall(context):
    response = "Game: \n"
    for i, player in enumerate(ACTIVE_PLAYERS):
        i += 1
        i = str(i) + '. '
        player = i + player
        response += '\n' + player
    await context.message.channel.send(response)


REFBOT.run(props.Discord.bot_token)
