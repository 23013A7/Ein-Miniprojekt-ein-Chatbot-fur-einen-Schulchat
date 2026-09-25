import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import  Command

schlussel = ""

bot = Bot(token=schlussel)
dp = Dispatcher()

@dp.message(Command("старт"))
async def cmd_start(message: types.Message):
    await message.answer(f"СУПЕРИЕРОГЛИФЫ")
