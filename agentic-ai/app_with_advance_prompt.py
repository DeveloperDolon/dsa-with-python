from openai import OpenAI;
from dotenv import load_dotenv;
import os;

load_dotenv();

client = OpenAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
);

def chat_bot():
    while True:
        context = input('Ask something to my ai🔈(exit): ');
        if(context == 'exit'):
            return;

        # ---------> The example of system prompt and user prompt
        response = client.chat.completions.create(
            model="gemini-3.5-flash",
            messages=[
                {   "role": "system", 
                    "content": "You are a assistant for solve mathematical problem, you will just help for solve mathematics, also replay with bangla language. If anyone ask you another question then replay him a very interesting answer to him to chang the topic and ask a mathematical related question or problem."
                },
                {
                    "role": "user",
                    "content": context
                }
            ]
        );

        print(response.choices[0].message.content)

chat_bot();
