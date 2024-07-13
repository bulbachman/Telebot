from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from config import BOT_TOKEN
from messages import MESSAGES

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот был успешно запущен!')


kb = ReplyKeyboardMarkup(resize_keyboard=True)
description_button = KeyboardButton('/description')
photo_button = KeyboardButton('/photo')
give_button = KeyboardButton('/give')
kb.add(description_button).insert(photo_button).add(give_button)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(MESSAGES['help'], parse_mode='HTML', reply_markup=kb)


@dp.message_handler(commands=['start'])
async def help_command(message: types.Message):
    await message.answer(f'''<i>{MESSAGES['start']}</i>''', parse_mode='HTML')
    await message.delete()


@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await message.reply(MESSAGES['description'])


@dp.message_handler(commands=['give'])
async def send_sticker(message: types.Message):
    await message.answer('Смотри какой динозавр смешной' + '😂')
    await bot.send_sticker(message.from_user.id,
                           sticker='CAACAgIAAxkBAAEHw51j7hZBVTvl2e4zYQSPNCw0CnwN9wACRwMAArVx2gY1e3PZAAGLHaQuBA')
    await message.delete()


@dp.message_handler(commands=['photo'])
async def send_image(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="https://steamuserimages-a.akamaihd.net/ugc/416937800340621455/2BCCCF9EE68DB958F41299F20004571D9F52F69D/?imw=512&amp;imh=395&amp;ima=fit&amp;impolicy=Letterbox&amp;imcolor=%23000000&amp;letterbox=true")
    await message.delete()


@dp.message_handler(commands=['location'])
async def send_place(message: types.Message):
    await bot.send_location(chat_id=message.from_user.id, latitude=53.848218, longitude=27.509881)
    await message.delete()


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
    # await bot.send_message(chat_id=message.from_user.id, text=message.text)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
