class TextProcessor:
    @staticmethod
    def process(text):
        words = set(word.strip(".,!?\"'") for word in text.split())
        return sorted(words)
