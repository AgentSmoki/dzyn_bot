from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("playlists"))
async def cmd_playlists(message: Message) -> None:
    """Список плейлистов пользователя."""
    # TODO: загрузить из БД
    await message.answer(
        "📋 <b>Мои плейлисты</b>\n\n"
        "У тебя пока нет плейлистов.\n"
        "После скачивания трека нажми «Добавить в плейлист»."
    )
