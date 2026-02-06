import discord
from discord.ext import commands

# إعداد الصلاحيات
intents = discord.Intents.default()
intents.message_content = True

# تحديد علامة الأمر (مثلاً !)
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'تم تسجيل الدخول باسم: {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send('أهلاً بك! أنا بوت سيرفرك الجديد.')

# ضع التوكن الخاص بك هنا بدلاً من كلمة YOUR_TOKEN_HERE

bot.run('MTQ2OTI5NDc5NzcwNDUyODA0NQ.GoMYPL.1U1UtQWbVpNnh94tUv8g3LfO2_cytmyX1T4pt8')
