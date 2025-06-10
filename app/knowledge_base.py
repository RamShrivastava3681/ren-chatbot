# Full knowledge base for Ren – Python tutor + code writer 💡✨

knowledge_base = {
    # 🔰 Basics
    "what is python": "Python is a high-level, interpreted programming language known for its simplicity and readability.",
    "how to declare a variable": "Just assign a value to a name. Example: name = 'Ren'",
    "how to print something": "Use the print() function. Example: print('Hello, world!')",
    "how to take input": "Use the input() function. Example: name = input('Enter your name: ')",

    # 📦 Data Types
    "what are data types in python": "Common types: int, float, str, list, tuple, dict, set, bool.",
    "what is a list": "Ordered, mutable collection. Example: my_list = [1, 2, 3]",
    "what is a tuple": "Ordered, immutable collection. Example: my_tuple = (1, 2, 3)",
    "what is a dictionary": "Key-value pairs. Example: my_dict = {'name': 'Ren'}",
    "what is a set": "Unordered collection of unique elements. Example: my_set = {1, 2, 3}",

    # 🔁 Control Flow
    "what is if else": "Used for conditional execution. Example:\nif x > 0:\n  print('Positive')\nelse:\n  print('Negative')",
    "how to use for loop": "Use range() to loop over numbers. Example: for i in range(5): print(i)",
    "how to use while loop": "Repeats while a condition is True. Example:\ni = 0\nwhile i < 5:\n  print(i)\n  i += 1",
    "what is break": "Used to exit a loop early.",
    "what is continue": "Skips the current iteration and continues to the next.",

    # 🧩 Functions
    "how to define a function": "Use the def keyword. Example:\ndef greet():\n  print('Hello!')",
    "how to return a value": "Use return. Example:\ndef square(x): return x * x",
    "what is recursion": "A function calling itself. Example:\ndef fact(n): return 1 if n==0 else n*fact(n-1)",

    # 🧱 Object-Oriented Programming
    "what is a class": "A class is a blueprint for objects. It defines properties and behaviors.",
    "how to define a class": "Example:\nclass Dog:\n  def __init__(self, name):\n    self.name = name",
    "what is inheritance": "Inheritance allows one class to acquire properties of another. Example:\nclass Cat(Animal): pass",
    "what is self": "`self` refers to the instance of the class.",
    "what is __init__": "`__init__` is a constructor method that gets called when a new object is created.",

    # 📁 File Handling
    "how to read a file": "Use open() and read(). Example:\nwith open('file.txt', 'r') as f:\n  print(f.read())",
    "how to write to a file": "Use write mode. Example:\nwith open('file.txt', 'w') as f:\n  f.write('Hello')",
    "what is with open": "It automatically closes the file after use. Safer than manually closing.",

    # ⚙️ Advanced
    "what is lambda": "A lambda is a small anonymous function. Example: lambda x: x*x",
    "what is map function": "Applies a function to every item in an iterable. Example: map(str.upper, ['a', 'b'])",
    "what is filter": "Filters items based on a function. Example: filter(lambda x: x>0, [-1, 2, 3])",
    "what is list comprehension": "A concise way to build lists. Example: [x for x in range(5) if x%2==0]",
    "what is try except": "Used to catch and handle exceptions (errors).",
    "what is module": "A Python file with reusable code you can import.",
    "how to install a library": "Use pip. Example: pip install numpy",

    # 💬 Help
    "help": "Ask me anything about Python! Try 'how to write a function', 'reverse a string', or 'code to read file'.",
    "topics": "I know: Variables, Data Types, Loops, Functions, Classes, Files, OOP, Exceptions, Lambdas, and more!"
}

# 💻 Code Snippets – Ren writes too! 😤
code_snippets = {
    "reverse a string": '''# Reverse a string
text = "hello"
reversed_text = text[::-1]
print(reversed_text)  # output: 'olleh'
''',

    "for loop example": '''# Print numbers 0 to 4
for i in range(5):
    print(i)
''',

    "read file": '''# Read a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
''',

    "list comprehension": '''# Create a list of squares
squares = [x**2 for x in range(10)]
print(squares)
''',

    "function example": '''# Define and call a function
def greet(name):
    print(f"Hello, {name}!")

greet("Ren")
''',

    "fibonacci sequence": '''# Generate Fibonacci sequence
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fib(10)
''',

    "write to file": '''# Write to a file
with open("notes.txt", "w") as file:
    file.write("Ren was here!")
''',

    "class example": '''# Define a simple class
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hi, I’m {self.name}!")

s = Student("Ren")
s.greet()
''',

    "try except example": '''# Handle division error
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Oops! Can’t divide by zero.")
'''
}
knowledge_base = {
    # 🔰 Python Basics
    "what is python": "Python is an interpreted, high-level, dynamically typed programming language great for beginners and pros alike.",
    "why use python": "Because of its readability, vast libraries, community support, and applications in AI, ML, web, automation, and more.",
    "how to install python": "Download from python.org and follow the installer. Or use a package manager like brew or apt.",
    "how to run python code": "Use `python filename.py` in terminal or an IDE like VS Code or Jupyter.",
    "how to declare a variable": "Assign a value using `=`. No need to declare type. Ex: `name = 'Ren'`.",
    "how to comment": "Use `#` for single-line and `'''...'''` or `\"\"\"...\"\"\"` for multi-line comments.",
    "how to print something": "Use print(). Example: `print('Hi Ren')`.",
    "how to take input": "Use input(). Example: `name = input('Enter name: ')`.",
    "python indentation": "Python uses indentation to define blocks. Typically 4 spaces.",

    # 📦 Data Types
    "data types in python": "Common types include: int, float, bool, str, list, tuple, dict, set, NoneType.",
    "type casting": "Convert between types. Example: `int('5')`, `str(42)`.",
    "check data type": "Use `type(x)` to check a variable’s type.",
    "string operations": "Concatenation, slicing, length: `s + s2`, `s[:3]`, `len(s)`.",
    "list methods": "Common ones: append(), pop(), insert(), sort(), reverse().",
    "dictionary methods": "get(), keys(), values(), items(), update().",
    "set operations": "union(), intersection(), difference(), add(), remove().",

    # 🔁 Control Flow
    "conditional statements": "`if`, `elif`, `else` used for decision making.",
    "logical operators": "`and`, `or`, `not` for combining conditions.",
    "comparison operators": "`==`, `!=`, `>`, `<`, `>=`, `<=`.",
    "nested loops": "You can nest `for` and `while` loops inside each other.",
    "loop else block": "`else` after loop runs if no break was hit.",

    # 🧩 Functions
    "parameters vs arguments": "Parameters are variables in function definition; arguments are actual values passed.",
    "default parameters": "You can assign default values in function. Ex: `def greet(name='User'):`",
    "keyword arguments": "Call with `key=value` format. Example: `greet(name='Ren')`.",
    "variable length arguments": "`*args` for multiple positional and `**kwargs` for keyword arguments.",

    # 🧱 Object-Oriented Programming
    "oop concepts": "Class, Object, Inheritance, Polymorphism, Encapsulation, Abstraction.",
    "dunder methods": "Special methods like `__init__`, `__str__`, `__len__`, `__getitem__`.",
    "class vs object": "A class is a blueprint, an object is an instance.",
    "classmethod vs staticmethod": "classmethod gets class as first arg; staticmethod is regular function in a class.",

    # 🧹 Exception Handling
    "try except finally": "Use `finally` to run code regardless of exceptions.",
    "raise exception": "Use `raise` to manually throw an exception. Example: `raise ValueError('Wrong!')`.",
    "custom exception": "Define a class inheriting from Exception to make custom errors.",

    # 🔀 Iterators and Generators
    "what is an iterator": "Any object with `__next__()` and `__iter__()` methods.",
    "what is a generator": "A function that yields values using `yield` instead of return.",
    "difference between return and yield": "`return` ends function, `yield` pauses and resumes.",

    # 🧰 Built-in Functions
    "common built-ins": "len(), type(), range(), sum(), max(), min(), input(), print(), list(), dict(), set().",
    "enumerate function": "Returns index and item. Ex: `for i, val in enumerate(lst)`.",
    "zip function": "Combines multiple iterables. Ex: `zip(list1, list2)`.",

    # 🧮 Math and Random
    "math module": "Provides sqrt, ceil, floor, sin, cos, etc.",
    "random module": "random(), randint(), choice(), shuffle(), sample().",

    # 🧰 Modules and Packages
    "how to import module": "`import module` or `from module import function`.",
    "create module": "Just save functions in a `.py` file and import it.",
    "standard libraries": "os, sys, math, datetime, re, json, random, itertools, collections.",

    # 📁 File Handling
    "file modes": "'r' (read), 'w' (write), 'a' (append), 'rb', 'wb' (binary).",
    "read line by line": "Use `for line in file:` inside a with block.",

    # 🧠 Machine Learning Basics
    "what is machine learning": "ML is a subset of AI where computers learn patterns from data to make predictions.",
    "types of ml": "Supervised, Unsupervised, Semi-supervised, and Reinforcement Learning.",
    "what is supervised learning": "ML where the model learns from labeled data.",
    "what is unsupervised learning": "ML where the model finds patterns in unlabeled data.",
    "what is overfitting": "When a model learns the noise in training data and performs poorly on new data.",
    "what is underfitting": "When a model is too simple to capture the underlying pattern.",
    "train vs test data": "Train data builds the model, test data evaluates it.",
    "what is sklearn": "A Python library for ML, includes tools for classification, regression, clustering, etc.",
    "what is a model": "A mathematical representation trained to learn from data.",
    "what is accuracy": "Ratio of correctly predicted samples to total samples.",
    "common algorithms": "Linear Regression, Logistic Regression, Decision Trees, KNN, SVM, KMeans, Naive Bayes.",
    "features and labels": "Features are input variables, labels are target output.",
    "dataset": "A collection of data points used for training/testing models.",
    "what is numpy": "Library for numerical computing. Works well with large datasets.",
    "what is pandas": "Used for data manipulation and analysis using DataFrames.",
    "what is matplotlib": "Used for data visualization (plots, charts).",

    # 💬 Help
    "help": "Ask me any Python or ML question! Try: 'list comprehension', 'difference between list and tuple', or 'how to use pandas'.",
    "topics": "I can teach: Python Basics, Data Types, Control Flow, Functions, OOP, File Handling, Modules, Exception Handling, Iterators, ML, and more!"
}
code_snippets = {
    "reverse a string": '''text = "hello"\nprint(text[::-1])''',

    "for loop example": '''for i in range(5):\n    print(i)''',

    "read file": '''with open("example.txt", "r") as file:\n    print(file.read())''',

    "write to file": '''with open("file.txt", "w") as f:\n    f.write("Hello Ren!")''',

    "function example": '''def greet(name):\n    print(f"Hello, {name}!")\ngreet("Ren")''',

    "fibonacci sequence": '''def fib(n):\n    a, b = 0, 1\n    for _ in range(n):\n        print(a, end=" ")\n        a, b = b, a + b\nfib(10)''',

    "list comprehension": '''squares = [x**2 for x in range(10)]\nprint(squares)''',

    "class example": '''class Student:\n    def __init__(self, name):\n        self.name = name\n    def greet(self):\n        print(f"Hi, I’m {self.name}!")\ns = Student("Ren")\ns.greet()''',

    "try except example": '''try:\n    x = 10 / 0\nexcept ZeroDivisionError:\n    print("Can't divide by zero!")''',

    "lambda function": '''double = lambda x: x * 2\nprint(double(4))''',

    "map example": '''nums = [1, 2, 3]\nsquares = list(map(lambda x: x*x, nums))\nprint(squares)''',

    "filter example": '''nums = [-2, 3, 0, 5, -1]\npositives = list(filter(lambda x: x > 0, nums))\nprint(positives)''',

    "generator example": '''def countdown(n):\n    while n > 0:\n        yield n\n        n -= 1\nfor i in countdown(5):\n    print(i)''',

    "sklearn model example": '''from sklearn.linear_model import LinearRegression\nmodel = LinearRegression()\nX = [[1], [2], [3]]\ny = [2, 4, 6]\nmodel.fit(X, y)\nprint(model.predict([[4]]))''',

    "pandas example": '''import pandas as pd\ndata = {'Name': ['Ren', 'Ken'], 'Age': [20, 22]}\ndf = pd.DataFrame(data)\nprint(df)''',

    "matplotlib example": '''import matplotlib.pyplot as plt\nx = [1, 2, 3]\ny = [2, 4, 6]\nplt.plot(x, y)\nplt.show()'''
}

