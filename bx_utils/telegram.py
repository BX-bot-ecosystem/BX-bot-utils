from telegram import Update
from telegram.ext import ContextTypes
import time
class Vcheck:
    @staticmethod
    def telegram():
        from telegram import __version__ as TG_VER
        try:
            from telegram import __version_info__
        except ImportError:
            __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]
        
        if __version_info__ < (20, 0, 0, "alpha", 1):
            raise RuntimeError(
                f"This example is not compatible with your current PTB version {TG_VER}. To view the "
                f"{TG_VER} version of this example, "
                f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
            )


class Message:
    @staticmethod
    async def send_message(update: Update, context: ContextTypes.DEFAULT_TYPE, text, parse_mode=None, reply_markup=None):
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
        time.sleep(len(text)/140)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode=parse_mode, reply_markup=reply_markup) 