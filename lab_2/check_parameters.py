import os
from datetime import datetime
from file_processors import TxtFileProcessor, ImageFileProcessor, ProgramFileProcessor
from return_pixel import PixelSizeChecker

class DocumentMonitor:
    def __init__(self, path):
        self.folder_path = path
        self.snapshot_time = None
        self.file_info = {}
        self.previous_file_list = set()
        self.file_processors = {
            ".txt": TxtFileProcessor(),
            ".png": ImageFileProcessor(PixelSizeChecker),
            ".jpg": ImageFileProcessor(PixelSizeChecker),
            ".py": ProgramFileProcessor(),
            ".java": ProgramFileProcessor()
        }

    def create_snapshot(self):
        self.snapshot_time = datetime.now()
        self.previous_file_list = set(self.file_info.keys())
        self.file_info = {}
        print(f"Snapshot taken at {self.snapshot_time}")

    def scan_folder(self):
        files = os.listdir(self.folder_path)
        print(f"\nFiles in folder: {', '.join(files)}")
        for file in files:
            file_path = os.path.join(self.folder_path, file)
            if os.path.isfile(file_path):
                self.update_file_info(file_path)

    def update_file_info(self, file_path):
        file_info = {}
        file_info["name"] = os.path.relpath(file_path, self.folder_path)
        file_info["extension"] = os.path.splitext(file_path)[1]
        file_info["created_time"] = datetime.fromtimestamp(os.path.getctime(file_path))
        file_info["modified_time"] = datetime.fromtimestamp(os.path.getmtime(file_path))

        if file_info["extension"] in self.file_processors:
            processor = self.file_processors[file_info["extension"]]
            additional_info = processor.process_file(file_path)
            file_info.update(additional_info)

        self.file_info[file_info["name"]] = file_info

    def show_file_info(self, filename):
        if filename in self.file_info:
            file_info = self.file_info[filename]
            print("File Name:", file_info["name"])
            print("Extension:", file_info["extension"])
            print("Created Time:", file_info["created_time"])
            print("Modified Time:", file_info["modified_time"])
            for key, value in file_info.items():
                if key not in ["name", "extension", "created_time", "modified_time"]:
                    print(f"{key.capitalize()}: {value}")
        else:
            print(f"File '{filename}' not found in the monitored folder.")

    def check_status(self):
        if self.snapshot_time:
            print(f"Snapshot taken at {self.snapshot_time}")

            current_file_list = set(self.file_info.keys())
            added_files = current_file_list - self.previous_file_list
            deleted_files = self.previous_file_list - current_file_list

            for filename, file_info in self.file_info.items():
                if filename in added_files:
                    print(f"{filename} - New File")
                elif filename in deleted_files:
                    print(f"{filename} - Deleted")
                elif filename not in deleted_files and os.path.exists(os.path.join(self.folder_path, filename)):
                    if file_info["modified_time"] > self.snapshot_time:
                        print(f"{filename} - Modified")
                    else:
                        print(f"{filename} - No change")
                else:
                    print(f"{filename} - File deleted")



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



