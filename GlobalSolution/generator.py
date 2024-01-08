import math
import random
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
        rows = len(self.global_train_data)
        for i in range(1):
            for img_idx in range(0, rows):
                number_of_leaves = random.randint(8, 10)
                leaves_indexes = random.sample(range(10), number_of_leaves)
                leaves = [float(self.global_train_data[img_idx][i]) for i in leaves_indexes]
                # calculate f_measure for each image
                score_idx = 0
                f_measure = 0.0
                leaves_copy = leaves.copy()
                my_functions = mf.MyFunctions().functions
                steps = {}
                layers = round(math.sqrt(number_of_leaves))
                for i in range(layers + 1):
                    steps["layer" + str(i)] = []
                self.create_steps(leaves_copy, my_functions, steps, layers)
                layers = len(steps) - 1
                score_idx = round((255 * steps["layer" + str(layers)][0][0]) % 255)
                f_measure = self.lut_train_data[img_idx][score_idx]

                image_data = {
                    "iteration": i,
                    "image_index": img_idx,
                    "f_measure": float(f_measure),
                    "leaves_indexes": leaves_indexes,
                    "leaves": leaves,
                    "score_idx": score_idx,
                    "steps": steps,
                }
                self.solution_tree.append(image_data)

    def create_steps(self, leaves_copy, my_functions, steps, layers):
        for layer in range(layers):
            temp_list = []
            while True:
                if len(leaves_copy) == 1:
                    steps["layer" + str(layer)].append([leaves_copy[0], "no_op", leaves_copy[0]])
                    temp_list.append(leaves_copy[0])
                    break
                elif len(leaves_copy) == 0:
                    break
                selected_leaves_indexes = random.sample(range(len(leaves_copy)), 2)
                selected_leaves = [leaves_copy[i] for i in selected_leaves_indexes]
                item = [0.0, "", (selected_leaves, selected_leaves_indexes)]
                func = random.choice(my_functions)
                item[0] = func(selected_leaves)
                item[1] = func.__name__
                temp_list.append(item[0])
                leaves_copy.remove(selected_leaves[0])
                leaves_copy.remove(selected_leaves[1])
                steps["layer" + str(layer)].append(item)
            leaves_copy = temp_list.copy()
        item = [0.0, "", []]
        if len(steps["layer" + str(layers - 1)]) > 1:
            selected_leaves = []
            selected_leaves.append(float(steps["layer" + str(layers - 1)][0][0]))
            selected_leaves.append(float(steps["layer" + str(layers - 1)][1][0]))
            func = random.choice(my_functions)
            result = func(selected_leaves)
            item[0] = result
            item[1] = func.__name__
            item[2] = (selected_leaves, [0, 1])
            steps["layer" + str(layers)].append(item)
        else:
            steps.pop("layer" + str(layers))
            
    # Save the best iteration data to a JSON file
    def save_best_iteration_to_json(self, json_output_file, best_tree_file):
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
        with open(best_tree_file, 'w') as best_tree_json_file:
            json.dump(sorted_generated_data[0], best_tree_json_file, indent=2)
