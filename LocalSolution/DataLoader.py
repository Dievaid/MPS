from csv import reader
class DataLoader:
    def __init__(self, localtrain_path):
        # TODO
        self._localtrain_path = localtrain_path
        self.localtrain_data = [[]]
        
        
    def load_data(self):
        # TODO
        print("Loading LocalTrain.csv")
        with open(self._localtrain_path) as file:
            self.localtrain_data = list(reader(file, delimiter=','))[0]
        print("Done with LocalTrain")
        
        