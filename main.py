TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

USERS = {
    "bob": "123",
    "ann": "pass123",
    "mike": "pa$$word",
}

SEPARATOR = "-" * 38

# --- Login ---
username = input("username:")
password = input("password:")

if USERS.get(username) != password:
    print("unregistered user, terminating the program..")
    exit()

print(SEPARATOR)
print(f"Welcome to the app, {username}")
print(f"We have {len(TEXTS)} texts to be analyzed.")
print(SEPARATOR)

# --- Text selection ---
try:
    text_number = int(input(f"Enter a number btw. 1 and {len(TEXTS)} to select: "))
except ValueError:
    print("Invalid input, terminating the program..")
    exit()

if text_number < 1 or text_number > len(TEXTS):
    print("Invalid text number, terminating the program..")
    exit()

selected_text = TEXTS[text_number - 1]
words = selected_text.split()

# --- Analysis ---
titlecase_words = [w for w in words if w[0].isupper() and not w.isupper()]
uppercase_words = [w for w in words if w.isupper() and w.isalpha()]
lowercase_words = [w for w in words if w.islower()]
numeric_strings = [w for w in words if w.isdigit()]

word_count = len(words)
titlecase_count = len(titlecase_words)
uppercase_count = len(uppercase_words)
lowercase_count = len(lowercase_words)
numeric_count = len(numeric_strings)
numeric_sum = sum(int(n) for n in numeric_strings)

print(SEPARATOR)
print(f"There are {word_count} words in the selected text.")
print(f"There are {titlecase_count} titlecase words.")
print(f"There are {uppercase_count} uppercase words.")
print(f"There are {lowercase_count} lowercase words.")
print(f"There are {numeric_count} numeric strings.")
print(f"The sum of all the numbers {numeric_sum}")
print(SEPARATOR)

# --- Bar chart of word lengths ---
length_counts = {}
for word in words:
    clean = word.strip(".,!?;:\"'()-")
    length = len(clean)
    if length > 0:
        length_counts[length] = length_counts.get(length, 0) + 1

max_len = max(length_counts.keys())
max_count = max(length_counts.values())

print(f"{'LEN':<4}| {'OCCURRENCES':<20} |NR.")
print(SEPARATOR)

for length in range(1, max_len + 1):
    count = length_counts.get(length, 0)
    bar = "*" * count
    print(f"{length:>4}|{bar:<20} |{count}")
