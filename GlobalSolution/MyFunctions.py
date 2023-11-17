import operator
import random
#TODO: maria to modify this file to add more functions

class MyFunctions:
    def __init__(self):
        
        # Define basic arithmetic functions
        self.functions = [self.add,
                          self.subtract,
                          self.multiply,
                          self.divide]

    def add(self, array):
        #sum the elements of the array
        return random.randint(0, 100) / 100

    def subtract(self, array):
        #subtract the elements of the array from the first one
        return random.randint(0, 100) / 100

    def multiply(self, array):
        #multiply the values from the array
        return random.randint(0, 100) / 100

    def divide(self, array):
        #divide the values from the array
        return random.randint(0, 100) / 100
        