import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F

schlussel = ""

bot = Bot(token=schlussel)
dp = Dispatcher()

@dp.message(Command("старт"))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Когда за стол?"),
            types.KeyboardButton(text="В которую пору книгохранилище двери отворяет?")
        ],
    ]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Текст где то"
    )
    await message.answer("Выбор", reply_markup=keyboard)

# Фильтр текста работает корректно
@dp.message(F.text.lower() == "когда за стол?")
async def with_puree(message: types.Message):
    await message.reply("РАБОТАЕТ")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.run(main())
