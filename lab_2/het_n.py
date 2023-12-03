import re

class ProgramStatsCalculator:
    def __init__(self, path):
        self.path = path
        self.content = None

    def load_file_content(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            self.content = file.read()

    def get_program_stats(self):
        if self.path.endswith(".py") or self.path.endswith(".java"):
            if self.content is None:
                self.load_file_content()

            lines = self.content.split('\n')
            line_count = len(lines)
            class_count = self.count_classes()
            method_count = self.count_methods()
            word_count = self.count_words()
            char_count = self.count_characters()

            return line_count, class_count, method_count, word_count, char_count

        return 0, 0, 0, 0, 0

    def count_classes(self):
        class_pattern = r'\bclass\b'
        class_count = len(re.findall(class_pattern, self.content))
        return class_count

    def count_methods(self):
        method_pattern = r'\bdef\s+(\w+)\s*\(.*\)\s*:'
        method_count = len(re.findall(method_pattern, self.content))
        return method_count

    def count_words(self):
        words = self.content.split()
        word_count = len(words)
        return word_count

    def count_characters(self):
        char_count = len(self.content)
        return char_count