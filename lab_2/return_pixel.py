from PIL import Image

class PixelSizeChecker:
    def __init__(self, path):
        self.file_path = path

    def get_size(self):
        if self.file_path.endswith((".png", ".jpg")):
            try:
                with Image.open(self.file_path) as img:
                    width, height = img.size
                    return f"{width}x{height}"
            except Exception as e:
                return f"Error: {str(e)}"
        else:
            return "Not a supported image format"