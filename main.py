import settings
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.markdown import bold
from getnearinfo import NearInfo
from googletrans import Translator

bot = Bot(token=settings.TOKEN)
dp = Dispatcher(bot)
get_info = NearInfo(settings.api_key)
translator = Translator()


@dp.message_handler(commands=["start"])
async def process_start_command(message: types.Message):
    await message.reply("Привет! Я бот для получения актуального курса криптовалюты NEAR в USD, BYN и RUB.")


@dp.message_handler(commands=['rate', 'курс'])
async def process_course_command(message: types.Message):
    near = get_info.get_near_info()
    try:
        await message.reply(bold("Курс NEAR на данный момент\n\n") +
                            f"{near['rates'][2]['asset_id_quote']}: {near['rates'][2]['rate']}\n"
                            f"{near['rates'][0]['asset_id_quote']}: {near['rates'][0]['rate']}\n"
                            f"{near['rates'][1]['asset_id_quote']}: {near['rates'][1]['rate']}",
                            parse_mode='MARKDOWN')
    except:
        near_error_rus = translator.translate(near['error'], dest='ru', src='en').text
        await message.reply(f"{near['error']}\n\nПеревод: {near_error_rus}")


@dp.message_handler()
async def process_command_catch_messages(message: types.Message):
    if message.text.lower() == 'курс':
        near = get_info.get_near_info()
        try:
            await message.reply(bold("Курс NEAR на данный момент\n\n") +
                                f"{near['rates'][2]['asset_id_quote']}: {near['rates'][2]['rate']}\n"
                                f"{near['rates'][0]['asset_id_quote']}: {near['rates'][0]['rate']}\n"
                                f"{near['rates'][1]['asset_id_quote']}: {near['rates'][1]['rate']}",
                                parse_mode='MARKDOWN')
        except:
            near_error_rus = translator.translate(near['error'], dest='ru', src='en').text
            await message.reply(f"{near['error']}\n\nПеревод: {near_error_rus}")

if __name__ == '__main__':
    executor.start_polling(dp)
