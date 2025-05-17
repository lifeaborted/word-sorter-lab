class TextProcessor:
    @staticmethod
    def process(text):
        words = set(word.strip(".,!?\"'") for word in text.split() if word.strip())
        return sorted(words)
