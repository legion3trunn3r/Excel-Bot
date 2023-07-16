#!/usr/bin/python3

from aiogram import executor, types
from data.bot_creating import dp, bot
from handlers import client

# Handler
client.register_handlers_client(dp)


#Commands description
async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Noelle greeting"),
        types.BotCommand("get_stat", "Show finance statistics")
    ])

# Bot starting
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=set_default_commands)
