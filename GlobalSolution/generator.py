#import pandas as pd
import math
import glob
import platform
import random
import csv
import os
import MyFunctions as mf
import json

class Generator:
    def __init__(self, data_loader):
        self.global_train_data = data_loader.globaltrain_data
        self.lut_train_data = data_loader.luttrain_data
        self.solution_tree = []

    def generate_solution_tree(self):
        # iterate through the solution tree
        for i in range(100):
            print('Iteration: ', str(i))

            # generate a random function from the list of functions
            function = random.choice(mf.MyFunctions().functions)

            iteration_data = {
                "iteration": i,
                "function_name": function.__name__,
                "f_measure_avg": 0,  # Initialize for the average F-measure

                # List to store generated data for each image
                "generated_data": []
            }

            # apply function to each image in the global_train_data
            for img_idx in range(1, len(self.global_train_data)):
                
                # generate random number of leaves for each image
                number_of_leaves = random.randint(2, len(self.global_train_data[0]))

                # generate the random leaves
                leaves = random.sample(self.global_train_data[img_idx], number_of_leaves)

                # calculate f_measure for each image
                score_idx = round(255 * function(leaves))
                f_measure = self.lut_train_data[img_idx][score_idx]

                # save the f_measure
                iteration_data["f_measure_avg"] += float(f_measure)

                # add generated data for each image to the iteration_data
                image_data = {
                    "image_index": img_idx,
                    "leaves": leaves,
                    "f_measure": float(f_measure)
                }

                iteration_data["generated_data"].append(image_data)

            # calculate the average f_measure for each function
            iteration_data["f_measure_avg"] /= len(self.global_train_data)

            # append the iteration_data to the solution tree
            self.solution_tree.append(iteration_data)
            
    # Save the best iteration data to a JSON file
    def save_best_iteration_to_json(self, json_output_file):
        # Find the iteration with the best f_measure_avg
        best_iteration = max(self.solution_tree, key=lambda x: x["f_measure_avg"])

        # Sort the generated_data based on individual f_measure values
        sorted_generated_data = sorted(best_iteration["generated_data"], key=lambda x: x["f_measure"], reverse=True)

        # Take the function code and iteration number
        function_name = best_iteration["function_name"]
        iteration_number = best_iteration["iteration"]
        f_measure_avg = best_iteration["f_measure_avg"]

        # Create a dictionary to hold the additional information
        additional_info = {
            "iteration_number": iteration_number,
            "function_name": function_name,
            "f_measure_avg": f_measure_avg,
        }

        # Combine the additional information with the top 20 data
        final_data = [additional_info] + sorted_generated_data[:20]

        # Write the final data to the JSON file
        with open(json_output_file, 'w') as json_file:
            json.dump(final_data, json_file, indent=2)
        

            
            
            
            
            
        
        
        