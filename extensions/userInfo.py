from datetime import datetime

import hikari
import lightbulb

#create the plugin
info_plugin = lightbulb.Plugin("Info")

@info_plugin.command #create command for this plugin
@lightbulb.option("user", "Who do you want to know about.", hikari.User, required=False)#option for specifying the user
@lightbulb.command("info", "Get information on a server memeber.")#the command
@lightbulb.implements(lightbulb.SlashCommand)
async def info(ctx: lightbulb.Context) -> None:
    user = ctx.get_guild().get_member(ctx.options.user or ctx.user)#get the user

    if not user: #if user == NULL
        await ctx.respond("That user is not in this server.")
        return
    
    created_at = int(user.created_at.timestamp()) #account creation date int
    joined_at = int(user.joined_at.timestamp()) #account join server date int

    roles = (await user.fetch_roles())[1:] #gets all the roles except for @everyone ([1:])

    #Creating the embed
    embed = (
        hikari.Embed(
            title=f"User Info - {user.display_name}", #User's name
            description=f"ID: `{user.id}`", #User's id
            color=0x39FF12, #color of line on embed
            timestamp=datetime.now().astimezone() #timestamp for command call
        )
        .set_footer(
            text=f"Requested by {ctx.member.display_name}",
            icon=ctx.member.avatar_url or ctx.member.default_avatar_url
        )
        .set_thumbnail(user.avatar_url or user.default_avatar_url)
        .add_field(
            "Bot?",
            str(user.is_bot),
            inline=True
        )
        .add_field(
            "Created account on",
            f"<t:{created_at}:d>\n(<t:{created_at}:R>",
            inline=True
        )
        .add_field(
            "Joined server on",
            f"<t:{joined_at}:d>\n(<t:{joined_at}:R>",
            inline=True,
        )
        .add_field(
            "Roles",
            ", ".join(r.mention for r in roles),
            inline=False
        )
    )

    await ctx.respond(embed)

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(info_plugin)
