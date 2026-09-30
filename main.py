import asyncio
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F
from aiogram.utils.keyboard import ReplyKeyboardBuilder

schlussel = ""

bot = Bot(token=schlussel)
dp = Dispatcher()

@dp.message(Command("старт"))
async def cmd_start(message: types.Message):
    builder = ReplyKeyboardBuilder()

    buttons = [
        "Когда за стол?",
        "В которую пору книгохранилище двери отворяет?",
        "Кто ведёт русский язык?",
        "Какое имя у Надежды Намсараевны?",
        "Почему?",
        "Расписания на сегодня?"
    ]

    for text in buttons:
        builder.add(types.KeyboardButton(text=text))

    # adjust(1, 2, 2) означает: 1 кнопка в 1-й строке, 2 во 2-й, 2 в 3-й
    builder.adjust(1, 2, 2)

    await message.answer(
        "Выбор",
        reply_markup=builder.as_markup(
            resize_keyboard=True,
            input_field_placeholder="Здравья Гавриловне"
        )
    )

@dp.message(F.text.lower() == "когда за стол?")
async def esszimmer(message: types.Message):
    if Uberprufung_der_aktuellen_Uhrzeit("11:25", "11:45"):
        gehen = "Сейчас **нужно идти за стол**"
    else:
        gehen = f"Сейчас за стол идти **не нужно**\n\nДо за стола осталось: {Timing("11:25")}"
    await message.reply(f"За стол работает в обед, с 11:25 по 11:45 \n\n{gehen}", parse_mode="Markdown")

@dp.message(F.text == "В которую пору книгохранилище двери отворяет?")
async def bibliothek(message: types.Message):
    if Uberprufung_der_aktuellen_Uhrzeit("8:00", "19:00"):
        gehen = "Сей час — **книгохранилище работает**"
    else:
        gehen = f"\n\nСейчас книгохранилище **закрыто**, до нового открытия осталось: {Timing("8:00")}"
    await message.reply(f"Книгохранилище работает, с 8:00 АМ по 19:00{gehen}", parse_mode="Markdown")

@dp.message(F.text == "Кто ведёт русский язык?")
async def bibliothek(message: types.Message):
    await message.reply(f"Русский язык ведёт учительница с именем Учительница по русскому языку", parse_mode="Markdown")

@dp.message(F.text == "Какое имя у Надежды Намсараевны?")
async def bibliothek(message: types.Message):
    await message.reply(f"Её не завут, она сама приходит", parse_mode="Markdown")

@dp.message(F.text == "Почему?")
async def bibliothek(message: types.Message):
    await message.reply(f"Потому что!", parse_mode="Markdown")

@dp.message(F.text == "Расписания на сегодня?")
async def bibliothek(message: types.Message):
    await message.reply(f"{Stundenplan()}", parse_mode="Markdown")

def Uberprufung_der_aktuellen_Uhrzeit(Minimum, Maximum):
    now = datetime.now(ZoneInfo("Asia/Chita"))
    current_zeit = now.time()
    start = datetime.strptime(f"{Minimum}", "%H:%M").time()
    ende = datetime.strptime(f"{Maximum}", "%H:%M").time()
    return start <= current_zeit <= ende

def Timing(Zeit):
    now = datetime.now(ZoneInfo("Asia/Chita"))

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

def Stundenplan(woche=None):
    if woche is None:
        woche = datetime.now(ZoneInfo("Asia/Chita")).weekday()
    
    match woche:
        case 0:
            return "Расписания на понедельник неизвестно"
        case 1:
            return "Расписания на вторник неизвестно"
        case 2:
            return "Расписания на тройник неизвестно"
        case 3:
            return "Расписания на четверник неизвестно"
        case 4:
            return "Расписания на пятник неизвестно"
        case 5:
            return "Расписания на шестерник неизвестно"
        case _:
            return "Расписания на неизвестный день недели неизвестно"
    

async def main():
    print("START DAS PROGRAMM")
    await dp.start_polling(bot)

if __name__ == '__main__':
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.run(main())
