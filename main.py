from pymino import Client
from pymino import Bot
from pymino.ext import *

bot = Bot(command_prefix="!", community_id="182533906", device_key="E7309ECC0953C6FA60005B2765F99DBBC965C8E9", signature_key="DFA5ED192DDA6E88A12FE12130DC6206B1251E44",
                service_key="6ac4661d-2e0f-4dd4-916e-0012ad1ae12a")

@bot.on_ready()
def ready():
    print("Activo")

@bot.command("help")
def help(ctx: Context, message: str):
    print("hola")


bot.run(email = "erikaone777@gmail.com", password = "Mimi777")
