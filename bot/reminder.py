import discord
import asyncio
from discord.ext import commands
from bot import utils
from datetime import datetime

async def przypomnij(bot, channelID, meeting):
    channel = bot.get_channel(channelID)
    try:
        time = datetime.strptime(meeting.hour, '%H:%M')   
        date = datetime.strptime(meeting.date, '%d-%m-%Y')
    except Exception as e:
        print(e)
        await channel.send("> ERROR: Błąd daty lub godziny")
        return

    remind = date.replace(hour=time.hour, minute=time.minute)
    # - datetime.timedelta(days=1)
    # to remind in the day before
    print(remind)

    if(remind < utils.return_date()):
        await channel.send("> ERROR: Zła data, ustaw datę w przód")
        return

    await channel.send(f"> Przypomnienie o spotkaniu ustawione na termin: **{remind}**")
    odliczanie = remind - utils.return_date()
    print(odliczanie)

    await asyncio.sleep(odliczanie.total_seconds())
    await channel.send(f"### SPOTKANIE \n Jutro ({date}) o godzinie {time}!")

class CurrentDate:
    def __init__(self):
        self.hour = '17:00'
        self.date = '01-01-2025'

    def change_hour(self,hour):
        self.hour = hour
    
    def change_date(self, date):
        self.date = date

    def return_hour(self):
        return self.hour

def reminder(token, channelID):
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='!', intents=intents)
    meeting = CurrentDate()

    @bot.event
    async def on_ready():
        print(f'{bot.user.name} is working')     

    @bot.command()
    async def czas(ctx, time=None):
        if time is None:
            await ctx.send(f"> Aktualnie ustawiona godzina to **{meeting.hour}**")
        else:
            if utils.check_hour(time):
                meeting.change_hour(time)
                print(time)
                await ctx.send(f"> Godzina ustawiona na **{meeting.hour}**")
            else:
                print('Zły format')
                await ctx.send("> ERROR: Godzina musi być napisana w formacie HH-MM np. 17:30")
        
    @bot.command()
    async def spotkanie(ctx, date, hour=None):
        if date:
            if utils.check_date(date):
                if hour != None:
                    meeting.change_hour(hour)
                meeting.change_date(date)
                await przypomnij(bot, channelID, meeting)    
            else:
                await ctx.send("> ERROR: Data musi być napisana w formacie DD-MM-YYYY np. 01-03-2024")

    bot.run(token)
            


