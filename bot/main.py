import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot.config import settings
from bot.handlers import start, music, playlists, shazam, subscription

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main() -> None:
    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(music.router)
    dp.include_router(playlists.router)
    dp.include_router(shazam.router)
    dp.include_router(subscription.router)

    logger.info("Дзынь бот запущен 🎵")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
