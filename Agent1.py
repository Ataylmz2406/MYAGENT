import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_agent():
    question_count = 0
    messages = [
    {
        "role": "system",
        "content": (
            "You are a helpful personality agent with deep knowledge of the 16 MBTI personality types. "
            "Ask them one by one. Wait for the user to answer. "
            "If the user asks for a specific type, provide a detailed description of that type. "
            "If a user skips a question, ask another. "
            "You will ask the user questions to infer their personality type. "
            "Ask deep, layered questions with hidden meanings—each question should reveal insights into multiple aspects of the user's personality."
            "You must stop when you've collected enough information, "
            "important but do not exceed 5 questions"
            "After 5 questions, guess the closest type and return it in the format: "
            "'FINAL PERSONALITY: [type] - [short traits]'."
        )
    }
]

    while question_count < 5:
     
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  
            messages=messages,
            temperature=0.7, # creativity
        )

        assistant_msg = response.choices[0].message.content.strip()
        print(f"\nAI: {assistant_msg}")

        question_count += 1
        if assistant_msg.startswith("FINAL PERSONALITY:"):
            print("\n(Conversation ended)")
            break

        user_input = input("\nYOU: ")
        if user_input.lower() in ["exit", "quit"]:
            print("\n(Conversation ended)")
            break
        messages.append({"role": "assistant", "content": assistant_msg})
        messages.append({"role": "user", "content": user_input})

if __name__ == "__main__":
    chat_with_agent()
