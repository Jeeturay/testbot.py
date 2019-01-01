import requests
import json
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from locoapi import *
import pandas
client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
	print("Bot Logged in",client.user.name)
	print("------------------------------")


@client.command(pass_context=True,no_pm=True)
async def locotime():
        times = get_show()
        time_loco = str(pandas.to_datetime(times['start_time'],unit='ms'))
        embed = discord.Embed(title="Next Loco Details",description="The Next Loco is At",colour=discord.Colour.red())
        embed.set_thumbnail(url="https://is3-ssl.mzstatic.com/image/thumb/Purple128/v4/06/0b/b5/060bb52a-7818-02a6-7922-c076d844c226/source/512x512bb.jpg")
        embed.set_author(name="Loco's Time",icon_url="https://is3-ssl.mzstatic.com/image/thumb/Purple128/v4/06/0b/b5/060bb52a-7818-02a6-7922-c076d844c226/source/512x512bb.jpg")
        embed.set_footer(text="Its For u By Mahesh")
        embed.add_field(name="Next Loco",value=times['name'],inline=True)
        embed.add_field(name="Time of Loco Game",value=time_loco,inline=True)
        embed.add_field(name="No of Questions",value=10,inline=True)
        embed.add_field(name="Prize for Next Loco",value=times['prize'],inline=True)
        embed.add_field(name="Name of Loco",value=times['contest_category_name'],inline=True)
        embed.add_field(name="Is it Spped Loco",value= not times['is_live_host'],inline=True)

        await client.say(embed=embed)

@client.command(pass_context=True,no_pm=True)
async def locouser(ctx,user:str):
        searchs = search(user)
        print(searchs)
        data = searchs[0]
        userid = data['user_uid']
        details = get_user_profile(userid)
        username = details['username']
        img = details['avatar_url']
        total_money = details['total_earning']
        questions = str(details['total_correct_question_answered'])+"/"+str(details['total_question_answered'])
        wins = str(details['total_win'])+"/"+str(details['total_contest_played'])
        friends = details['total_friends']
        coins = details['total_coin_earned']
        streaks = details['total_past_streaks_count']

        embed = discord.Embed(title="My-loco's Profile",description="Loco's Profile of " + user,colour=discord.Colour.purple())
        embed.set_footer(text="By-Team of My-Loco")
        embed.set_author(name="Loco",icon_url="https://is3-ssl.mzstatic.com/image/thumb/Purple128/v4/06/0b/b5/060bb52a-7818-02a6-7922-c076d844c226/source/512x512bb.jpg")
        embed.add_field(name="Username in Loco",value=username)
        embed.add_field(name="Userid in Loco",value=userid)
        embed.add_field(name="Question Summary",value=questions)
        embed.add_field(name="Total Streaks",value=streaks)
        embed.add_field(name="No of Friends",value=friends)
        embed.add_field(name="Total Coins u got",value=coins)
        embed.add_field(name="Total Money U won",value=total_money)
        embed.add_field(name="Total Won Games",value=wins)
        embed.set_thumbnail(url=img)
        await client.say(embed=embed)

@client.command(pass_context=True,no_pm=True)
async def forcoins(ctx,user:str):
        sinfo = search(user)
        if not sinfo:
                embed = discord.Embed(title="Error",description="Error Response",colour=discord.Colour.red())
                embed.add_filed(name="Error Name",value="No user Find With that username")
                embed.add_filed(name="Suggestion",value="Please Check once Again the username")
                await cline.say(embed=embed)
        else:
                data = sinfo[0]
                userid = data['user_uid']
                data = {
                    "client_id": "UYHvqxF1oIC2iXjo4NffoUh7akQ1ztn4eguyJ7c7",
                        "client_secret": "BsvYdIVl2kKRSW6g2ViOTuh4J0QiavxoWXOnMa6g2YqRw0NzorU3FmrtSdoRtH1aVv4DwhIgnFrO3ncEtGa1B2htIDDMhWNdQbEmQK58apJMn9FbrJxxJLBGlk1gxivW",
                        "to_user_uid": userid
                                 }
                res = acceptme(data)
                print(res)
                if 'success' in res:
                        await client.say("Yes, You got it")
                elif 'message' in res:
                        await client.say(res['message'])

@client.command(pass_context=True,no_pm=True)
async def helpu():
        embed = discord.Embed(title="Shows Help Menu",description="Total Commands",colour=discord.Colour.dark_gold())
        embed.add_field(name="!locotime",value="Show Next Loco game Info",inline=False)
        embed.add_field(name="!forcoins",value="Gives you a 460 coins",inline=False)
        embed.add_field(name="!locouser <username>", value="Shows Stats of Loco Profile",inline=False)
        embed.add_field(name="Usage of !forcoins",value="!forcoins,  Send Friend Request to my-loco username \n After Request sent type command followed by username",inline=False)
        await client.say(embed=embed)
   
client.run('NTA4ODY4MTE3NjYxNzQ1MTUz.DwX4-w.XxXJm-F2d0FYD1euITeKEacW_6k')
