# choose_action.py

class UserInterface:
    def __init__(self, monitor):
        self.monitor = monitor

    def run(self):
        while True:
            action = input("\n Choose an action: commit, info <filename>, status, exit) = ")
            if action == "commit":
                self.monitor.create_snapshot()
            elif action.startswith("info"):
                _, filename = action.split(maxsplit=1)
                self.monitor.show_file_info(filename)
            elif action == "status":
                self.monitor.scan_folder()
                self.monitor.check_status()
            elif action == "exit":
                break
            else:
                print("Invalid action. Please try again.")
# choose_action.py

class UserInterface:
    def __init__(self, monitor):
        self.monitor = monitor

    def run(self):
        while True:
            action = input("\n Choose an action: commit, info <filename>, status, exit) = ")
            if action == "commit":
                self.monitor.create_snapshot()
            elif action.startswith("info"):
                _, filename = action.split(maxsplit=1)
                self.monitor.show_file_info(filename)
            elif action == "status":
                self.monitor.scan_folder()
                self.monitor.check_status()
            elif action == "exit":
                break
            else:
                print("Invalid action. Please try again.")
