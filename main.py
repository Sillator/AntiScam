from discord.ext import commands
from AntiScam import AntiScam

whitelist = [636187868414476288, 602874796790906890]
logs_channel = None # Here you can add the ID of the channel where the logs will be sent.

bot = commands.Bot(command_prefix='>')
bot.remove_command('help') # Remove this line if you want to use the help command.

@bot.listen()
async def on_message(message):
    await AntiScam(message, bot = bot, whitelist = whitelist, muted_role='Muted', verified_role='Verified', logs_channel=921478772664959088

bot.run('OTIxNDgxNjMwMDUxMzQwMzQ5.YbzipA.ChoWX-6_W4Ra5LjS5Xuj2uy55n8')
