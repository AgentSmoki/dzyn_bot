from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message(lambda m: m.voice is not None)
async def handle_voice(message: Message) -> None:
    """Принимает голосовое сообщение и распознаёт трек (Шазам-функция)."""
    await message.answer("🎙️ Слушаю... Распознаю трек...")
    # TODO: скачать voice, отправить в AudD API, вернуть результат
    await message.answer("🔎 Распознавание в разработке. Скоро заработает!")
