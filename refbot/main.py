# Imports required for Discord
import asyncio
import logging
from logging.handlers import RotatingFileHandler
import discord
from discord.ext import commands
import properties as props
import users

LOGGER = logging.getLogger('refbot_logger')
LOGGER.setLevel(logging.DEBUG)

FORMATTER = logging.Formatter('%(asctime)s: %(levelname)s: %(module)s: %(message)s')
ROTATING_FILE_HANDLER = RotatingFileHandler('Refbot.log', maxBytes=1024*1000, backupCount=10)
ROTATING_FILE_HANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(ROTATING_FILE_HANDLER)
LOGGER.info("Logger initialized and running.")

REFBOT = commands.Bot(command_prefix="!")

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

REFBOT.run(props.Discord.bot_token)