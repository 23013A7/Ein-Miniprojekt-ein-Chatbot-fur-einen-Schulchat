import asyncio
from datetime import datetime, timedelta
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

@dp.message(F.text.lower() == "когда за стол?")
async def with_puree(message: types.Message):
    if Uberprufung_der_aktuellen_Uhrzeit("13:00", "13:31"):
        gehen = "Сейчас **нужно идти за стол**"
    else:
        gehen = f"Сейчас за стол идти <b>не нужно</b>\n\nДо за стола осталось: {Timing("13:00")}"
    await message.reply(f"За стол работает в обед, с 1:00 ПМ по 1:31 ПМ\n\n{gehen}", parse_mode="Markdown")

def Uberprufung_der_aktuellen_Uhrzeit(Minimum, Maximum):
    now = datetime.now()
    current_zeit = now.time()
    start = datetime.strptime(f"{Minimum}", "%H:%M").time()
    ende = datetime.strptime(f"{Maximum}", "%H:%M").time()
    if start <= current_zeit <= ende:
        return True
    else:
        return False

def Timing(Zeit):
    now = datetime.now()

    zielzeit = datetime.strptime(Zeit, "%H:%M")

    zieldatum_uhrzeit = now.replace(
        hour=zielzeit.hour,
        minute=zielzeit.minute,
        second=0,
        microsecond=0
    )

    if now > zieldatum_uhrzeit:
        zieldatum_uhrzeit += timedelta(days=1)

    time_left = zieldatum_uhrzeit - now

    gesamt_sekunden = int(time_left.total_seconds())
    stunden = gesamt_sekunden // 3600
    minuten = (gesamt_sekunden % 3600) // 60
    sekunden = gesamt_sekunden % 60

    return f"{stunden}:{minuten}:{sekunden}"

async def main():
    print("START DAS PROGRAMM")
    await dp.start_polling(bot)

if __name__ == '__main__':
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.run(main())
