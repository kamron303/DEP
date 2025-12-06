import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command

TOKEN = "8481219439:AAHew1lz7LDXoSMff-Z3wv7CkbAQJcNe3vw"

bot = Bot(TOKEN)
dp = Dispatcher()

spam_tasks = {}

@dp.message(Command("start"))
async def start_cmd(message: Message):
    chat_id = message.chat.id

    if chat_id in spam_tasks:
        await message.answer("Уже запущено!")
        return

    await message.answer("Запускаю 🎰 … деп деп")

    async def spam():
        while True:
            await message.answer("🎰")  # просто эмодзи
            await message.answer("деп деп")
            await asyncio.sleep(2)

    task = asyncio.create_task(spam())
    spam_tasks[chat_id] = task

@dp.message(Command("stop"))
async def stop_cmd(message: Message):
    chat_id = message.chat.id

    if chat_id in spam_tasks:
        spam_tasks[chat_id].cancel()
        del spam_tasks[chat_id]
        await message.answer("Ладно, так уж и быть")
    else:
        await message.answer("Он ещё не запущен")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
