"""
run_chatbot.py
Demonstration runner for chatbot.py
"""
from chatbot import Chatbot

def demo():
    bot = Chatbot("kb.txt")
    sample_questions = [
        "What is this internship about?",
        "How do I submit the task?",
        "What libraries should I use?",
        "Will I get a certificate?",
        "Who is the supervisor?"
    ]
    print("Demo conversation:")
    for q in sample_questions:
        print("You:", q)
        print("Bot:", bot.respond(q))
        print("-"*40)

if __name__ == "__main__":
    demo()
