# Read data from input file
from csv import reader
from main import setup_logger
logger = setup_logger()
class DataLoader:
    def __init__(self, globaltrain_filepath, luttrain_filepath):
        self._globaltrain_filepath = globaltrain_filepath
        self._luttrain_filepath = luttrain_filepath
        self.globaltrain_data = [[]]
        self.luttrain_data = [[]]
        
        
    def load_data(self):
        logger.info("Loading GlobalTrain.csv")
        with open(self._globaltrain_filepath) as file:
            self.globaltrain_data = list(reader(file, delimiter=','))[1:]
        logger.info("Done with GlobalTrain")
        
        logger.info("Loading LUTTrain.csv")
        with open(self._luttrain_filepath) as file:
            self.luttrain_data = list(reader(file, delimiter=','))[1:]
        logger.info("Done with LUTTrain")
        
        