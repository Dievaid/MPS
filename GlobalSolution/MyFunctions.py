import math
import numpy as np
import statistics as s

class MyFunctions:
    def __init__(self):
        
        # Define functions
        self.functions = [
                            self.func_mean,
                            self.func_hmean,
                            self.func_gmean,
                            self.func_median,
                            self.min_val,
                            self.max_val,
                            self.func_sqmean
                        ]

 
    def func_mean(self, globalLine):
        return np.mesn(globalLine)

    def func_gmean(self, globalLine):
        return s.geometric_mean(globalLine)

    def func_median(self, globalLine):
        s.median(globalLine)

    def func_hmean(self, globalLine):
        return s.harmonic_mean(globalLine)

    def func_sqmean(self, globalLine):
        sum = 0

        for g in globalLine:
            sum += g * g
        
        return math.sqrt(sum / len(globalLine))

    def min_val(self, globalLine):
        return min(globalLine) 

    def max_val(self, globalLine):
        return max(globalLine)
