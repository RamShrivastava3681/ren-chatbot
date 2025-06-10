import nltk
import random
import json
import os
import ast
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from app.knowledge_base import knowledge_base, code_snippets
from app.quiz_data import quiz_bank

nltk.download('punkt')

# Prepare NLP data
questions = list(knowledge_base.keys())
answers = list(knowledge_base.values())
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

# Greetings
greetings = ["hi", "hello", "hey", "good morning", "good evening", "yo", "how are you", "what's up", "sup", "morning", "evening"]
greeting_responses = {
    "morning": [
        "Good morning! 🌞 Ready to kickstart your day with some Python? 🐍✨",
        "Rise and shine! Time to learn Python~ ☕💻",
        "Good morning, Senpai! Time for some coding magic? 😎",
    ],
    "afternoon": [
        "Good afternoon! ☀️ How’s the day going? Ready for more Python? 🐍",
        "Afternoon, Senpai! Let’s dive into some code! 💻",
        "Hey there, it’s the afternoon! Python time? 😎",
    ],
    "evening": [
        "Good evening! 🌙 How was your day? Ready to code? 💻",
        "Evening, Senpai! Let’s wrap up the day with some Python practice. 📘",
        "Evening! 🌓 Let’s take a break and get some coding done! 💻",
    ],
    "default": [
        "Hiya~ I'm Ren! Need help with Python or just wanna talk? 🤖💬",
        "Oh, it’s you… Need something, Senpai? 🙄",
        "Hello there! Ask me anything about Python 🐍✨",
        "You again? Hmph… I guess I’ll help. 😤",
        "Yo~ Need some code magic? 🪄💻",
        "Ren's here and fully operational! What can I do for you today?",
    ]
}

# Get current time of day
def get_time_of_day():
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        return "morning"
    elif 12 <= current_hour < 17:
        return "afternoon"
    elif 17 <= current_hour < 22:
        return "evening"
    else:
        return "default"

# 🔍 Code Explanation
def explain_code(code):
    try:
        tree = ast.parse(code)
        explanations = []

        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                explanations.append("📝 This line assigns a value to a variable.")
            elif isinstance(node, ast.For):
                explanations.append("🔁 This is a for-loop iterating over a sequence.")
            elif isinstance(node, ast.If):
                explanations.append("🔍 This is an if-statement checking a condition.")
            elif isinstance(node, ast.FunctionDef):
                explanations.append(f"🛠️ This defines a function named '{node.name}'.")
            elif isinstance(node, ast.Call):
                explanations.append("📞 This line calls a function.")
            elif isinstance(node, ast.Expr):
                explanations.append("📄 This is an expression line.")
            elif isinstance(node, ast.While):
                explanations.append("🔄 This is a while-loop.")
            elif isinstance(node, ast.Return):
                explanations.append("🎁 This line returns a value from a function.")
        
        if not explanations:
            return "Hmm… I parsed it, but it’s either too short or too cryptic, baka! 😠"

        return "\n".join(set(explanations))

    except Exception as e:
        return f"Ugh… I couldn't understand that code. Is it valid Python? 😤\n\nError: {str(e)}"

# Quiz session state management
quiz_session = {
    "active": False,
    "level": None,
    "questions": [],
    "current_index": 0,
    "score": 0,
    "num_questions": 3
}

def start_quiz(level="easy", num_questions=3):
    if level not in quiz_bank:
        return "I only have quiz levels for: easy, medium, and hard. Pick one, dummy~ 😤"

    quiz_session["active"] = True
    quiz_session["level"] = level
    quiz_session["questions"] = random.sample(quiz_bank[level], min(num_questions, len(quiz_bank[level])))
    quiz_session["current_index"] = 0
    quiz_session["score"] = 0
    quiz_session["num_questions"] = num_questions

    return format_question(quiz_session["questions"][0], 1)

def format_question(question_obj, question_number):
    result = [f"\n📘 Question {question_number}: {question_obj['question']}"]
    result.append(f"A: {question_obj['options'][0]}")
    result.append(f"B: {question_obj['options'][1]}")
    result.append(f"C: {question_obj['options'][2]}")
    result.append(f"D: {question_obj['options'][3]}")
    return "\n".join(result)

def process_quiz_answer(user_input, correct_answer):
    if user_input.lower() == correct_answer.lower():
        return "Correct! Ren approves! 💪 Keep going, Senpai! 😤"
    else:
        return f"Wrong answer! The correct answer was {correct_answer}. 😤 But keep trying, Senpai. You'll get better!"

# 🧠 History
HISTORY_FILE = "app/history.json"

def save_to_history(question, response):
    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "w") as f:
            json.dump([], f)

    with open(HISTORY_FILE, "r") as f:
        history = json.load(f)

    history.append({"Q": question, "A": response})
    with open(HISTORY_FILE, "w") as f:
        json.dump(history[-10:], f)  # Keep only last 10 entries

def get_history():
    if not os.path.exists(HISTORY_FILE):
        return "No history yet, baka."
    
    with open(HISTORY_FILE, "r") as f:
        history = json.load(f)

    result = ["📜 Your last questions:"]
    for i, entry in enumerate(history):
        result.append(f"{i+1}. {entry['Q']} → {entry['A']}")
    
    return "\n".join(result)

# 💬 Main response handler
def get_response(user_input):
    raw_input = user_input.strip()
    user_input = raw_input.lower()

    # Greeting
    if any(greet in user_input for greet in greetings):
        time_of_day = get_time_of_day()
        response = random.choice(greeting_responses.get(time_of_day, greeting_responses["default"]))
        save_to_history(raw_input, response)
        return response

    # History
    if user_input in ["history", "what did i ask", "show my history"]:
        return get_history()

    # Explain code
    if user_input.startswith("explain this code:"):
        code = raw_input[len("explain this code:"):].strip()
        response = explain_code(code)
        save_to_history(raw_input, response)
        return response

    # Quiz mode
    if "quiz me" in user_input or "start quiz" in user_input:
        if "easy" in user_input:
            level = "easy"
        elif "medium" in user_input:
            level = "medium"
        elif "hard" in user_input:
            level = "hard"
        else:
            level = "easy"
        response = start_quiz(level)
        save_to_history(raw_input, "Started quiz.")
        return response

    # Answer quiz question
    if quiz_session["active"] and user_input.lower() in ["a", "b", "c", "d"]:
        current_question = quiz_session["questions"][quiz_session["current_index"]]
        correct_answer = current_question["answer"].lower()
        response = process_quiz_answer(user_input, correct_answer)
        quiz_session["current_index"] += 1
        if user_input.lower() == correct_answer:
            quiz_session["score"] += 1

        if quiz_session["current_index"] < len(quiz_session["questions"]):
            next_question = quiz_session["questions"][quiz_session["current_index"]]
            response += "\n" + format_question(next_question, quiz_session["current_index"] + 1)
        else:
            total = len(quiz_session["questions"])
            score = quiz_session["score"]
            percentage = (score / total) * 100
            if percentage == 100:
                remark = "🎉 Perfect!"
            elif percentage >= 80:
                remark = "🥳 Great job!"
            elif percentage >= 50:
                remark = "🙂 You passed!"
            else:
                remark = "🙁 Try again!"
            response += f"\n\n--- Quiz Finished ---\nYour Score: {score}/{total} ({percentage:.2f}%)\n{remark}"
            quiz_session["active"] = False

        save_to_history(raw_input, response)
        return response

    # Code snippet match
    for key in code_snippets:
        if key in user_input:
            explanation = knowledge_base.get(f"how to {key}", "")
            response = f"{explanation}\n\nHere’s how you do it in Python:\n\n{code_snippets[key]}"
            save_to_history(raw_input, response)
            return response

    # NLP similarity
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, X)
    score = similarity.max()

    if score < 0.3:
        response = "Ugh… I don’t get it. Maybe ask that a different way, okay? 😤"
    else:
        index = similarity.argmax()
        response = answers[index]

    save_to_history(raw_input, response)
    return response

def grade_quiz(user_answers, difficulty):
    questions = quiz_bank[difficulty]
    correct = 0
    total = len(questions)

    print(f"\n--- {difficulty.capitalize()} Quiz Results ---")
    for i, q in enumerate(questions):
        user_answer = user_answers.get(i, "").upper()
        correct_answer = q["answer"]
        status = "✅ Correct" if user_answer == correct_answer else f"❌ Incorrect (Correct: {correct_answer})"
        print(f"Q{i+1}: {q['question']}\nYour Answer: {user_answer} - {status}\n")
        if user_answer == correct_answer:
            correct += 1

    score = correct
    percentage = (score / total) * 100
    print(f"Final Score: {score}/{total} ({percentage:.2f}%)")

    if percentage == 100:
        remark = "🎉 Perfect!"
    elif percentage >= 80:
        remark = "🥳 Great job!"
    elif percentage >= 50:
        remark = "🙂 You passed!"
    else:
        remark = "🙁 Try again!"

    print(f"Remark: {remark}")
