from email.policy import default
import lightbulb
import hikari
import random

#Creating the bot
bot = lightbulb.BotApp(
    token="OTgxNzY4NDg1NDkzNDE1OTg2.GBBNaa.B1RrkXptmLK8bCvYUG4K1ungw9pr8OYFfdCuaw",
    default_enabled_guilds=(331608355913203713)
)

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



#If a message has been sent into the server
@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    #Prints message from discord to the terminal
    print(event.content)

@bot.command
@lightbulb.command("ping", "Says pong back") #command, description
@lightbulb.implements(lightbulb.SlashCommand) #uses slash command
async def pingPong(ctx): #every function requires a context variable
    await ctx.respond('pong') #replies with pong

@bot.command
@lightbulb.option("question", "the question that will soon be answered")
@lightbulb.command("8ball", "Will send a random 8 ball message")
@lightbulb.implements(lightbulb.SlashCommand)
async def eightBall(ctx):
    await ctx.respond(random.choice(eightBallMessages))




bot.run()
