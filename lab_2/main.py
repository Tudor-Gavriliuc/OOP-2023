
import os
import threading
import time
from check_parameters import DocumentMonitor
from Choose_action import UserInterface

class DocumentMonitorApp:
    def __init__(self, path):
        self.monitor = DocumentMonitor(path)
        self.ui = UserInterface(self.monitor)

    def run(self):
        # Create a thread for scheduled detection
        detection_thread = threading.Thread(target=self.schedule_detection)
        detection_thread.daemon = True  # Set the thread as a daemon, so it doesn't block program exit

        # Start the detection thread
        detection_thread.start()

        # Run user interface in the main thread
        self.ui.run()

    def schedule_detection(self):
        while True:
            self.monitor.scan_folder()
            self.monitor.check_status()
            time.sleep(14)  # Schedule detection every 14 seconds

if __name__ == "__main__":
    folder_path = r"C:\Users\ThinkPad\PycharmProjects\POO_lab2"
    app = DocumentMonitorApp(folder_path)
    app.run()