#current link https://discord.com/api/oauth2/authorize?client_id=981768485493415986&permissions=8&scope=bot%20applications.commands

from email.policy import default
from dotenv import load_dotenv
from hikari import Intents, guilds

import lightbulb
import hikari
import random
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

#8 ball messages
eightBallMessages = [
    #Negative messages
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",

    #Positive messages
    "As I see, yes",
    "Most likely",
    "Outlook good",
    "Signs point to yes",
    "Yes",

    #Certain messages
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes - definitely",
    "You may rely on it",

    #Uncertain messages
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again"
]

#Coin
coin = ["heads", "tails"]

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

#8ball
@bot.command
@lightbulb.option("question", "the question that will soon be answered")
@lightbulb.command("8ball", "Will use psychic powers to answer your question")
@lightbulb.implements(lightbulb.SlashCommand)
async def eightBall(ctx):
    await ctx.respond(f"Question: {ctx.options.question}\nThe 8ball says...{random.choice(eightBallMessages)}")

#Coinflip
@bot.command
@lightbulb.command("coin", "coinflip")
@lightbulb.implements(lightbulb.SlashCommand)
async def coinFlip(ctx):
    await ctx.respond(random.choice(coin))

#Voodoo
#"When you are ready to challenge the keeper of the underworld, you will have to make a living sacrifice. Everything you need for it can be found in the underworld."
@bot.command
@lightbulb.command("voodoo", "description was too long")
@lightbulb.implements(lightbulb.SlashCommand)
async def vooDoo(ctx):
    #get the bots nickname. Get the numbers in the bots nickname.
    #store them and add 1 to the number
    #change the nickname with bot.rest.edit_my_user(username="new kewl username")

    botUser = ctx.get_guild().get_my_member()
    botNick = botUser.display_name
    



bot.run()
