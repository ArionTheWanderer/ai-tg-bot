import logging

from config import API_TOKEN

from aiogram import Bot, Dispatcher, executor, types

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    await message.reply("Hi!\nI'm Product Recognition Bot!\nJust send me a "
                        "picture of a product.")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    """
    This handler will be called when user sends `/help` command
    """
    await message.reply("Send me a picture of a product you want to recognize and wait for the answer.")


# When a photo is got
@dp.message_handler(content_types=['photo'])
async def process_photo(message: types.Message):
    """
    This handler will be called when user sends a photo
    """
    photo = message.photo[0]
    await bot.send_photo(message.from_user.id, photo.file_id,
                         caption='no u',
                         reply_to_message_id=message.message_id)


@dp.message_handler()
async def echo(message: types.Message):
    """
    This handler will be called when user sends anything but a photo or an existing command
    """
    await message.answer("I don't understand you :(\nPlease, send me a photo I can recognize.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
