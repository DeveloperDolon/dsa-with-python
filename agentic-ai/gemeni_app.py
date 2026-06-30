from google import genai
from google.genai.types import HttpOptions
from dotenv import load_dotenv;

load_dotenv();

client = genai.Client(http_options=HttpOptions(api_version="v1"))
def chat_bot():
    while True:
        context = input('Ask something to my ai🔈(exit): ');
        if(context == 'exit'):
            return;
    
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=context,
        )
        print(response.text)

chat_bot();
