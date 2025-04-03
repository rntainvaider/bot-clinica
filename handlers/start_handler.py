from aiogram.types import Message
from aiogram import F, Router
from aiogram.filters import Command
from keyboards.keyboard import get_inline_keyboard, get_start_keyboard

router_start = Router()


@router_start.message(Command("start"))
async def handle_command_start(message: Message) -> None:
    keyboard = get_start_keyboard()
    text = """
    <blockquote>
        This is a quoted message.
    </blockquote>
    """
    await message.answer(text, parse_mode="HTML", reply_markup=keyboard)


@router_start.message(F.text == "Название клиники")
async def handle_clinic_name_request(message: Message) -> None:
    inline_keyboard = get_inline_keyboard()
    await message.answer("asd", reply_markup=inline_keyboard)


@router_start.message(F.text == "Услуги")
async def handle_services_request(message: Message) -> None:
    await message.answer("asd")


@router_start.message(F.text == "Мой кабинет")
async def handle_personal_account_request(message: Message) -> None:
    await message.answer("asd")


@router_start.message(F.text == "Поддержка")
async def handle_support_request(message: Message) -> None:
    await message.answer("asd")


@router_start.message(F.text == "ВЫЗОВ ВРАЧА НА ДОМ")
async def handle_doctor_call_request(message: Message) -> None:
    await message.answer("asd")
