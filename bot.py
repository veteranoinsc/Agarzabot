import discord
from discord import TextChannel
from discord.ext import commands, tasks
from discord.utils import get
from itertools import cycle
import random
from random import choice
from discord.ext.commands import CommandNotFound, Bot, has_permissions , MissingPermissions, MissingRequiredArgument
import asyncio
import os
import json
import time
import string
import re
import sys
import inspect
from collections import Counter
from datetime import datetime  

client = commands.Bot(command_prefix='a.')
status = cycle(['Do a.help for info ', 'Use a.bugreport to report bugs! ', 'Use a.suggest to suggest ideas!', 'V.0.6 | Updates coming'])
gif = ('https://media.giphy.com/media/xTiN0L7EW5trfOvEk0/giphy.gif')
client.remove_command('help')

#fun-commands

@client.command()
async def password(ctx, length = 12):
  letters = string.ascii_lowercase + string.ascii_uppercase + string.digits 
  Password = (random.choice(letters) for i in range(length))
  author = ctx.message.author.name
  icon = ctx.message.author.avatar_url
  embed = discord.Embed(color=0x00ffff)
  embed.set_author(name=author, icon_url=icon)
  embed.add_field(name='<:tick:651543094336159787>  x   Password!', value="``` I sent a random password to ur dm!```", inline=False)
  embed.set_footer(text='Developed by PoundsCoin#9999')
  await ctx.send(embed=embed)
  await ctx.author.send(f"".join(Password))

@client.command()
async def say(ctx, *,words):
    embed = discord.Embed(color=0x00ffff)
    embed.add_field(name='Message:', value=f"{words}", inline=False)
    embed.set_footer(text='Developed by PoundsCoin#9999')
    await ctx.send(embed=embed)
    await ctx.message.delete()
@say.error
async def say_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("<:error:657997451042750485> x  Please specify a message to say")  
@client.command()
async def dm(ctx, member : discord.Member, *, message):
    author = ctx.message.author.name
    icon = ctx.message.author.avatar_url
    embed = discord.Embed(color=0x00ffff)
    embed.set_author(name=author, icon_url=icon)
    embed.add_field(name='<:tick:651543094336159787>  x   Message sent!', value="Take me 2s!", inline=False)
    embed.set_footer(text='Developed by PoundsCoin#9999')
    await ctx.send(embed=embed)
    await member.send(message)
    await ctx.message.delete()
@dm.error
async def dm_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send(" <:error:657997451042750485> x  Please specify a user to dm")  
@client.command()
async def cookie(ctx, member: discord.User=None):
     embed5 = discord.Embed(
         title=f"{member.name}'s get a :cookie:"
     )
     embed5.set_author(name=f"{member.name}#{member.discriminator}", icon_url=member.avatar_url)
     embed5.set_image(url="https://media1.giphy.com/media/xUA7aPf8kouyzgbOXC/giphy.gif?cid=ecf05e471b9dc87cc16f1112cee411c49c06ffc5311a7ab1&rid=giphy.gif")
     await ctx.send(embed=embed5)
@client.command()
async def gay(ctx, *, gaything):
    embed = discord.Embed(
        colour=discord.Colour.blue(),
        title='Gay percent!')

    embed.set_footer(text=f'Request by {ctx.author} | Online   ' ,icon_url=ctx.author.avatar_url)
    embed.add_field(name='<:error:657997451042750485> x  Gay', value=f">>> **{gaything}** is **{random.randint(1,101)}%** gay",inline=False)

    await ctx.send(embed=embed)
@gay.error
async def gay_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send(" <:error:657997451042750485> x Specify a user")

@client.command(name='8ball')
async def _ball(ctx, *, question):
    responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'That is a definite yes!',
        'Maybe',
        'There is a good chance',
        'Im lazy to answer : )',
        'The time will say it'
        'Ask me better late mate']
    answer = random.choice(responses)
    await ctx.send(f"{answer}")
@_ball.error
async def _ball_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("<:error:657997451042750485> x  Please specify the question.")
@client.command()
async def esay(ctx, title, *, body):
  embed = discord.Embed(
    colour=discord.Colour.blue(),
        title=f' {title }')
  
  embed.add_field(name=f'x', value=f'{body}' ,inline=False)
  await ctx.send(embed=embed)
@esay.error
async def esay_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("<:error:657997451042750485>  x  `Example:` a.esay **title - body** ")
#info-commands


@client.command()
async def userinfo(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    embed = discord.Embed(

        colour=member.colour,
        timestamp=ctx.message.created_at

    )

    roles = [role for role in member.roles]
    statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]

    embed.set_author(name=f"User Info  x  ▶  {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested By {ctx.author}", icon_url=ctx.author.avatar_url)

    embed.add_field(name=">>> :closed_lock_with_key: x  User Name", value=member.name, inline=False)
    embed.add_field(name=">>> :shield: x ID", value=member.id, inline=False)
    embed.add_field(name=">>> :alarm_clock: x  Account Created", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
    embed.add_field(name=">>> :clock: x  Member Joined", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
    embed.add_field(name=f">>> :gun: x  Roles ({len(roles)})", value=" ".join([role.mention for role in roles]), inline=False)
    embed.add_field(name=">>> :airplane: x  Top Role", value=member.top_role.mention, inline=False)
    embed.add_field(name=">>> <:bot:634854279294877706> x  Bot", value=member.bot, inline=False)
    embed.add_field(name='>>> :mag_right: x  Status:', value=member.status , inline=False)
    await ctx.send(embed=embed)

@client.command(name='botservers')
async def server_count(ctx):
    embed = discord.Embed(
    colour=discord.Colour.blue(),
        title='[ Information ]')

    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    embed.set_footer(text=f'Request by {ctx.author} | Online   ' ,icon_url=ctx.author.avatar_url)
    embed.add_field(name=':flushed: x  Servers', value= f'```{(len(client.guilds))}```',inline=False)

    await ctx.send(embed=embed)

@client.command(name='botinfo')
async def infobot(ctx):
    embed = discord.Embed(
    colour=discord.Colour.blue(),
        title='[ Bot information ]')

    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    embed.set_footer(text=f'Request by {ctx.author} | Online   ' ,icon_url=ctx.author.avatar_url)
    embed.add_field(name=':crown:  x  Owner', value=f'>>> PoundsCoin#9999',inline=True)
    embed.add_field(name='<:bot:634854279294877706> x  Name', value= f'>>> AgarzaBot#8543',inline=True)
    embed.add_field(name=':id: x  My ID', value= f'>>> 630337223837089824',inline=True)
    embed.add_field(name='<:bot:634854279294877706> x  Guilds', value= f'>>> {(len(client.guilds))}',inline=True)
    embed.add_field(name='<:onlines:715931980742656153> x  Users', value= f'>>> {(len(client.users))}',inline=False)
    embed.add_field(name=':frame_photo: x  Avatar', value= f'>>> [Avatar Link](https://cdn.discordapp.com/avatars/630337223837089824/3e420640a040b9853d2f44f427512d33.webp?size=1024)',inline=True)
    embed.add_field(name=':blue_book: x  Library', value= f'>>> [Discord.py](https://discordpy.readthedocs.io/)',inline=False)

    await ctx.send(embed=embed)


@client.command(aliases=["avatar"])
async def av(ctx, member: discord.User=None):
     embed5 = discord.Embed(
         title=f"{member.name}'s Avatar: "
     )
     embed5.set_author(name=f"{member.name}#{member.discriminator}", icon_url=member.avatar_url)
     embed5.set_image(url=member.avatar_url)
     await ctx.send(embed=embed5)
@av.error
async def av_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send(" <:error:657997451042750485> x  Please specify the user")
@client.command(aliases=["serverinfo, server_info"])
async def serverinfo(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    guild = ctx.author.guild
    roles = str(len(guild.roles))
    emojis = str(len(guild.emojis))
    channels = str(len(guild.channels))
    statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]
    embed = discord.Embed(
        colour=discord.Colour.blue(),
        timestamp=ctx.message.created_at

    )


    embed.set_author(name=f"Server Info")
    embed.set_thumbnail(url=guild.icon_url)
    embed.set_footer(text=f"Requested By {ctx.author}")
    embed.add_field(name=">>> :closed_lock_with_key: x  Name:", value=guild.name, inline=False)
    embed.add_field(name=">>> :shield:   x  ID:", value=guild.id , inline=False)
    embed.add_field(name=">>> :gear:   x  Created at:", value=guild.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
    embed.add_field(name=">>> :bust_in_silhouette: x  Owner:", value=guild.owner, inline=False)
    embed.add_field(name=">>> :busts_in_silhouette:   x  Members:", value=guild.member_count, inline=False)
    embed.add_field(name='>>> :mag_right: x  Members Status:', value=f" :green_circle: - {statuses[0]}  :orange_circle: -  {statuses[1]}  :red_circle: - {statuses[2]}  :white_circle: - {statuses[3]}" , inline=False)
    embed.add_field(name=">>> <:tick:651543094336159787>   x  Boosting Level:", value=guild.premium_tier , inline=False)
    embed.add_field(name=">>> <:error:657997451042750485>   x  Region:", value=guild.region , inline=False)
    embed.add_field(name=">>> <:Verifed:711681731215753228>   x  Verification:", value=guild.verification_level, inline=False)
    embed.add_field(name=">>> <:joecap:716395735448289280>   x  Roles:", value=roles, inline=False)
    embed.add_field(name=">>> <:onlines:715931980742656153>   x  Channels:", value=channels, inline=False)
    embed.add_field(name=">>> <:bot:634854279294877706>   x  Emojis:", value=emojis, inline=False)

    await ctx.send(embed=embed)
@client.command()
async def ping(ctx):
        embed = discord.Embed(
        colour=discord.Colour.blue(),
        title='Ping command!!')

        embed.set_footer(text=f'Request by {ctx.author} | Online   ' ,icon_url=ctx.author.avatar_url)
        embed.add_field(name='<:bot:634854279294877706> x Ping', value= f"```Pong! {round(client.latency * 1000)}ms```",inline=False)

        await ctx.send(embed=embed)
        
#bot-support-commands
        
@client.command()
async def suggest(ctx, *, arg):

    channel = client.get_channel(715951246833352765)
    author = ctx.message.author.name
    icon = ctx.message.author.avatar_url

    embed = discord.Embed(color=0x00ffff)
    embed.set_author(name=author, icon_url=icon)
    embed.add_field(name='<:bot:634854279294877706> x  New Suggestion', value=arg, inline=False)
    embed.add_field(name='Suggested by:', value=f'{ctx.author.mention}', inline=False)
    embed.set_footer(text='Developed by PoundsCoin#3519')
    await channel.send(embed=embed)
    await ctx.send(f"Thanks for your suggestion!")
    await ctx.message.delete()
@suggest.error
async def suggest_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send(" <:error:657997451042750485> x  Please specify something to suggest!")  
@client.command()
async def bugreport(ctx, *, arg):
    channel = client.get_channel(715951274415357952)
    author = ctx.message.author.name
    icon = ctx.message.author.avatar_url

    embed = discord.Embed(color=0x00ffff)
    embed.set_author(name=author, icon_url=icon)
    embed.add_field(name='<:bot:634854279294877706>  x   New Bug Report', value=arg, inline=False)
    embed.add_field(name='Reported by:', value=f'{ctx.author.mention}', inline=False)
    embed.set_footer(text='Developed by PoundsCoin#3519')
    await channel.send(embed=embed)
    await ctx.send(f"Thanks for your bug report!")
    await ctx.message.delete()
@bugreport.error
async def bugreport_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("<:error:657997451042750485> x  Please specify a bug to report")  
@client.command(aliases=['inv', 'i'])
async def invite(ctx):
    embed = discord.Embed(
        colour=discord.Colour.blue(),
    )

    embed.set_footer(text=f'Request by {ctx.author} | Online   ' ,icon_url=ctx.author.avatar_url)
    embed.add_field(name='<:tick:651543094336159787> x  Link', value=' [Invite](https://discord.com/api/oauth2/authorize?client_id=630337223837089824&permissions=8&scope=bot)',inline=False)

    await ctx.send(embed=embed)
#moderation-commands
@client.command()
@commands.has_permissions(kick_members=True)
async def kick (ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    embed = discord.Embed(
        colour=discord.Colour.blue(),
        )
    embed.set_footer(text=f'Request by {ctx.author} | Kick   ' ,icon_url=ctx.author.avatar_url)
    embed.add_field(name='<:tick:651543094336159787> |Done', value=f'>>> User {member} got kicked!',inline=False)
    await ctx.send(embed=embed) 
@kick.error
async def kick_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send(" <:error:657997451042750485> x  Please specify a user to kick")  
@client.command()
@commands.has_permissions(ban_members=True)
async def ban (ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    embed = discord.Embed(
        colour=discord.Colour.blue(),
        )
    embed.set_footer(text=f'Request by {ctx.author} | Ban   ' ,icon_url=ctx.author.avatar_url)
    embed.add_field(name='<:tick:651543094336159787> |Done', value=f'>>> User {member} got banned!',inline=False)
    await ctx.send(embed=embed) 
@ban.error
async def ban_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send(" <:error:657997451042750485>  x  Please specify a user to ban")  


@client.command()
async def announce(ctx, channel: TextChannel, *, message):
    await channel.send("<a:announcement:715970361983893564> x  **Announcement**")
    await channel.send(f"{message}")
    announcement =  await ctx.send(">>> <:tick:651543094336159787> x Announcement successfully created")
    await asyncio.sleep(3)
    await announcement.delete()
@announce.error
async def announce_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send(" <:error:657997451042750485> x  Please specify the channel and message")
@client.event
async def on_message_delete(message):
    global lastdel
    global lastauth
    lastdel = message.content
    lastauth = message.author


@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def snipe(ctx):
    global lastdel
    print(lastdel)

    if lastdel == None:
        await ctx.send('Couldnt find a last message')
    else:
        embed = discord.Embed(title=':jigsaw:  x  SNIPED', description=f'Message sniped : {lastdel}\nMessage From : {lastauth}')
        
        await ctx.send(embed=embed)
@snipe.error
async def snipe_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send(" <:error:657997451042750485> x  Please specify the user")
@client.command()
@commands.has_permissions(kick_members=True)
async def warn(ctx, member:discord.Member, *, arg):
    author = ctx.author
    guild = ctx.guild
    channel = get(guild.text_channels, name='warn-logs')
    if channel is None:
        channel = await guild.create_text_channel('warn-logs')
    await channel.send(f'>>> {member.mention} **got warned by the reason**: {arg} x  **Warned by:** {author.mention}')
    await member.send(f'>>> You got warned for:** {arg}')
    await ctx.message.delete()
@warn.error
async def warn_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("<:error:657997451042750485> x  Please specify the user and reason!")    
@client.command()
@commands.has_permissions(manage_messages=True)

async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)
    lol = await ctx.send(f">>> :white_check_mark: | {amount} Messages removed")
    await asyncio.sleep(3)
    await lol.delete()
@clear.error
async def clear_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("<:error:657997451042750485> x  Please specify the amount of messages to delete")


#help-cmd-commands

@client.command()
async def cmds(ctx):
    embed = discord.Embed(
        colour=discord.Colour.blue(),
        title='Bot Commands')

    embed.set_footer(text=f'Request by {ctx.author}| Online   ' ,icon_url=ctx.author.avatar_url)
    embed.add_field(name='>>> :rotating_light:  x  Prefix', value='`a.`',inline=False)
    embed.add_field(name=' >>> :wrestlers:  x  Fun  ', value=' ```say, 8ball, dm, gay, cookie, password, esay```',inline=False)
    embed.add_field(name='>>> :police_car:  x  Moderation', value=' ```clear, warn, ban, kick, snipe```',inline=False)
    embed.add_field(name='>>> <:error:657997451042750485>  x  Information', value=' ```userinfo, serverinfo, botservers, ping, avatar, botinfo, announce```',inline=False)
    embed.add_field(name='>>> :bust_in_silhouette:  x  Bot Support', value=' ```suggest, bugreport, invite```',inline=False)
    embed.add_field(name='>>> :gear:  x  Configuration', value='```newcategory, newchannel, newvoicechannel, delrole```',inline=False)


    await ctx.send(embed=embed)


    
@client.command()
async def help(ctx):
    embed = discord.Embed(
        colour=discord.Colour.blue(),
        title='Help')
    embed.set_footer(text=f"Requested By {ctx.author}  | Help", icon_url=ctx.author.avatar_url)
    embed.add_field(name='<:error:657997451042750485> | Prefix', value='`a.`',inline=False)
    embed.add_field(name=' :gear: | Developer  ', value=' `PoundsCoin#9999`',inline=False)
    embed.add_field(name=' <:onlines:715931980742656153>   | Commands', value=' >>> Do a.cmds to see the commands',inline=False)
    embed.add_field(name='<:joecap:716395735448289280> | Add-ons', value=' >>> [Support](https://discord.gg/u4Hr7YV) ',inline=False)
    await ctx.send(embed=embed)
    
#config-commands
@client.command()
@has_permissions(manage_messages=True)
async def delrole(ctx, role: discord.Role):
    await role.delete()
    embed = discord.Embed(
        colour=discord.Colour.blue(),
        )
    embed.set_footer(text=f'Request by {ctx.author} | Role   ' ,icon_url=ctx.author.avatar_url)
    embed.add_field(name='<:tick:651543094336159787> | Role deleted', value=f'>>> `{role.name}`',inline=False)
    await ctx.send(embed=embed) 
@delrole.error
async def delrole_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send(" <:error:657997451042750485> x  Please specify a role to delete")  

@client.command()
@has_permissions(manage_channels=True)
async def newcategory(ctx, *, name):
    embed = discord.Embed(
        colour=discord.Colour.blue(),
        title='New category Created')
    embed.set_footer(text=f'Request by {ctx.author} | Category   ' ,icon_url=ctx.author.avatar_url)
    embed.add_field(name='<:tick:651543094336159787> | Congrats!', value=f'>>> `{name}` Has been created',inline=False)
    await ctx.guild.create_category(name)
    await ctx.send(embed=embed)
@newcategory.error
async def newcategory_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send(" <:error:657997451042750485> x  Please specify a category to create")  
@client.command()
@has_permissions(manage_channels=True)
async def newchannel(ctx, *, name):
    embed = discord.Embed(
        colour=discord.Colour.blue(),
        title='New channel Created')
    embed.set_footer(text=f'Request by {ctx.author} | Channel   ' ,icon_url=ctx.author.avatar_url)
    embed.add_field(name='<:tick:651543094336159787> | Congrats!', value=f'>>> `{name}` Has been created',inline=False)
    await ctx.guild.create_text_channel(name)
    await ctx.send(embed=embed)
@newchannel.error
async def newchannel_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send(" <:error:657997451042750485> x  Please specify a channel to create")  
@client.command()
@has_permissions(manage_channels=True)
async def newvoicechannel(ctx, *, name):
    embed = discord.Embed(
        colour=discord.Colour.blue(),
        title='New voice channel Created')
    embed.set_footer(text=f'Request by {ctx.author} | Voice Channel     ' ,icon_url=ctx.author.avatar_url)
    embed.add_field(name='<:tick:651543094336159787> | Congrats!', value=f'>>> `{name}` Has been created',inline=False)
    await ctx.guild.create_voice_channel(name)
    await ctx.send(embed=embed)
@newvoicechannel.error
async def newvoicechannel_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send(" <:error:657997451042750485> x  Please specify a voice channel to create")  
#Events

@client.event
async def on_ready():
    change_status.start()
    print(f'All good')
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
     await ctx.send(f"<:error:657997451042750485> | Error, You don't have enough permissions to use this command!")

@client.event
async def on_member_join(member):
   await client.get_channel(715954486870540298).send(f"Welcome {member.mention}, please remember reading <#715957309951574017> and have fun!")

@client.event
async def on_member_remove(member):
   await client.get_channel(715954486870540298).send(f"{member.name} has left :(")     
@tasks.loop(seconds= 7)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


