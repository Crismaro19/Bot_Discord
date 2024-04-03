# Importaciones
import discord
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Create a Discord client instance
intents = discord.Intents.all()
client = discord.Client(intents=intents)

# Diccionarios de datos
comandos_validos = {
    "iron": "ironcito ",
    "nati": "naticita",
    "maro": "Dios creador y destructor de universos",
    "oram": "a sus ordenes mi sr",
}


# Confirmacion de activacion del bot
@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

# Tomar los mensajes en el chat y validarlos
@client.event
async def on_message(message):

    # Validar que el mensaje no sea del bot (Para no generar bucles)
    if message.author == client.user:
        return

    # Responder "Holas"
    if message.content.lower() == 'hola':

        response = '¡Hola! ¿Cómo estás?'
        await message.channel.send(response)

    # Dar
    if message.content.lower() == 'puedo entrar?':

        response = 'Claro solo tienes que rezarle al poderoso Oram, rezo: oram sama dejame entrar'
        await message.channel.send(response)

    if message.content.lower() in comandos_validos:
        response = comandos_validos[message.content.lower()]
        await message.channel.send(response)

    if message.content.lower() == 'oram sama dejame entrar':

        if message.author.voice is None or message.author.voice.channel is None:
            await message.channel.send("Por favor, únete a un canal de voz primero.")
            return
        
        channel = discord.utils.get(client.get_all_channels(), name="Arriba")

        await message.author.move_to(channel)

# Run the bot with the token retrieved from the .env file
client.run(os.getenv('TOKEN'))
