import asyncio
from dyscord_plugin import DyscordPlugin
from dyscord_plugin.message import DyscordContext
from discord.ext.commands import command
import discord


class DyscordFun(DyscordPlugin):
    '''This is the fun plugin for Dyscord.'''
    def __init__(self, b):
        super().__init__(b)

    @command(pass_context=True)
    async def aesthetic(self, ctx: DyscordContext, *, phrase):
        """ＡＥＳＴＨＥＴＩＣ"""
        char = "abcdefghijklmnopqrstuvwxyz"
        tran = "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"
        table = str.maketrans(char, tran)
        char = char.upper()
        tran = "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"
        table = str.maketrans(char, tran)
        msg = phrase.translate(table)
        await ctx.channel.send(msg)