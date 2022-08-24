import discord
import random
import requests
import os
import praw
from discord import message 
from discord.utils import get
from discord.ext import commands
import nacl
import time 

import keep_alive

intents = discord.Intents.all()
client = commands.Bot(command_prefix = '.' )

#slash = SlashCommand(client, sync_commands=True)

#guilds_ids=[759819332640309288 , 875296632311255080]


keep_alive.keep_alive()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('with your mom'))
    print ( " Bot is Ready" )

async def on_message(ctx):
    if ctx.content.startswith("Hello"):
        await ctx.reply('Hey, How is it going kid :)')

async def on_message(ctx):
    if ctx.content.startswith("gm"):
        await ctx.send('Hello Guys Wasssssup /n https://streamable.com/7mmqqe')


#@slash.slash(name="test", description="This is just a test command, nothing more." ,guild_ids=759819332640309288)
#async def test(ctx):
    #await ctx.send(content="Hello World!")

@client.command(aliases=['latency'])
async def ping(ctx):
    await ctx.send(f'Latency = ||{client.latency}ms||')

@client.command()
async def wksh(ctx):
    channel = ctx.author.voice.channel
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('wksh.mp3'), after=lambda e: print('done', e))   
    time.sleep(10)
    await ctx.voice_client.disconnect()

@client.command()
async def ohno(ctx):
    channel = ctx.author.voice.channel
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('oh-no.mp3'), after=lambda e: print('done', e))   
    time.sleep(10)
    await ctx.voice_client.disconnect()

@client.command()
async def subah(ctx):
    channel = ctx.author.voice.channel
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('subah.mp3'), after=lambda e: print('done', e))   
    time.sleep(36)
    await ctx.voice_client.disconnect()

@client.command()
async def bhhb(ctx):
    channel = ctx.author.voice.channel
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('bhhb.mp3'), after=lambda e: print('done', e))   
    time.sleep(4)
    await ctx.voice_client.disconnect()

@client.command()
async def thug(ctx):
    channel = ctx.author.voice.channel
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('thug-life.mp3'), after=lambda e: print('done', e))   
    time.sleep(15)
    await ctx.voice_client.disconnect()

@client.command()
async def sad(ctx):
    channel = ctx.author.voice.channel
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('sad.mp3'), after=lambda e: print('done', e))   
    time.sleep(5)
    await ctx.voice_client.disconnect()


@client.command()
async def fbi(ctx):
    channel = ctx.author.voice.channel
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('fbi.mp3'), after=lambda e: print('done', e))   
    time.sleep(3)
    await ctx.voice_client.disconnect()

@client.command()
async def nikal(ctx):
    channel = ctx.author.voice.channel
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('nikal.mp3'), after=lambda e: print('done', e))   
    time.sleep(3)
    await ctx.voice_client.disconnect()

@client.command()
async def sus(ctx):
    channel = ctx.author.voice.channel
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('amongus-music.mp3'), after=lambda e: print('done', e))   
    time.sleep(8)
    await ctx.voice_client.disconnect()

@client.command()
async def enter(ctx):
    channel = ctx.author.voice.channel
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('enter.mp3'), after=lambda e: print('done', e))   
    time.sleep(3)
    await ctx.voice_client.disconnect()

@client.command()
async def knife(ctx):
    channel = ctx.author.voice.channel
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('knife.mp3'), after=lambda e: print('done', e))   
    time.sleep(3)
    await ctx.voice_client.disconnect()

@client.command()
async def join(ctx): 
    await ctx.author.voice.channel.connect()

@client.command(aliases=['MEME'])
async def meme(ctx):

    reddit = praw.Reddit(client_id='VacGPQVfCaj6AjRoibAdXg',
                        client_secret='HY_y0tvRtgNiQRdVEpz2uOf-Ek_GiQ',
                        user_agent='android:com.example.myredditapp:v1.2.3 (by /u/MAINHU69)')
    
    
    submission = reddit.subreddit("IndianDankMemes").random()

    em = discord.Embed(title=f'r/{submission.subreddit}', description=f'{submission.title} -- u/{submission.author}', color=0xf1c40f)
    em.set_thumbnail(url=submission.url)
    em.set_image(url=submission.url)
    em.set_footer(text=f'⬆️ - {submission.score}')
    

    await ctx.send(embed=em)

@client.command(aliases=['MEMES'])
async def memes(ctx):

    reddit = praw.Reddit(client_id='VacGPQVfCaj6AjRoibAdXg',
                        client_secret='HY_y0tvRtgNiQRdVEpz2uOf-Ek_GiQ',
                        user_agent='android:com.example.myredditapp:v1.2.3 (by /u/MAINHU69)')

    submission = reddit.subreddit("SaimanSays").random()

    e = discord.Embed(title=f'r/{submission.subreddit}', description=f'{submission.title} -- u/{submission.author}', color=0xf1c40f)
    e.set_thumbnail(url=submission.url)
    e.set_image(url=submission.url)
    e.set_footer(text= f'⬆️ {submission.score}')
  
    await ctx.send(embed=e)

@client.command()
async def question(ctx,*, question):

    
    responses = [627054728668250162 , 626047160911134731 , 873260923501051935 , 622346986150035466 , 731025464813944874 , 761814966483025931 , 624871652844503044 , 482590841073041409 , 852844117859369001 , 473441321542090762 , 557065282745663488 , 895659167304523857 , 902609377008160879 , 874582092669923328 , 936690674139545621]

    await ctx.send(f'**Question** : {question}\n **Answer** : <@!{random.choice(responses)}>')

@client.command()
async def will(ctx,*, question):
    
    responses = ['Yes' , 'No' ]
    await ctx.send(f'**Question** : Will {question}\n **Answer** : {random.choice(responses)}')

@client.command(aliases=['fect'])
async def fact(ctx):
    poss = ['not get a gf', 'die single', 'have a night with a boy', 'be never denk again' , 'get cheated by her' , 'always be a mamas boy', 'never reach silver', 'reach radiant' , 'leave the boat' , 'make naysayer active' , 'be last son of naysayers' , 'forget chaddi baddis for grills', 'leave grills for chaddi baddis']

    responses = [627054728668250162 , 626047160911134731 , 873260923501051935 , 622346986150035466 , 731025464813944874 , 761814966483025931 , 624871652844503044 , 482590841073041409 , 852844117859369001 , 473441321542090762 , 557065282745663488 , 895659167304523857 , 902609377008160879 , 874582092669923328 , 936690674139545621]



    await ctx.send(f'Fact of the day : <@!{random.choice(responses)}> will {random.choice(poss)}')
    
@client.command()
async def pp(ctx):
 
    responses = ['8=============D' , '8============D' , '8===========D' , '8==========D' , '8=========D' , '8========D' , '8=======D' , '8======D' , '8=====D' , '8====D' , '8===D' , '8==D' ,'8=D' , '8D']
    await ctx.reply(f'Your PP Size {random.choice(responses)}')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx, member : discord.Member ,*, reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member ,*, reason=None):
    await member.ban(reason=reason)

@client.command()
async def unban(ctx,*, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:

        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name , member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{banned_users}')
            await ctx.send(f'Unbanned {user.mention}')
            return
        
client.run('ODc2ODEzNDUyMTA1MTEzNjQw.YRpiKQ.rYRO3uAYmE43Pv_7W2GcdHBOeVc')


