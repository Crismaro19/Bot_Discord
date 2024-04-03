# Import the required modules
import discord
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Create a Discord client instance
intents = discord.Intents.all()
client = discord.Client(intents=intents)

# Set the confirmation message when the bot is ready
@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

# Define an event for when a message is received
@client.event
async def on_message(message):
    # Ignore messages from the bot itself to avoid infinite loops
    if message.author == client.user:
        return

    if message.content.lower() == 'hola':

        response = '¡Hola! ¿Cómo estás?'
        await message.channel.send(response)

    if message.content.lower() == 'puedo entrar?':

        response = 'Claro solo tienes que rezarle al poderoso Oram, rezo: oram sama dejame entrar'
        await message.channel.send(response)

    if message.content.lower() == 'oram sama dejame entrar':
        
        channel = discord.utils.get(client.get_all_channels(), name="Arriba")
  
        await message.author.move_to(channel)

# Run the bot with the token retrieved from the .env file
client.run(os.getenv('TOKEN'))
