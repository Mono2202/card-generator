import pandas as pd

DB_NAME = "pokemon_munchkin_v2.csv"
NEW_DB_NAME = "pokemon_munchkin.csv"

TYPES_EMOJIS = {
    "⚪": "Normal",
    "🔥": "FIre",
    "💦": "Water",
    "🌱": "Grass",
    "⚡": "Electric",
    "🧊": "Ice",
    "💪": "Fighting",
    "☠️": "Poison",
    "🌎": "Ground",
    "🪽": "Flying",
    "🔮": "Psychic",
    "🐛": "Bug",
    "🪨": "Rock",
    "👻": "Ghost",
    "🐉": "Dragon",
    "👿": "Dark",
    "🏗️": "Steel",
    "🧚": "Fairy"
}

CATEGORY_EMOJIS = {
    "🌿🔥💧": "Starter",
    "🐾": "Regular",
    "🦴": "Fossil",
    "🏆": "Legendary",
    "✨": "Mythical",
    "🐉": "Pseudo-Legendary"
}

def parse_emoji_typing_to_strings(value):
    types = value.split(", ")
    return ", ".join([TYPES_EMOJIS[current_type] for current_type in types])

def parse_emoji_can_evolve_to_bool(value):
    return value == "✅"

def parse_emoji_category_to_strings(value):
    return CATEGORY_EMOJIS[value]

def parse_description(value):
    return value[:-1].replace("•", "")

df = pd.read_csv(NEW_DB_NAME)
# columns_to_delete = ['BonusFormula', 'Index']
# df = df.drop(columns=columns_to_delete)

# df["Typing"] = df["Typing"].apply(parse_emoji_typing_to_strings)
# df["Can Evolve"] = df["Can Evolve"].apply(parse_emoji_can_evolve_to_bool)
# df["Category"] = df["Category"].apply(parse_emoji_category_to_strings)
df["Description"] = df["Description"].apply(parse_description)

df.to_csv(NEW_DB_NAME, index=False)
