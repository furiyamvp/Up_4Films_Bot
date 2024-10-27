from aiogram import types
from keyboards.default.user import user_main_menu_def
from loader import dp


@dp.message_handler(text="Call-markaz 📞", state="*")
async def call_center_handler(message: types.Message):
    text = """
1) @Zangori_Ekran_Admin
"""
    await message.answer(text=text, reply_markup=await user_main_menu_def())
