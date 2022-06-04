import random
import hikari
import lightbulb

eightBall_plugin = lightbulb.Plugin("8ball")

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

@eightBall_plugin.command
@lightbulb.option("question", "the question that will soon be answered")
@lightbulb.command("8ball", "Will use psychic powers to answer your question")
@lightbulb.implements(lightbulb.SlashCommand)
async def eightBall(ctx):
    await ctx.respond(f"Question: {ctx.options.question}\nThe 8ball says...{random.choice(eightBallMessages)}")

def load(bot: lightbulb.BotApp):
    bot.add_plugin(eightBall_plugin)