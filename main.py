import os
import openai
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

load_dotenv()

# bot = Bot(token=os.getenv("6144904939:AAEUJWw9gRzxYHAFmB0yhvzs5MynlFvwXT4"))
# dp = Dispatcher(bot)

# openai.api_key = os.getenv("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")

TOKEN='6144904939:AAEUJWw9gRzxYHAFmB0yhvzs5MynlFvwXT4'
# dp = Dispatcher(bot)

OPENAI_API_KEY='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'

@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply('Hello! I\'m a GPT chat bot. Ask me something.')


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
    executor.start_polling(dp)
