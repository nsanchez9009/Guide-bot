from curses.ascii import isdigit
import hikari
import lightbulb

vooDoo_plugin = lightbulb.Plugin("Voodoo")

#Voodoo
#"When you are ready to challenge the keeper of the underworld, you will have to make a living sacrifice. Everything you need for it can be found in the underworld."
@vooDoo_plugin.command
@lightbulb.command("voodoo", "description was too long")
@lightbulb.implements(lightbulb.SlashCommand)
async def vooDoo(ctx):
    botUser = ctx.get_guild().get_my_member()
    guild = ctx.get_guild()
    bot = ctx.bot
    wof = hikari.File('./media/wof.gif')

    res = [str(i) for i in botUser.display_name.split() if i.isdigit()]

    if len(res) == 0:
        await bot.rest.edit_my_member(guild, nickname = f"Guide 1")
    
    elif res == 1:
        await bot.rest.edit_my_member(guild, nickname = f"Guide 2")
    else:
        res = int("".join(res)) + 1
        await bot.rest.edit_my_member(guild, nickname = f"Guide {res}")

    await ctx.respond(f"The guide has been slain...\nGuide {res} has arrived.")
    await ctx.respond(wof)



def load (bot: lightbulb.BotApp):
    bot.add_plugin(vooDoo_plugin)