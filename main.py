import asyncio
from datetime import datetime
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
        input_field_placeholder="Здравья Гавриловне"
    )
    await message.answer("Выбор", reply_markup=keyboard)

# Фильтр текста работает корректно
@dp.message(F.text.lower() == "когда за стол?")
async def with_puree(message: types.Message):
    if Uberprufung_der_aktuellen_Uhrzeit("13:00", "13:31"):
        gehen = "Сейчас **нужно идти за стол**"
    else:
        gehen = "Сейчас за стол идти **не нужно**"
    await message.reply(f"За стол работает в обед, с 1:00 ПМ по 1:31 ПМ\n\n{gehen}")

def Uberprufung_der_aktuellen_Uhrzeit(Minimum, Maximum):
    now = datetime.now()
    current_zeit = now.time()
    start = datetime.strptime(f"{Minimum}", "%H:%M").time()
    ende = datetime.strptime(f"{Maximum}", "%H:%M").time()
    if start <= current_zeit <= ende:
        return True
    else:
        return False

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.run(main())
