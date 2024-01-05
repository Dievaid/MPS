import math
import numpy as np
import statistics as s
import random

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
        return np.mean(globalLine)

    def func_gmean(self, globalLine):
        return s.geometric_mean(globalLine)

    def func_median(self, globalLine):
        return s.median(globalLine)

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

if __name__ == "__main__":
    mf = MyFunctions()
    func = random.choice(mf.functions)
    print(func([0.9,0.856863,0.905898,0.903922,0.905898,0.907843,0.754902,0.906205]))