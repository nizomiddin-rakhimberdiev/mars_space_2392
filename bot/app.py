from aiogram import Bot, Dispatcher, types, F
import asyncio

from aiogram.fsm.context import FSMContext

from states import RegisterStates
from database import Database

db = Database()

bot = Bot(token="7110333341:AAFsQLYZHd0lDone8Xf6k0nJ0iTi5KOgqFg")
dp = Dispatcher()

@dp.message(F.text == '/start')
async def start(message: types.Message, state: FSMContext):
    data = db.check_authentication(message.from_user.id)
    if data:
        await message.answer("Assalamu alaykum, nima kerak")
    else:
        await message.answer("Ro'yxatdan o'tish uchun Space id ni yuboring")
        await state.set_state(RegisterStates.space_id)

@dp.message(RegisterStates.space_id)
async def register(message: types.Message, state: FSMContext):
    space_id = message.text
    data = db.check_authentication(message.from_user.id)
    if data:
        await message.answer("Siz ro'yxatdan o'tgansiz")
    else:
        db.registration(message.from_user.id, space_id)
        await message.answer("Ro'yxatdan o'tdingiz")
        await state.clear()

async def main():
    db.create_table()
    await dp.start_polling(bot)

if __name__ == '__main__':
    print("Bot is running...")
    asyncio.run(main())