from return_pixel import PixelSizeChecker
from get_text import TextStatsCalculator
from het_n import ProgramStatsCalculator

class FileProcessor:
    def process_file(self, file_path):
        pass

class TxtFileProcessor(FileProcessor):
    def process_file(self, file_path):
        text_stats_calculator = TextStatsCalculator(file_path)
        line_count, word_count, char_count = text_stats_calculator.get_text_stats()
        return {"line_count": line_count, "word_count": word_count, "char_count": char_count}

class ImageFileProcessor(FileProcessor):
    def __init__(self, pixel_size_checker_class):
        self.pixel_size_checker_class = pixel_size_checker_class

    def process_file(self, file_path):
        image_size_checker = self.pixel_size_checker_class(file_path)
        return {"image_size": image_size_checker.return_size()}

class ProgramFileProcessor(FileProcessor):
    def process_file(self, file_path):
        program_stats_calculator = ProgramStatsCalculator(file_path)
        line_count, class_count, method_count, word_count, char_count = program_stats_calculator.get_program_stats()
        return {
            "line_count": line_count,
            "class_count": class_count,
            "method_count": method_count,
            "word_count": word_count,
            "char_count": char_count
        }