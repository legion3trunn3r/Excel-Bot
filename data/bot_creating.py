#!/usr/sbin/python3

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from creds.tgAPI.bot_token import bot_token

bot = Bot(bot_token)
dp = Dispatcher(bot)