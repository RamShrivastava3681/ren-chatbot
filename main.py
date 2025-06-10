from app.bot import get_response

print("🤖 Ren: Hello! I’m Ren, your Python tutor. Ask me anything about Python! (type 'exit' to quit)")

while True:
    user_input = input("👤 You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("🤖 Ren: Goodbye and happy coding, Senpai! 🐍✨")
        break
    response = get_response(user_input)
    print("🤖 Ren:", response)

