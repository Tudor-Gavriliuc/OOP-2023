
class TextStatsCalculator:
    def __init__(self, path):
        self.path = path

    def get_text_stats(self):
        if self.path.endswith(".txt"):
            try:
                with open(self.path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    lines = content.split('\n')
                    words = content.split()
                    char_count = len(content)
                    line_count = len(lines)
                    word_count = len(words)
                    return line_count, word_count, char_count
            except Exception as e:
                return "Error: " + str(e)
        else:
            return "Not a text file"