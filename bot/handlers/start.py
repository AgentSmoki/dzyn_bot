from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer(
        "🎵 <b>Дзынь</b> — вся твоя музыка в одном месте\n\n"
        "Что умею:\n"
        "🔍 /search — найти трек по названию\n"
        "🎙️ Отправь голосовое — распознаю как Шазам\n"
        "📋 /playlists — мои плейлисты\n"
        "📤 /import — импорт из VK, Яндекс, Spotify\n"
        "💳 /pro — Pro-подписка\n"
        "🔗 /referral — реферальная ссылка\n"
    )


@router.message(Command("help"))
async def cmd_help(message: Message) -> None:
    await message.answer(
        "ℹ️ <b>Помощь</b>\n\n"
        "Напиши название трека или исполнителя — пришлю варианты.\n"
        "Запиши голосовое сообщение — распознаю трек (как Шазам).\n\n"
        "Команды:\n"
        "/search — поиск\n"
        "/playlists — плейлисты\n"
        "/import — импорт музыки\n"
        "/pro — подписка\n"
        "/referral — реферальная программа"
    )
