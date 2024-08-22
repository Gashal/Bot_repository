from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message


BOT_TOKEN = ''

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def proccess_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


async def proccess_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ я пришлю тебе твое сообщение'
    )


async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
        #print(message.model_dump_json(indent=4, exclude_none=True)) Для вывода прямо в терминал апдейта в json формате с отступами
    except TypeError:
        await message.reply(
            text='Данный тип апдейтов не поддерживается методом send_copy'
        )


dp.message.register(proccess_start_command, Command(commands='start'))
dp.message.register(proccess_help_command, Command(commands='help'))
dp.message.register(send_echo)

if __name__ == '__main__':
    dp.run_polling(bot)