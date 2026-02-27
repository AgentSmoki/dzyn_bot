from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("search"))
async def cmd_search(message: Message) -> None:
    """Поиск трека по названию или исполнителю."""
    await message.answer("🔍 Напиши название трека или исполнителя:")


@router.message()
async def handle_text_search(message: Message) -> None:
    """Обрабатывает текстовые сообщения как поисковый запрос."""
    if not message.text:
        return

    query = message.text.strip()
    # TODO: вызвать music_search.search(query) и вернуть результаты
    await message.answer(f"🔍 Ищу: <b>{query}</b>...\n\n(поиск в разработке)")
