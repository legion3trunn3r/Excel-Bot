#!/usr/sbin/python3

from data.bot_creating import dp, bot
from aiogram import types as Message, Dispatcher
from sheets.spreadsheets import Sheets

async def start(message: Message):
    await message.answer("Hello, my name is Noelle, I am your personal financial assistant.")

async def get_all_stat(message: Message):
    stat = Sheets.get_data_from_sheet('dev!A2:A5')
    await message.answer(f"Finance statistics:\n\n💶 The rest of free money: {stat[0][0]}\n\n🥡 The rest of market money: {stat[1][0]}\n\n🛒 Market expenses: {stat[3][0]}\n\n💸 Total expenses: {stat[2][0]}")

# Handlers calling
def register_handlers_client(dp: Dispatcher):

    try:

        dp.register_message_handler(start, commands=['start'])

        dp.register_message_handler(get_all_stat, commands=['get_stat'])

    except KeyError:
        print(KeyError)