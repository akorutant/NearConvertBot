import settings
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.markdown import bold
from getnearinfo import NearInfo

bot = Bot(token=settings.TOKEN)
dp = Dispatcher(bot)
get_info = NearInfo(settings.api_key)


@dp.message_handler(commands=["start"])
async def process_start_command(message: types.Message):
    await message.reply("Привет! Я бот для получения актуального курса криптовалюты NEAR в USD, BYN и RUB.")


@dp.message_handler(commands=['rate', 'курс'])
async def process_course_command(message: types.Message):
    near = get_info.get_near_info()
    await message.reply(bold("Курс NEAR на данный момент\n\n") +
                        f"{near[2]['asset_id_quote']}: {near[2]['rate']}\n"
                        f"{near[0]['asset_id_quote']}: {near[0]['rate']}\n"
                        f"{near[1]['asset_id_quote']}: {near[1]['rate']}", parse_mode='MARKDOWN')


@dp.message_handler()
async def process_command_catch_messages(message: types.Message):
    if message.text.lower() == 'курс':
        near = get_info.get_near_info()
        await message.reply(bold("Курс NEAR на данный момент\n\n") +
                            f"{near[2]['asset_id_quote']}: {near[2]['rate']}\n"
                            f"{near[0]['asset_id_quote']}: {near[0]['rate']}\n"
                            f"{near[1]['asset_id_quote']}: {near[1]['rate']}", parse_mode='MARKDOWN')

if __name__ == '__main__':
    executor.start_polling(dp)
