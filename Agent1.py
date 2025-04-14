import os
from openai import OpenAI
from dotenv import load_dotenv

# Load your API key from .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_agent():
    question_count = 0
    messages = [
    {
        "role": "system",
        "content": (
            "You are a helpful personality agent with deep knowledge of the 16 MBTI personality types. "
            "Ask them one by one wait for the user to answer. "
            "if the user asks for a specific type, you will provide a detailed description of that type. "
            "if a user skips a question ask another question. "
            "You will ask the user questions to infer their personality type. "
            "Make the questions deep and make it so that each question has hidden meanings."
            "You must stop when you've collected enough information, "
            "important but do not exceed 5 questions"
            "after 5 questions guess the closest type and give that type. When you're done, reply with 'FINAL PERSONALITY:' followed by their type and traits."
        )
    }
]

    while question_count <= 5:
     
        response = client.chat.completions.create(
            model="gpt-4o",  # or "gpt-3.5-turbo"
            messages=messages,
            temperature=0.7, # creativity
        )

        assistant_msg = response.choices[0].message.content.strip()
        print(f"\nAI: {assistant_msg}")

        question_count += 1
        if question_count >= 6 or assistant_msg.startswith("FINAL PERSONALITY:"):
            print("\n(Conversation ended)")
            break

        user_input = input("\nYOU: ")
        messages.append({"role": "assistant", "content": assistant_msg})
        messages.append({"role": "user", "content": user_input})

if __name__ == "__main__":
    chat_with_agent()
