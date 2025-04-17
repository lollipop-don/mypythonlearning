import random
first_names = [
    "Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Isaac", "Jack",
    "Karen", "Leo", "Mia", "Nina", "Oscar", "Paul", "Quincy", "Rachel", "Sam", "Tina",
    "Uma", "Victor", "Wendy", "Xander", "Yara", "Zane", "Aaron", "Bella", "Caleb", "Diana",
    "Elijah", "Fiona", "Gavin", "Hazel", "Ivy", "Jake", "Kylie", "Liam", "Megan", "Noah",
    "Olivia", "Parker", "Queen", "Ryan", "Sophie", "Thomas", "Ursula", "Violet", "Will", "Zoe",
    "Adrian", "Brianna", "Cody", "Delilah", "Ethan", "Freya", "George", "Hailey", "Ian", "Julia",
    "Kevin", "Lara", "Max", "Natalie", "Omar", "Phoebe", "Quinn", "Riley", "Sean", "Talia",
    "Uri", "Vanessa", "Wade", "Xenia", "Yusuf", "Zelda", "Abby", "Blake", "Chloe", "Derek",
    "Elle", "Finn", "Gemma", "Harvey", "Isla", "Jonah", "Kara", "Logan", "Mila", "Nico",
    "Opal", "Preston", "Reed", "Sierra", "Troy", "Ulric", "Vera", "Wyatt", "Xiomara", "Yvonne"
]

languages = [
    "Python", "Java", "C++", "JavaScript", "Go", "Rust", "C#", "Ruby", "Swift",
    "Kotlin", "PHP", "TypeScript", "Scala", "Perl", "Dart", "Haskell", "Elixir", "Lua"
]

# Shuffle first names to randomize order
random.shuffle(first_names)

# Create dictionary cycling through languages
name_language_dict = {first_names[i]: languages[i % len(languages)] for i in range(100)}

# Example of printing the result
for name, lang in list(name_language_dict.items())[:10]:
    print(f"{name}: {lang}")