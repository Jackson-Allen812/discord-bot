import discord
import WebScraper as Web
import Toolbox as Lib
from discord.ext import commands

# bot token left out for security purposes
TOKEN = "XXXXXXXXXX"

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
            embedvar = discord.Embed(title=poke.capitalize(), 
                                     description=Web.turn_to_string(Web.grab_poke(poke)), 
                                     color=Web.get_color(Web.grab_poke(poke)[0]))

            embedvar.set_image(url=Web.get_poke_image(poke))

            embedvar.set_footer(text=Web.get_poke_dex_entry(poke))

            await ctx.send(embed=embedvar)

        except TypeError:
            await ctx.send("Sorry, that isn't a Pokemon. Check your spelling and try again.")
        except (IndexError, ValueError):
            await ctx.send("Something seems to have gone wrong. Did you not enter a Pokemon name?")


@bot.command(pass_context=True)
async def give(ctx, account, amount):

    author = bot.get_user(ctx.message.author.id).name
    

    try:
        if isinstance(ctx.channel, discord.channel.DMChannel):
            print(author + " tried to use the give command in a DM.")
            await ctx.send("Sorry, I only give Money on servers!")
            return

        amount = int(amount)
        formatted_id = Lib.format_id(account)

        if amount < 0:
            raise ValueError

        if int(formatted_id) == ctx.message.author.id:
            print(author + " tried to give themselves Money.")
            await ctx.send("You cannot give yourself Money.")
            return
        if int(amount) > 100:
            print(author + " used the give command to give " +
                bot.get_user(int(formatted_id)).name + " " + amount + " Money")
            await ctx.send("Please only give 100 Money at max.")
            return

        Lib.write_to_file(formatted_id, amount)

        await ctx.send("Congrats " + account + ", you've been given " + str(amount) + " Money!")
    except:
        await ctx.send("Something appears to have gone wrong, please try again.")
        print(author + " tried to use the give command, but an error occured.")


@bot.command(pass_context=True)
async def balance(ctx):

    author = bot.get_user(ctx.message.author.id).name

    if isinstance(ctx.channel, discord.channel.DMChannel):
        print(author + " tried to use the balance command in a DM.")
        await ctx.send("Sorry, I can only check your balance on servers!")
        return

    print(author + " used the balance command in the " +
          bot.get_channel(ctx.channel.id).name + " channel.")

    amount = Lib.account_balance(Lib.format_id(ctx.message.author.id))
    
    if amount is None:
        await ctx.send("You don't have an account yet, wait for someone to give you Money")
    else:
        await ctx.send("You have " + str(amount) + " Money!")


@bot.event
async def on_ready():
	print("Logged in as: " + bot.user.name)
	print("User ID: " + str(bot.user.id))
	print("----------------------------")


def run_bot():
	bot.run(TOKEN, bot=True)


run_bot()
