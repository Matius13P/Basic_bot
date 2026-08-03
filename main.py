import re
import random
import discord
from bot_logic import gen_pass


# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content.strip()
    cmd = content.lower()

    if cmd.startswith('$hello'):
        await message.channel.send("Hi!")
    elif cmd.startswith('$bye'):
        await message.channel.send("Good bye!🙂")
    elif cmd.startswith('$info'):
        await message.channel.send(
            "Hola, soy Kodly! Soy un bot de Discord creado como un proyecto en Kodland. "
            "Puedo generar contraseñas con 'gen_pass(x)', responder mensajes de saludo '$hello' y '$bye', "
            "generar números aleatorios con '$nro' y darte información con '$info'."
        )
    elif cmd.startswith('$nro'):
        await message.channel.send(str(random.randint(1, 10)))
    elif cmd.startswith('gen_pass'):
        if re.fullmatch(r'gen_pass\s*\(\s*(\d+)\s*\)', content):
            length = int(re.match(r'gen_pass\s*\(\s*(\d+)\s*\)', content).group(1))
            await message.channel.send(f"Contraseña generada: {gen_pass(length)}")
        else:
            await message.channel.send("Usa: gen_pass(10)")
    else:
        await message.channel.send(content)

client.run("TOKEN")
