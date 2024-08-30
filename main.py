# Required Library:
# pip install g4f

import asyncio
import platform

if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from g4f.client import Client

class Chatbot:
    def __init__(self):
        self.client = Client()
        self.messages = []

    def start(self):
        print("Welcome to the Chatbot! You can type 'exit' to quit.")
        while True:
            user_input = input("You: ")
            if user_input.strip().lower() == "exit":
                print("Goodbye!")
                break

            response = self.get_chatbot_response(user_input)
            print(f"Chatbot: {response}")

    def get_chatbot_response(self, user_input):
        try:
            self.messages.append({"role": "user", "content": user_input})

            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=self.messages,
                language="en"
            )
            chatbot_response = response.choices[0].message.content
            self.messages.append({"role": "assistant", "content": chatbot_response})
            return chatbot_response

        except Exception as e:
            print(f"Error: {e}")
            return "Sorry, something went wrong."

if __name__ == '__main__':
    bot = Chatbot()
    bot.start()
