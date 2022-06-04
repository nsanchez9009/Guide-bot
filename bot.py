#current link https://discord.com/api/oauth2/authorize?client_id=981768485493415986&permissions=8&scope=bot%20applications.commands

from email.policy import default
from dotenv import load_dotenv
from hikari import Intents, guilds

import lightbulb
import hikari
import os

load_dotenv()

bot_token = os.environ['BOT_TOKEN']

#Creating the bot
bot = lightbulb.BotApp(
    token=bot_token,
    intents=hikari.Intents.ALL,
    default_enabled_guilds=(331608355913203713, 831400778643406848),
)

bot.load_extensions_from("./extensions/", must_exist=True)

#--------------------------------------------------------------------------------------------------------------------

#If a message has been sent into the server
@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    #Prints message from discord to the terminal
    print(event.content)

#ping pong latency
@bot.command
@lightbulb.command("ping", "Says pong back and gives latency") #command, description
@lightbulb.implements(lightbulb.SlashCommand) #uses slash command
async def pingPong(ctx): #every function requires a context variable
    await ctx.respond(f"pong\nLatency: {bot.heartbeat_latency*1000:.2f}ms") #replies with pong

bot.run()
