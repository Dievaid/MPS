import glob
from csv import reader

class DataLoader:
    def __init__(self, directory_path):
        self.directory_path = directory_path
        self.localtrain_data = {}
        self.csv_names = []

    def load_data(self):
        csv_files = glob.glob(self.directory_path + '/*.csv')
        for path in csv_files:
            self.csv_names.append(path)
            with open(path, 'r') as read_obj:
                csv_reader = reader(read_obj)
                file_data = [row for row in csv_reader]
                self.localtrain_data[path] = file_data
        