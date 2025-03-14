
from aiogram import types


kanal_keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
    [types.InlineKeyboardButton("Kanalga obuna", url='https://t.me/asilbekmirolimov')]
])


valyuta_keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
    [types.InlineKeyboardButton("🇺🇿 UZS ▶️ RUB 🇷🇺", callback_data='UZS_RUB'), types.InlineKeyboardButton("🇷🇺 RUB ▶️ UZS 🇺🇿", callback_data='RUB_UZS')],
    [types.InlineKeyboardButton("🇺🇸 USD ▶️ RUB 🇷🇺", callback_data='USD_RUB'), types.InlineKeyboardButton("🇷🇺 RUB ▶️ USD 🇺🇸", callback_data='RUB_USD')],
    [types.InlineKeyboardButton("🇺🇸 USD ▶️ UZS 🇺🇿", callback_data='USD_UZS'), types.InlineKeyboardButton("🇺🇿 UZS ▶️ USD 🇺🇸", callback_data='UZS_USD')]
])