#import pandas as pd
import math
import glob
import platform
import random
import csv
import os
import MyFunctions as mf
import json
import numpy as np

class Generator:
    def __init__(self, data_loader):
        self.global_train_data = data_loader.globaltrain_data
        self.lut_train_data = data_loader.luttrain_data
        self.solution_tree = []

    def generate_solution_tree(self):
        # iterate through the solution tree
        for i in range(10):
            print('Iteration: ', str(i))

            # apply function to each image in the global_train_data
            # 1st row to 15296th
            for img_idx in range(0, random.randint(0, len(self.global_train_data))):
                
                # generate random number of leaves for each image
                number_of_leaves = random.randint(2, len(self.global_train_data[0]) - 1)
                function = random.choice(mf.MyFunctions().functions)
                # generate the random leaves
                leaves = list(map(lambda x : float(x), random.sample(self.global_train_data[img_idx], number_of_leaves)))
                # calculate f_measure for each image
                score_idx = 0
                f_measure = 0.0
                try:
                    score_idx = round(255 * function(leaves))
                    if score_idx > 255:
                        continue
                    f_measure = self.lut_train_data[img_idx][score_idx]
                    # print(f"[Iteration {i}] f_measure for {img_idx} is {f_measure}")
                except:
                    # print(f"{function(leaves)} {score_idx} {function.__name__}")
                    exit(0)

                # add generated data for each image to the iteration_data
                image_data = {
                    "iteration": i,
                    "image_index": img_idx,
                    "leaves": leaves,
                    "f_measure": float(f_measure),
                    "function_name": function.__name__
                }
                self.solution_tree.append(image_data)
            
    # Save the best iteration data to a JSON file
    def save_best_iteration_to_json(self, json_output_file):
        # Sort the generated_data based on individual f_measure values
        sorted_generated_data = sorted(self.solution_tree, key=lambda x: x["f_measure"], reverse=True)[:5000]
        f_measure_avg = 0.0
        for elem in sorted_generated_data:
            f_measure_avg += elem["f_measure"]
        f_measure_avg /= len(sorted_generated_data)
        # # Create a dictionary to hold the additional information
        additional_info = {
            "f_measure_avg": f_measure_avg,
        }

        # Combine the additional information with the top 20 data
        final_data = [additional_info] + sorted_generated_data

        # Write the final data to the JSON file
        with open(json_output_file, 'w') as json_file:
            json.dump(final_data, json_file, indent=2)
        

            
            
            
            
            
        
        
        