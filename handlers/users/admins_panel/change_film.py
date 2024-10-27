from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.admin import admin_main_menu_def
from keyboards.inline.change_film import *
from main.config import ADMINS
from states.UpdateFilmState import UpdateFilm
from loader import dp
from utils.checker.checker_link import check_link_instagram, check_link_you_tube
from utils.db_commands.update_film import admin_update_film, admin_delete_film


@dp.callback_query_handler(admin_film_change_film.filter(action="change_film_film"), chat_id=ADMINS)
async def admin_change_film_film_handler(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    film_id = callback_data.get('film_id')
    await state.update_data(film_id=film_id)
    text = "Please upload the movie to the bot"
    await call.message.answer(text=text)
    await UpdateFilm.film.set()


@dp.message_handler(state=UpdateFilm.film, chat_id=ADMINS, content_types=types.ContentType.VIDEO)
async def change_film_film_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    film_id = data.get('film_id')
    print(film_id)
    film = message.video.file_id

    if await admin_update_film(int(film_id), "film", film, message.date):
        text = "Film changed 🔄"
        await message.answer(text=text, reply_markup=await admin_main_menu_def())
        await state.finish()
    else:
        text = "An error occurred while changing the movie 🔄❌"
        await message.answer(text=text, reply_markup=await admin_main_menu_def())
        await state.finish()


@dp.message_handler(state=UpdateFilm.film)
async def error_film_handler(message: types.Message):
    text = "You can only upload videos, you cannot upload anything in text format."
    await message.answer(text=text)
    await UpdateFilm.film.set()


@dp.callback_query_handler(admin_film_change_name.filter(action="change_film_name"), chat_id=ADMINS)
async def admin_change_film_name_handler(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    film_id = callback_data.get('film_id')
    await state.update_data(film_id=film_id)
    text = "Please enter a new film name"
    await call.message.answer(text=text)
    await UpdateFilm.name.set()


@dp.message_handler(state=UpdateFilm.name)
async def update_name_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    film_id = data.get('film_id')
    name = message.text

    if await admin_update_film(int(film_id), "name", name, message.date):
        text = "Film's name changed 🔄"
        await message.answer(text=text, reply_markup=await admin_main_menu_def())
        await state.finish()
    else:
        text = "An error occurred while renaming the movie 🔄❌"
        await message.answer(text=text, reply_markup=await admin_main_menu_def())
        await state.finish()


@dp.callback_query_handler(admin_film_change_state.filter(action="change_film_state"), chat_id=ADMINS)
async def admin_change_film_state_handler(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    film_id = callback_data.get('film_id')
    await state.update_data(film_id=film_id)
    text = "Please enter a new film state"
    await call.message.answer(text=text)
    await UpdateFilm.state.set()


@dp.message_handler(state=UpdateFilm.state)
async def update_state_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    film_id = data.get('film_id')
    state = message.text
    if await admin_update_film(int(film_id), "state", state, message.date):
        text = "Film's state changed 🔄"
        await message.answer(text=text, reply_markup=await admin_main_menu_def())
        await state.finish()

    else:
        text = "Error: Film's didn't state change 🔄❌"
        await message.answer(text=text, reply_markup=await admin_main_menu_def())
        await state.finish()


@dp.callback_query_handler(admin_film_change_date.filter(action="change_film_date"), chat_id=ADMINS)
async def admin_change_film_date_handler(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    film_id = callback_data.get('film_id')
    await state.update_data(film_id=film_id)
    text = "Please enter a new film date"
    await call.message.answer(text=text)
    await UpdateFilm.date.set()


@dp.message_handler(state=UpdateFilm.date)
async def update_date_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    film_id = data.get('film_id')
    date = message.text
    if message.text.isnumeric():
        if await admin_update_film(int(film_id),"date", int(date), message.date):
            text = "Film's date changed 🔄"
            await message.answer(text=text, reply_markup=await admin_main_menu_def())
            await state.finish()
        else:
            text = "Error: Film's didn't date change 🔄❌"
            await message.answer(text=text, reply_markup=await admin_main_menu_def())
            await state.finish()
    else:
        text = "Please do not use numbers"
        await message.answer(text=text)
        await UpdateFilm.date.set()


@dp.callback_query_handler(admin_film_change_type.filter(action="change_film_type"), chat_id=ADMINS)
async def admin_change_film_type_handler(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    film_id = callback_data.get('film_id')
    await state.update_data(film_id=film_id)
    text = "Please enter a new film type"
    await call.message.answer(text=text)
    await UpdateFilm.type.set()


@dp.message_handler(state=UpdateFilm.type)
async def update_type_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    film_id = data.get('film_id')
    tpy = message.text
    if await admin_update_film(int(film_id), "type", tpy, message.date):
        text = "Film's type changed 🔄"
        await message.answer(text=text, reply_markup=await admin_main_menu_def())
        await state.finish()
    else:
        text = "Error: Film's didn't type change 🔄❌"
        await message.answer(text=text, reply_markup=await admin_main_menu_def())
        await state.finish()


@dp.callback_query_handler(admin_film_change_instagram.filter(action="change_film_instagram"), chat_id=ADMINS)
async def admin_change_film_instagram_handler(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    film_id = callback_data.get('film_id')
    await state.update_data(film_id=film_id)
    text = "Please enter a new film instagram link"
    await call.message.answer(text=text)
    await UpdateFilm.instagram.set()


@dp.message_handler(state=UpdateFilm.instagram)
async def update_instagram_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    film_id = data.get('film_id')
    instagram = message.text.split("=")[0]
    if await check_link_instagram(message.text):
        if await admin_update_film(int(film_id), "instagram", instagram, message.date):
            text = "Film's instagram link changed 🔄"
            await message.answer(text=text, reply_markup=await admin_main_menu_def())
            await state.finish()
        else:
            text = "Error: Film's didn't instagram link change 🔄❌"
            await message.answer(text=text, reply_markup=await admin_main_menu_def())
            await state.finish()
    else:
        text = "You can only enter an instagram link"
        await message.answer(text=text)
        await UpdateFilm.instagram.set()


@dp.callback_query_handler(admin_film_change_you_tube.filter(action="change_film_you_tube"), chat_id=ADMINS)
async def admin_change_film_tiktok_handler(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    film_id = callback_data.get('film_id')
    await state.update_data(film_id=film_id)
    text = "Please enter a new film you tube link"
    await call.message.answer(text=text)
    await UpdateFilm.you_tube.set()


@dp.message_handler(state=UpdateFilm.you_tube)
async def update_tiktok_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    film_id = data.get('film_id')
    you_tube = message.text.split("=")[0]
    if await check_link_you_tube(message.text):
        if await admin_update_film(int(film_id), "you_tube", you_tube, message.date):
            text = "Film's you tube link changed 🔄"
            await message.answer(text=text, reply_markup=await admin_main_menu_def())
            await state.finish()
        else:
            text = "Error: Film's didn't you tube link change 🔄❌"
            await message.answer(text=text, reply_markup=await admin_main_menu_def())
            await state.finish()
    else:
        text = "You can only enter an you tube link"
        await message.answer(text=text)
        await UpdateFilm.you_tube.set()


@dp.callback_query_handler(admin_film_delete.filter(action="change_film_delete"), chat_id=ADMINS)
async def admin_change_film_tiktok_handler(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    film_id = callback_data.get('film_id')
    if await admin_delete_film(int(film_id)):
        text = "The film has been deleted 🔄"
        await call.message.answer(text=text, reply_markup=await admin_main_menu_def())
        await state.finish()
    else:
        text = "There is an error while deleting the movie 🗑❌"
        await call.message.answer(text=text, reply_markup=await admin_main_menu_def())
        await state.finish()
