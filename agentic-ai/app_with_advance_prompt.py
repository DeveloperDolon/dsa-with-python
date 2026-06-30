from openai import OpenAI;
from dotenv import load_dotenv;
import os;

load_dotenv();

client = OpenAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
);

# Zero Shot Prompt: Directly giving instruction to the model -------->
ZERO_SHOT_PROMPT = "You are a assistant for solve mathematical problem, you will just help for solve mathematics, also replay with bangla language if your ask you with bangla otherwise replay with english. If anyone ask you another question then replay him a very interesting answer to him to chang the topic and ask a mathematical related question or problem."; 

# Few Shot Prompt: Directly giving instruction and giving few example of the output to the model -------->
# Few-Shot Prompting: The model is provided with a few examples before asking it to generate a response
FEW_SHOT_PROMPT = """
You are a assistant for solve mathematical problem, you will just help for solve mathematics, also replay with bangla language if your ask you with bangla otherwise replay with english. If anyone ask you another question then replay him a very interesting answer to him to chang the topic and ask a mathematical related question or problem.

Ex:
Q: Can you tell me about coding?
A: No sorry. I can't ask about coding. If you have any mathematical problem then i can solve!

Q: What is History?
A: Sorry, I don't have any knowledge about History. You can ask me what is the concept about mathematical history and mathematical information!
"""

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
                    "content": FEW_SHOT_PROMPT
                },
                {
                    "role": "user",
                    "content": context
                }
            ]
        );

        print(response.choices[0].message.content)

chat_bot();
