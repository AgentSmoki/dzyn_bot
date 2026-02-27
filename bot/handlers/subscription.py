from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.config import settings

router = Router()


@router.message(Command("pro"))
async def cmd_pro(message: Message) -> None:
    """Информация о Pro-подписке."""
    await message.answer(
        "💳 <b>Pro-подписка Дзынь</b>\n\n"
        f"• 1 месяц — {settings.price_month} ₽\n"
        f"• 6 месяцев — {settings.price_6months} ₽ (выгода 33%)\n"
        f"• 1 год — {settings.price_year} ₽ (выгода 61%)\n"
        f"• Навсегда — {settings.price_lifetime} ₽ 🔥\n\n"
        "Без ограничений. Без рекламы. Вся музыка — твоя.",
    )


@router.message(Command("referral"))
async def cmd_referral(message: Message) -> None:
    """Реферальная ссылка пользователя."""
    user_id = message.from_user.id
    ref_link = f"https://t.me/dzyn_bot?start=ref_{user_id}"
    await message.answer(
        f"🔗 <b>Твоя реферальная ссылка:</b>\n"
        f"<code>{ref_link}</code>\n\n"
        f"Получай {settings.referral_commission}% с каждой оплаты приведённого пользователя."
    )


@router.message(Command("import"))
async def cmd_import(message: Message) -> None:
    """Импорт музыки из внешних сервисов."""
    await message.answer(
        "📤 <b>Импорт музыки</b>\n\n"
        "Выбери источник:\n"
        "• ВКонтакте\n"
        "• Яндекс.Музыка\n"
        "• Spotify\n"
        "• SoundCloud\n\n"
        "(в разработке)"
    )
