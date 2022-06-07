from dotenv import load_dotenv

import hikari
import lightbulb
import os
import requests

load_dotenv()

wolf_api = os.environ['WOLF_API']
oracle_plugin = lightbulb.Plugin("Oracle")

@oracle_plugin.command
@lightbulb.option("question", "What will you ask?")
@lightbulb.command("oracle", "Will answer any question.")
@lightbulb.implements(lightbulb.SlashCommand)
async def oracle(ctx):
    question = ctx.options.question or ctx.question
    url = f"http://api.wolframalpha.com/v1/simple?appid={wolf_api}&i={question}%3F"
    response = requests.get(url)

    if response.status_code == 501:
        await ctx.respond("Unable to process that")
        return
    
    await ctx.respond(response.text)

def load(bot: lightbulb.BotApp):
    bot.add_plugin(oracle_plugin)