from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


def get_start_keyboard() -> ReplyKeyboardMarkup:
    kb = [
        [
            KeyboardButton(text="Название клиники"),
        ],
        [
            KeyboardButton(text="Услуги"),
            KeyboardButton(text="Мой кабинет"),
        ],
        [
            KeyboardButton(text="Поддержка"),
            KeyboardButton(text="ВЫЗОВ ВРАЧА НА ДОМ"),
        ],
    ]

    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери че тебе надо",
    )

    return keyboard


def get_inline_keyboard() -> InlineKeyboardMarkup:
    kb = [
        [
            InlineKeyboardButton(text="Перейти на сайт", url="https://example.com"),
        ],
        [
            InlineKeyboardButton(text="Кнопка с callback", callback_data="callback_1"),
            InlineKeyboardButton(text="Другая кнопка", callback_data="callback_2"),
        ],
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)

    return keyboard
