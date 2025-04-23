import streamlit as st
import io
import contextlib
from textwrap import dedent

st.set_page_config(page_title="Python Mastery Playground", layout="wide")
st.title("🚀 Python Mastery Playground")
st.caption("An elegant demonstration of 21 essential Python concepts")

# Stylish custom CSS for IDE/terminal look
st.markdown("""
<style>
    .block-container {
        padding-top: 2rem;
    }



    .stCodeBlock pre {
        background-color: #1e1e1e !important;
        color: #d4d4d4 !important;
        font-family: 'Fira Code', monospace;
        font-size: 0.9rem;
    }

    .terminal-output {
        background-color: #111;
        color: #33ff33;
        font-family: 'Courier New', monospace;
        font-size: 0.85rem;
        padding: 1rem;
        border-radius: 8px;
        margin-top: 1rem;
    }

    button[kind="secondary"] {
        background-color: #262730;
        color: white;
        border-radius: 8px;
    }
            
    .footer {
        text-align: center;
        padding: 2rem 0 1rem;
        color: #888;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# Function to display code with execution and output
def show_code(title, code):
    with st.expander(f"💡 {title}"):
        st.markdown('<div class="code-container">', unsafe_allow_html=True)
        st.code(dedent(code), language="python")
        st.markdown('</div>', unsafe_allow_html=True)

        run_button = st.button(f"▶️ Run: {title}", key=title)
        if run_button:
            output = run_code(code)
            st.markdown("**🖥 Terminal Output:**")
            st.markdown(f'<div class="terminal-output">{output}</div>', unsafe_allow_html=True)

# Execute code safely and capture output
def run_code(code_string):
    f = io.StringIO()
    try:
        with contextlib.redirect_stdout(f):
            exec(dedent(code_string), {})
    except Exception as e:
        return str(e)
    return f.getvalue().replace("\n", "<br>")  # preserve line breaks

# All concepts
concepts = [
    ("1. Using `self`", """
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

s = Student("Alice", 92)
s.display()
"""),

    ("2. Using `cls`", """
class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print("Objects created:", cls.count)

a = Counter()
b = Counter()
Counter.show_count()
"""),

    ("3. Public Variables and Methods", """
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} car started")

c = Car("Toyota")
print(c.brand)
c.start()
"""),

    ("4. Class Variables and Methods", """
class Bank:
    bank_name = "Default Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

b1 = Bank()
b2 = Bank()
Bank.change_bank_name("Global Bank")
print(b1.bank_name, b2.bank_name)
"""),

    ("5. Static Methods", """
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(5, 7))
"""),

    ("6. Constructors and Destructors", """
class Logger:
    def __init__(self):
        print("Logger initialized")

    def __del__(self):
        print("Logger destroyed")

log = Logger()
del log
"""),

    ("7. Access Modifiers", """
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

e = Employee("John", 50000, "123-45-6789")
print(e.name)
print(e._salary)
# print(e.__ssn)  # Raises AttributeError
"""),

    ("8. The `super()` Function", """
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

t = Teacher("Ms. Rose", "Math")
print(t.name, t.subject)
"""),

    ("9. Abstract Classes and Methods", """
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

r = Rectangle(5, 3)
print(r.area())
"""),

    ("10. Instance Methods", """
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")

d = Dog("Buddy", "Labrador")
d.bark()
"""),

    ("11. Class Methods", """
class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

Book.increment_book_count()
print(Book.total_books)
"""),

    ("12. Static Methods", """
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

print(TemperatureConverter.celsius_to_fahrenheit(25))
"""),

    ("13. Composition", """
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_car(self):
        self.engine.start()

e = Engine()
c = Car(e)
c.start_car()
"""),

    ("14. Aggregation", """
class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, employee):
        self.employee = employee

emp = Employee("Alice")
dept = Department(emp)
print(dept.employee.name)
"""),

    ("15. MRO and Diamond Inheritance", """
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d = D()
d.show()  # Follows MRO: D -> B -> C -> A
"""),

    ("16. Function Decorators", """
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

say_hello()
"""),

    ("17. Class Decorators", """
def add_greeting(cls):
    cls.greet = lambda self: "Hello from Decorator!"
    return cls

@add_greeting
class Person:
    pass

p = Person()
print(p.greet())
"""),

    ("18. Property Decorators", """
class Product:
    def __init__(self):
        self._price = 0

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

p = Product()
p.price = 100
print(p.price)
del p.price
"""),

    ("19. `callable()` and `__call__()`", """
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

m = Multiplier(3)
print(callable(m))
print(m(10))
"""),

    ("20. Custom Exception", """
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")

try:
    check_age(16)
except InvalidAgeError as e:
    print("Error:", e)
"""),

     ("21. Custom Iterable", """
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

for i in Countdown(5):
    print(i)
""")
]

# Loop through and display all
for title, code in concepts:
    show_code(title, code)

# Final decoration
st.balloons()

# Footer
st.markdown('<div class="footer">✨ Developed by <strong>Sabila Aleem</strong> ✨</div>', unsafe_allow_html=True)

