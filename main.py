import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import commands
import random
import ch
import meme

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6543916116:AAHZtmmCi0h8W3qprT4rHZ5Rl-4gdwLyaR4")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start", "help"))
async def start_message(message: types.Message):
    commands.count_add()
    await message.answer(commands.start)

@dp.message(Command("chat"))
async def start_message(message: types.Message):
    commands.count_add()
    await message.answer(commands.chat)

@dp.message(Command("count"))
async def count_message(message):
    commands.count_add()
    await message.answer(f"Общее количество введенных команд: {open('counter.txt', 'r').read()}\n"
                         f"Общее количество сообщений: {open('counter_msg.txt', 'r').read()}")

@dp.message(Command("2ch"))
async def test_message(message):
    commands.count_add()
    await message.answer(f'{ch.list_2ch[random.randint(0, len(ch.list_2ch) -1)]}')

@dp.message(Command("meme"))
async def test_message(message):
    commands.count_add()
    await message.answer(f'{meme.meme[random.randint(0, len(meme.meme) -1)]}')

@dp.message(Command("future"))
async def test_message(message):
    commands.count_add()
    await message.answer(f'{commands.future[random.randint(0, len(commands.future) -1)]}')

@dp.message(Command("rules"))
async def start_message(message: types.Message):
    commands.count_add()
    await message.answer(commands.rules)

@dp.message(Command("iq"))
async def start_message(message: types.Message):
    commands.count_add()
    iq = random.randint(0, 229)
    if iq == 0:
        await message.answer("У тебя 0 IQ\n\n"
                             "Ахахахахах, по IQ ты равен камню")
    elif 0 < iq < 51:
        await message.answer(f"У тебя {iq} IQ\n\n"
                             "Примерно столько у 7-ми летнего ребенка")
    elif 50 < iq < 101:
        await message.answer(f"У тебя {iq} IQ\n\n"
                             "Ничего особенного")
    elif 100 < iq < 160:
        await message.answer(f"У тебя {iq} IQ\n\n"
                             "Ваш IQ выше среднего")
    elif iq == 160:
        await message.answer(f"У тебя {iq} IQ\n\n"
                             "У вас такое же IQ, как и у Энштейна")
    elif 160 < iq < 228:
        await message.answer(f"У тебя {iq} IQ\n\n"
                             "У вас запредельно высокий IQ")

#dp.message(message)
#async def echo(message: types.Message):
#        if message.text == 'Ослина' or message.text == 'ослина':
#            await message.answer('Звал?')


# Запуск процесса поллинга новых апдейтов
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())