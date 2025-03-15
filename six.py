import unicodedata
import collections

def detect_script(char):
    """Detects the script of a given character."""
    try:
        name = unicodedata.name(char)
        if "CYRILLIC" in name:
            return "Cyrillic"
        elif "ARABIC" in name:
            return "Arabic"
        elif "HAN" in name:
            return "Chinese"
        elif "HIRAGANA" in name or "KATAKANA" in name:
            return "Japanese"
        elif "HANGUL" in name:
            return "Korean"
        elif "GREEK" in name:
            return "Greek"
        else:
            return "Latin"
    except ValueError:
        return "Unknown"

def analyze_text_file(filename):
    """Analyzes the text file and counts words per script."""
    script_count = collections.defaultdict(int)
    
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            for word in line.split():
                script = detect_script(word[0])  # Check script of the first character
                script_count[script] += 1
    
    return script_count

def main():
    filename = "file.txt"  # Ensure this file contains multilingual sentences
    script_count = analyze_text_file(filename)
    
    print("Language Script Analysis:")
    for script, count in script_count.items():
        print(f"{script}: {count} words")
    
    print(f"Total different languages detected: {len(script_count)}")

if __name__ == "__main__":
    main()
