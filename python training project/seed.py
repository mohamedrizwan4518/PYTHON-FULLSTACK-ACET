from app import app
from extensions import db

from models.lesson import Lesson
from models.challenge import Challenge
from models.badge import Badge
from models.user import User

def seed_data():
    with app.app_context():
        # Clean existing data
        db.drop_all()
        db.create_all()
        
        # 1. Badges (Updated based on new modules)
        badges = [
            Badge(name="Syntax Survivor", description="Mastered Python Basics (Module 1)", icon="fas fa-microchip", criteria_type="module_completion", criteria_value=1),
            Badge(name="Collection Collector", description="Conquered Lists and Dicts (Module 2)", icon="fas fa-boxes", criteria_type="module_completion", criteria_value=2),
            Badge(name="Function Forger", description="Crafted reusable logic (Module 3)", icon="fas fa-tools", criteria_type="module_completion", criteria_value=3),
            Badge(name="Data Handler", description="Handled Files and Exceptions (Module 4)", icon="fas fa-file-export", criteria_type="module_completion", criteria_value=4),
            Badge(name="Architect", description="Mastery of OOP (Module 6)", icon="fas fa-monument", criteria_type="module_completion", criteria_value=6),
            Badge(name="Python Master", description="Completed the Advanced Path", icon="fas fa-crown", criteria_type="level", criteria_value=15)
        ]
        db.session.add_all(badges)

        # 2. Module 1: Python Basics (Syntax + Mental Model)
        # Lesson 1.1: Values, Types, and Variables
        l1_1 = Lesson(title="1.1 Values, Types, and Variables", 
                    content="""<h3>World 1: The Foundations</h3>
<p>In Python, everything is an object. Each object has a <b>type</b> and a <b>value</b>.</p>
<ul>
    <li><b>int</b>: Whole numbers like 5, -10</li>
    <li><b>float</b>: Decimal numbers like 3.14</li>
    <li><b>bool</b>: True or False</li>
    <li><b>str</b>: Text like "Hello"</li>
</ul>
<p>Use <code>type(variable)</code> to check the type! Remember: naming rules require lowercase and underscores (snake_case).</p>""", 
                    difficulty="Beginner", order=1, xp_reward=50)
        db.session.add(l1_1)
        db.session.flush()
        
        db.session.add(Challenge(lesson_id=l1_1.id, title="The Identity Spell", 
                        description="Assign the integer `42` to a variable named `answer`. Then assign the string `'Python'` to `name`. Print both.",
                        starter_code="# Your code here\n",
                        solution_code="answer = 42\nname = 'Python'\nprint(answer)\nprint(name)",
                        xp_reward=100, difficulty="Beginner"))

        # Lesson 1.3: Strings
        l1_3 = Lesson(title="1.3 String Manipulation", 
                    content="""<h3>String Forging</h3>
<p>Strings are sequences. You can index them <code>s[0]</code> or slice them <code>s[1:4]</code>.</p>
<h4>Common Methods:</h4>
<ul>
    <li><code>.split()</code>: Break into list</li>
    <li><code>.join()</code>: Glue list into string</li>
    <li><code>.strip()</code>: Remove whitespace</li>
</ul>
<p>Modern Python uses <b>f-strings</b>: <code>f"Hello {name}"</code></p>""", 
                    difficulty="Beginner", order=2, xp_reward=50)
        db.session.add(l1_3)
        db.session.flush()

        db.session.add(Challenge(lesson_id=l1_3.id, title="The Name Reverser", 
                        description="Given `user_name = 'Quest'`, use slicing to print it reversed.",
                        starter_code="user_name = 'Quest'\n# Reverse it\n",
                        solution_code="user_name = 'Quest'\nprint(user_name[::-1])",
                        xp_reward=100, difficulty="Beginner"))

        # Boss Challenge: Module 1
        l1_boss = Lesson(title="Module 1 BOSS: \"Fix-the-bug\"", 
                    content="""<h3>Boss Fight 1</h3>
<p>A corrupted script is causing errors. You must fix the variable types and naming to restore order.</p>""", 
                    difficulty="Beginner", order=3, xp_reward=150)
        db.session.add(l1_boss)
        db.session.flush()

        db.session.add(Challenge(lesson_id=l1_boss.id, title="Script Restoration", 
                        description="Fix the following code: `1st_name = 100` (naming error), `age = '25' + 5` (type error). Make `first_name` stay 'Quest' and `age` be 30.",
                        starter_code="# Broken code\n1st_name = 'Quest'\nage = '25' + 5\n",
                        solution_code="first_name = 'Quest'\nage = 25 + 5\nprint(first_name)\nprint(age)",
                        xp_reward=200, difficulty="Beginner"))

        # 3. Module 2: Collections and Iteration
        # Lesson 2.1: Lists
        l2_1 = Lesson(title="2.1 Lists and Mutations", 
                    content="""<h3>World 2: Collections</h3>
<p>Lists are ordered and mutable. You can <code>.append()</code>, <code>.insert()</code>, or <code>.pop()</code> items.</p>
<p><b>Sort</b>: <code>sorted(list)</code> returns a new list, while <code>list.sort()</code> changes it in-place.</p>""", 
                    difficulty="Beginner", order=4, xp_reward=75)
        db.session.add(l2_1)
        db.session.flush()

        db.session.add(Challenge(lesson_id=l2_1.id, title="Inventory Sort", 
                        description="Start with `inventory = ['sword', 'shield']`. Add 'potion' to the end, then sort the inventory alphabetically and print it.",
                        starter_code="inventory = ['sword', 'shield']\n# Add and sort\n",
                        solution_code="inventory = ['sword', 'shield']\ninventory.append('potion')\ninventory.sort()\nprint(inventory)",
                        xp_reward=125, difficulty="Beginner"))

        # Lesson 2.3: Dictionaries
        l2_3 = Lesson(title="2.3 Mapping with Dictionaries", 
                    content="""<h3>The Key-Value Realm</h3>
<p>Dictionaries store associations. Accessing keys that don't exist causes an error. Use <code>.get(key, default)</code> to stay safe!</p>""", 
                    difficulty="Beginner", order=5, xp_reward=75)
        db.session.add(l2_3)
        db.session.flush()

        db.session.add(Challenge(lesson_id=l2_3.id, title="Player Stats", 
                        description="Create a dict `stats` with 'hp': 100, 'mp': 50. Update 'hp' to 120 and add 'level': 1. Print the 'mp' using .get()",
                        starter_code="stats = {}\n# Fill and update\n",
                        solution_code="stats = {'hp': 100, 'mp': 50}\nstats['hp'] = 120\nstats['level'] = 1\nprint(stats.get('mp'))",
                        xp_reward=125, difficulty="Beginner"))

        # Lesson 2.5: Loops
        l2_5 = Lesson(title="2.5 The Infinite Path (Loops)", 
                    content="""<h3>Iteration Helpers</h3>
<p>Use <code>for</code> for known counts and <code>while</code> for conditions. <code>enumerate()</code> gives you index AND value! <code>zip()</code> pairs two collections together.</p>""", 
                    difficulty="Beginner", order=6, xp_reward=75)
        db.session.add(l2_5)
        db.session.flush()

        db.session.add(Challenge(lesson_id=l2_5.id, title="Scoreboard Leaderboard", 
                        description="Given `names = ['Alice', 'Bob']` and `scores = [85, 92]`, use `zip` and `for` to print: 'Player: [name], Score: [score]'",
                        starter_code="names = ['Alice', 'Bob']\nscores = [85, 92]\n# Zip them\n",
                        solution_code="names = ['Alice', 'Bob']\nscores = [85, 92]\nfor name, score in zip(names, scores):\n    print(f'Player: {name}, Score: {score}')",
                        xp_reward=150, difficulty="Beginner"))

        # 4. Module 3: Functions and Modular Thinking
        l3_1 = Lesson(title="3.1 The Magic of Functions", 
                    content="""<h3>World 3: Modular Thinking</h3>
<p>Functions wrap logic. Use <code>def</code> to define them. Remember <b>Scope</b>: variables inside a function stay inside (Local), but they can see variables outside (Global).</p>""", 
                    difficulty="Intermediate", order=7, xp_reward=100)
        db.session.add(l3_1)
        db.session.flush()

        db.session.add(Challenge(lesson_id=l3_1.id, title="Power Spell", 
                        description="Define a function `calculate_power(base, exponent=2)` that returns base raised to the exponent power.",
                        starter_code="def calculate_power(base, exponent=2):\n    # Return power here\n",
                        solution_code="def calculate_power(base, exponent=2):\n    return base ** exponent",
                        xp_reward=150, difficulty="Intermediate"))

        # 5. Module 4: Data Handling (Exceptions + Files)
        l4_1 = Lesson(title="4.1 Handling the Chaos (Exceptions)", 
                    content="""<h3>World 4: Resilience</h3>
<p>Code breaks. Use <code>try...except...finally</code> to catch <code>ValueError</code>, <code>ZeroDivisionError</code>, and more.</p>""", 
                    difficulty="Intermediate", order=8, xp_reward=100)
        db.session.add(l4_1)
        db.session.flush()

        db.session.add(Challenge(lesson_id=l4_1.id, title="Safe Divider", 
                        description="Write a function `safe_divide(a, b)` that returns a/b. If b is 0, catch the Exception and return 'Error: Division by zero'.",
                        starter_code="def safe_divide(a, b):\n    # Try divide\n",
                        solution_code="def safe_divide(a, b):\n    try:\n        return a / b\n    except ZeroDivisionError:\n        return 'Error: Division by zero'",
                        xp_reward=175, difficulty="Intermediate"))

        # 6. Module 6: OOP (Object-Oriented Programming)
        l6_1 = Lesson(title="6.1 Constructing Classes", 
                    content="""<h3>World 6: The Architect</h3>
<p>OOP is about modeling real-world objects. Classes have <b>Attributes</b> (data) and <b>Methods</b> (behavior).</p>
<p><code>__init__</code> is the constructor. <code>self</code> refers to the specific instance.</p>""", 
                    difficulty="Intermediate", order=9, xp_reward=125)
        db.session.add(l6_1)
        db.session.flush()

        db.session.add(Challenge(lesson_id=l6_1.id, title="RPG Character", 
                        description="Create a class `Warrior` with attributes `name` and `attack_power`. Add a method `swing()` that prints '[name] swings for [power] damage!'",
                        starter_code="class Warrior:\n    # Implement here\n",
                        solution_code="class Warrior:\n    def __init__(self, name, attack_power):\n        self.name = name\n        self.attack_power = attack_power\n    def swing(self):\n        print(f'{self.name} swings for {self.attack_power} damage!')",
                        xp_reward=200, difficulty="Intermediate"))

        # Advanced Path: Module 7 (Decorators)
        l7_1 = Lesson(title="7.1 Advanced Patterns (Decorators)", 
                    content="""<h3>Intermediate Power</h3>
<p><b>Decorators</b> wrap functions to add functionality. <b>Closures</b> capture local variables even after the function finishes.</p>""", 
                    difficulty="Advanced", order=10, xp_reward=150)
        db.session.add(l7_1)
        db.session.flush()

        db.session.add(Challenge(lesson_id=l7_1.id, title="The Guard Decorator", 
                        description="Write a decorator `authenticated` that prints 'Checking Auth...' before calling the wrapped function.",
                        starter_code="def authenticated(func):\n    # Implement closure here\n",
                        solution_code="def authenticated(func):\n    def wrapper(*args, **kwargs):\n        print('Checking Auth...')\n        return func(*args, **kwargs)\n    return wrapper",
                        xp_reward=250, difficulty="Advanced"))

        db.session.commit()
        print("Database seeded with REAL-WORLD curriculum successfully!")

if __name__ == "__main__":
    seed_data()
