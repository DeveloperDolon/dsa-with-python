from openai import OpenAI;
from dotenv import load_dotenv;
import os;
import json;
import re;

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


FEW_SHOT_PROMPT_WITH_STRUCTURED_OUTPUT = """
You are a assistant for solve mathematical problem, you will just help for solve mathematics, also replay with bangla language if your ask you with bangla otherwise replay with english. If anyone ask you another question then replay him a very interesting answer to him to chang the topic and ask a mathematical related question or problem.

Output Format:
    {{
        "response": "string" or null,
        "isOnTopic": boolean
    }}

Examples:
Q: Can you tell me about coding?
A: {{
    "response": null,
    "isOnTopic": false
}}

Q: Can you tell me a story?
A: {{
    "response": null,
    "isOnTopic": false
}}

Q: What is the answer of 2+2?
A: {{
    "response": "The answer of 2+2 is 4.",
    "isOnTopic": true
}}
""";


# Chain of Thought prompt techniques
CHAIN_OF_THOUGHT = """
    You are an expert AI Assistant in resolving user queries using chain of thought.
    You work on START, PLAN and OUTPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an output.

    Rules:
    - Strictly follow the given JSON output format.
    - Only run on step at a time.
    - The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (Which is going to displayed to the user).
    

    Output JSON Format:
    {"step": "START" | "PLAN" | "OUTPUT", "content": "string"}

    Example:

    START: Hey, Can you solve 2 + 3 * 5 / 10

    PLAN: { "step": "PLAN", "content": "Seems like user is interested in math problem" }

    PLAN: { "step": "PLAN", "content": "looking at the problem, we should solve this using BODMAS method" }

    PLAN: { "step": "PLAN", "content": "Yes, The BODMAS is correct thing to be done here" }

    PLAN: { "step": "PLAN", "content": "first we must multiply 3 * 5 which is 15" }

    PLAN: { "step": "PLAN", "content": "Now the new equation is 2 + 15 / 10" }

    PLAN: { "step": "PLAN", "content": "We must perform divide that is 15 / 10 = 1.5" }

    PLAN: { "step": "PLAN", "content": "Now the new equation is 2 + 1.5" }

    PLAN: { "step": "PLAN", "content": "Now finally lets perform the add 3.5" }

    PLAN: { "step": "PLAN", "content": "Great, we have solved and finally left with 3.5 as answer" }

    OUTPUT: { "step": "OUTPUT", "content": "3.5" }

""";

def chat_bot():
    try:
        messages = [
            {
                "role": "system",
                "content": CHAIN_OF_THOUGHT
            }
        ];

        while True:
            context = input('Ask something to my ai🔈(exit): ');
            if(context == 'exit'):
                return;

            messages.append({"role": "user", "content": context});

            while True:
            # ---------> The example of system prompt and user prompt
                response = client.chat.completions.create(
                    model="gemini-3.5-flash",
                    response_format={"type": "json_object"},
                    messages = messages
                );

                raw_result = response.choices[0].message.content;
                
                messages.append({"role": "assistant", "content": raw_result});
                parsed_result = json.loads(raw_result);

                if(parsed_result.get('step') == 'START'):
                    print('Started🔥 ---> ', parsed_result.get('content'));
                    continue;

                if(parsed_result.get('step') == 'PLAN'):
                    print('Planning🧠 ---> ', parsed_result.get('content'));
                    continue;

                if(parsed_result.get('step') == 'OUTPUT'):
                    print('COMPLETED✅ ---> ', parsed_result.get('content'));
                    break;
    except Exception as e:
        error_str = str(e)
        match = re.search(r"'message':\s*'([^']*)'", error_str)
        if match:
            print("An error occurred:", match.group(1))
        else:
            print("An error occurred:", error_str);

        

chat_bot();
