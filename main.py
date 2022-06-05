import discord, json, asyncio, random
from discord.ext import commands, tasks

with open('config.json') as config_file:
    data = json.load(config_file)

intents = discord.Intents(messages=True)

AccountToken = data['AccountToken']
Messages = data['Messages']
ChannelID = data['ChannelID']
MessagesPerMin = data['MessagesPerMin']

client = commands.Bot(command_prefix='balls', intents=intents)

@client.event
async def on_ready():
    print(fr'''
.____                      .__    ___________
|    |    _______  __ ____ |  |   \_   _____/____ _______  _____
|    |  _/ __ \  \/ // __ \|  |    |    __) \__  \\_  __ \/     \
|    |__\  ___/\   /\  ___/|  |__  |     \   / __ \|  | \/  Y Y  \
|_______ \___  >\_/  \___  >____/  \___  /  (____  /__|  |__|_|  /
        \/   \/          \/            \/        \/            \/

Logged into {client.user}

Creator's Website -- iliyaa.tk

Farming..
    ''')
    level.start()

@tasks.loop(minutes=(int(MessagesPerMin)))
async def level():
    channel = client.get_channel(int(ChannelID))
    async with channel.typing():
        await asyncio.sleep(2.5)

    await channel.send(random.choice(Messages))


client.run(AccountToken, bot=False)
