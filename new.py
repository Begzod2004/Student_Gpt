# import os
# import openai
# from aiogram import Bot, Dispatcher, executor, types
# from dotenv import load_dotenv

# load_dotenv()

# bot_token = "6144904939:AAEUJWw9gRzxYHAFmB0yhvzs5MynlFvwXT4"
# openai.api_key = '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'

# bot = Bot(token=bot_token) 
# dp = Dispatcher(bot)


# @dp.message_handler(commands=['start', 'help'])
# async def welcome(message: types.Message):
#     await message.reply('Hello! I\'m a GPT chat bot. Ask me something.')


# @dp.message_handler()
# async def gpt(message: types.Message):
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=message.text,
#         temperature=0.5,
#         max_tokens=1024,
#         top_p=1,
#         frequency_penalty=0.0,
#         presence_penalty=0.0
#     )
#     await message.reply(response.choices[0].text)


# if __name__ == "__main__":
#     executor.start_polling(dp, skip_updates=True)





import os
import openai
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

load_dotenv()

openai.api_key = "O'zingizning api key YOZING"
bot_token = "ozingizning bot token YOZING"

bot = Bot(token=bot_token) 
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Salom! Men GPT chat botman. Menga savol berishingiz mumkin.")

@dp.message_handler()
async def gpt(message: types.Message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    await message.reply(response.choices[0].text)

if __name__ == "__main__":
    try:
        executor.start_polling(dp, skip_updates=True)
    except Exception as e:
        print(f"Xato yuz berdi: {e}")
