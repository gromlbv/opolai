import ollama
import asyncio

async def main():
    def responsefunc(text):
        response = ollama.chat(model='command-r', messages=[
          {
            'role': 'user',
            'content': text,
          },
        ])
        print(response['message']['content'])

    responsefunc("meow")
    await asyncio.sleep(1)
    print('... World!')

asyncio.run(main())