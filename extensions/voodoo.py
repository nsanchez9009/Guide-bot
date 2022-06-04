import hikari
import lightbulb

vooDoo_plugin = lightbulb.Plugin("Voodoo")

#Voodoo
#"When you are ready to challenge the keeper of the underworld, you will have to make a living sacrifice. Everything you need for it can be found in the underworld."
@vooDoo_plugin.command
@lightbulb.command("voodoo", "description was too long")
@lightbulb.implements(lightbulb.SlashCommand)
async def vooDoo(ctx):
    #get the bots nickname. Get the numbers in the bots nickname.
    #store them and add 1 to the number
    #change the nickname with bot.rest.edit_my_user(username="new kewl username")

    botUser = ctx.get_guild().get_my_member()
    botNick = botUser.display_name


def load (bot: lightbulb.BotApp):
    bot.add_plugin(vooDoo_plugin)