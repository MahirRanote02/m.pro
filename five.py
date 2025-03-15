import random

# Step 1: Basic Emoji Translator
emoji_dict = {
    "hello": "👋",
    "happy": "😃",
    "sad": "😢",
    "love": "❤️",
    "coffee": "☕",
    "dog": "🐶",
    "cat": "🐱",
    "car": "🚗",
    "sun": "☀️",
    "moon": "🌙",
    "thank you": "🙏",
    "good morning": "🌅",
    "good night": "🌙✨",
    "fire": "🔥",
    "clap": "👏",
    "star": "⭐",
    "rain": "🌧️",
    "music": "🎵",
    "book": "📖"
}

# Step 2: Mood-Based Emoji Filler
mood_dict = {
    "happy": ["😃", "🎉", "🥳", "😊", "🌞"],
    "sad": ["😢", "💔", "😞", "🌧️", "😭"],
    "excited": ["🤩", "🔥", "🎊", "🚀", "💃"],
    "angry": ["😡", "💢", "😠", "🤬", "😤"],
    "love": ["❤️", "💖", "😍", "💘", "💕"],
    "relaxed": ["😌", "🌿", "☕", "🛀", "🧘"]
}

def translate_to_emoji(sentence):
    words = sentence.split()
    translated_sentence = " ".join([emoji_dict.get(word.lower(), word) for word in words])
    return translated_sentence

def add_mood_emojis(sentence, mood):
    if mood in mood_dict:
        mood_emojis = " ".join(random.sample(mood_dict[mood], min(3, len(mood_dict[mood]))))
        return f"{sentence} {mood_emojis}"
    return sentence

def main():
    print("Welcome to the Emoji Translator! Type 'exit' to quit.")
    while True:
        user_input = input("Enter a sentence (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Goodbye! 👋")
            break
        
        if "(fill with" in user_input:
            parts = user_input.split("(fill with")
            sentence = translate_to_emoji(parts[0].strip())
            mood = parts[1].replace(")", "").strip().lower()
            print(add_mood_emojis(sentence, mood))
        else:
            print(translate_to_emoji(user_input))

if __name__ == "__main__":
    main()
