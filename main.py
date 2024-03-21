import os

import keyboard


class Label:

    def __init__(self, labels_directory_path: str, hotkey: str):
        self.__label_directory_path = labels_directory_path
        self.__hotkey = hotkey

    @property
    def __last_label(self):
        files = os.listdir(self.__label_directory_path)
        latest_file = None
        latest_mtime = None

        for file in files:
            file_path = os.path.join(self.__label_directory_path, file)
            mtime = os.path.getmtime(file_path)

            if latest_mtime is None or mtime > latest_mtime:
                latest_mtime = mtime
                latest_file = file_path

        return latest_file

    def run(self):
        keyboard.add_hotkey(self.__hotkey, lambda: os.startfile(self.__last_label))
        keyboard.wait()

if __name__ == '__main__':
    label = Label(r'C:\Users\Stalkie\Desktop\WydrukiPP', 'ctrl+shift+o')
    label.run()