import random
import hikari
import lightbulb

coinFlip_plugin = lightbulb.Plugin("Coin flip")

#Coin
coin = ["heads", "tails"]

@coinFlip_plugin.command
@lightbulb.command("coin", "Flip a coin")
@lightbulb.implements(lightbulb.SlashCommand)
async def coinFlip(ctx):
    await ctx.respond(random.choice(coin))

def load(bot: lightbulb.BotApp):
    bot.add_plugin(coinFlip_plugin)
