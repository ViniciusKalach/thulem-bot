import discord
from discord.ext import commands
import markovify
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Carregar corpus
def build_model():
    with open("messages.txt", encoding="utf-8") as f:
        text = f.read()
    return markovify.Text(text)

model = build_model()

@bot.event
async def on_ready():
    print(f"🧙‍♂️ Thúlëm está entre nós como {bot.user}")

@bot.command(name="visao")
async def visao(ctx):
    sentence = model.make_sentence(tries=100)
    if sentence:
        await ctx.send(f"✨ {sentence}")
    else:
        await ctx.send("Thúlëm está em silêncio...")

bot.run(TOKEN)
