from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

admin_film_change_film = CallbackData("change_film_film", "action", "film_id")
admin_film_change_name = CallbackData("change_film_name", "action", "film_id")
admin_film_change_state = CallbackData("change_film_state", "action", "film_id")
admin_film_change_date = CallbackData("change_film_date ", "action", "film_id")
admin_film_change_type = CallbackData("change_film_type", "action", "film_id")
admin_film_change_instagram = CallbackData("change_film_instagram", "action", "film_id")
admin_film_change_you_tube = CallbackData("change_film_you_tube", "action", "film_id")
admin_film_delete = CallbackData("change_film_delete", "action", "film_id")


async def admin_film_change_def(film_id: int):
    admin_film_change = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Kino 🎥",
                    callback_data=admin_film_change_film.new(action="change_film_film",
                                                             film_id=film_id)),
                InlineKeyboardButton(
                    text="Ismi 🎬",
                    callback_data=admin_film_change_name.new(action="change_film_name",
                                                             film_id=film_id))
            ],
            [
                InlineKeyboardButton(
                    text="Davlari 🌏",
                    callback_data=admin_film_change_state.new(action="change_film_state",
                                                              film_id=film_id)),
                InlineKeyboardButton(
                    text="Sanasi 📅",
                    callback_data=admin_film_change_date.new(action="change_film_date",
                                                             film_id=film_id))
            ],
            [
                InlineKeyboardButton(
                    text="Instagram 💜",
                    callback_data=admin_film_change_instagram.new(action="change_film_instagram",
                                                                  film_id=film_id)),

                InlineKeyboardButton(
                    text="You Tube ❤️",
                    callback_data=admin_film_change_you_tube.new(action="change_film_you_tube",
                                                                 film_id=film_id)),
            ],
            [
                InlineKeyboardButton(
                    text="Turi 🎞️",
                    callback_data=admin_film_change_type.new(action="change_film_type",
                                                             film_id=film_id))

            ],
            [
                InlineKeyboardButton(
                    text="O'chirib yuborish 🗑",
                    callback_data=admin_film_delete.new(action="change_film_delete",
                                                        film_id=film_id))
            ],
        ]
    )
    return admin_film_change
