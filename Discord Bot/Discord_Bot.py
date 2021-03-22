import discord
import WebScraper as Web
import Toolbox as Lib
from discord.ext import commands

# bot token left out for security purposes
TOKEN = "XXXXXXXXXXX"

client = discord.Client()
bot = commands.Bot(command_prefix="!")


@bot.command(name="checktype", pass_context=True)
async def check_type(ctx, poke):
    try:
        poke = int(poke)
        await ctx.send("Please enter a Pokemon's name, not their PokeDex ID.")
    except ValueError:
        try:
            print(bot.get_user(ctx.message.author.id).name + " used the checktype command to look up " + poke.capitalize())
            embedvar = discord.Embed(title=poke.capitalize(), description=Web.turn_to_string(Web.grab_poke(poke)),
                                     color=Web.get_color(Web.grab_poke(poke)[0]))
            embedvar.set_image(url=Web.get_poke_image(poke))
            embedvar.set_footer(text=Web.get_poke_dex_entry(poke))
            # embedvar.add_field(name="Resisted By:", value=Web.get_weak(Web.grab_poke(poke), "Weak"), inline=False)
            # embedvar.add_field(name="Strong Against:", value=Web.get_weak(Web.grab_poke(poke), "Strong"), inline=False)
            # embedvar.add_field(name="Resists:", value=Web.get_weak(Web.grab_poke(poke), "Resists"), inline=False)
            # embedvar.add_field(name="Immune:", value=Web.get_weak(Web.grab_poke(poke), "Immune"), inline=False)
            await ctx.send(embed=embedvar)
        except TypeError:
            await ctx.send("Sorry, that isn't a Pokemon. Check your spelling and try again.")
        except (IndexError, ValueError):
            await ctx.send("Something seems to have gone wrong. Did you not enter a Pokemon name?")



@bot.event
async def on_ready():
	print("Logged in as: " + bot.user.name)
	print("User ID: " + str(bot.user.id))
	print("----------------------------")


def run_bot():
	bot.run(TOKEN, bot=True)


run_bot()
