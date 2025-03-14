import logging
from aiogram import Bot, Dispatcher, executor, types
from keyboards import kanal_keyboard, valyuta_keyboard
import requests

API_TOKEN = "6146304144:AAH752IRKNgDIL1k4a5-vuvSuShQ-qIojSM" 
CHANNEL_ID = -1001687130068
URL = "https://nbu.uz/uz/exchange-rates/json/"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot)

async def changer(sum, out):
    data = requests.get(url=URL).json()
    for d in data:
        if d['code'] == out:
            money = d['cb_price']
    result = sum / money
    return result

async def obuna_boganmi(odam_id):
    chat_member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=odam_id)
    if chat_member.status in ['creator', 'member', 'administrator']:
        return True


@dp.message_handler(commands=['start'])
async def salom_ber(message: types.Message):
    if await obuna_boganmi(message.from_user.id):
        await message.answer(text="Assalomu aleykum, xush kelibsiz kerakli valyutani tanlang!", reply_markup=valyuta_keyboard)
    else:
        await message.answer(text="Kanalga obuna bo'lmagansiz, obuna bo'lib qaytadan tekshiring:\n/start", reply_markup=kanal_keyboard)


@dp.callback_query_handler()
async def valyuta_changer(call: types.CallbackQuery):
    valyutadan, valyutaga = call.data.split('_')[0], call.data.split('_')[1]
    await call.message.answer(f"{valyutaga} tanlandi, summa kiriting:")


@dp.message_handler()
async def summa(message: types.Message):
    som = message.text
    javob = await changer(sum=som, out="RUB")
    




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


