from wxpy import *

bot = Bot(cache_path=True)
print(bot.friends(update=True))
print(bot.groups(update=True))
print(bot.mps(update=True))
print(bot.friends().stats_text())

# menjin = bot.mps(update=True).search('西单大悦城写字楼')[0]


@bot.register()
def print_msg(msg):
    print(msg)


# bot.join()
embed()
