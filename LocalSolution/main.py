from DataLoader import DataLoader
import sys
import json
import MyFunctions as mf

def main():
    # entrypoint
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <LocalTrain directory>")
        return
    best_tree_filepath = './output/best_tree_file.json'
    dl = DataLoader(sys.argv[1])
    dl.load_data()
    tree_steps = get_steps(best_tree_filepath)
    i = 0
    f_average_measure = 0
    for key, value in dl.localtrain_data.items():
        
        TP = 0
        FP = 0
        TN = 0
        FN = 0
        for elem in value:
            threshold = get_pixel_threshold(tree_steps, elem)
            if(threshold < float(elem[0])):
                true_false = 1
                if(true_false == int(elem[1])): 
                    TP += 1
                else:
                    FP += 1
            else:
                true_false = 0
                if(true_false == int(elem[1])):
                    TN += 1
                else:
                    FN += 1
        f_measure = TP/(TP + 0.5*(FP + FN))    
        with open('f_measure.txt', 'a') as file:
            file.write(f"File name: {dl.csv_names[i]} F_measure: {str(f_measure)} \n")
        i += 1
        f_average_measure += f_measure
    f_average_measure = f_average_measure / i
    with open('f_measure.txt', 'a') as file:
        file.write(f"F_average_measure: {f_average_measure} \n")

def get_steps(best_tree_filepath):
    return_data = {}
    with open(best_tree_filepath) as file:
        content = file.read()
        try:
            content_data = json.loads(content)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
    i = 0
    tmp = content_data["leaves"].copy()
    return_data["initial_leaves"] = tmp.copy()
    return_data["initial_leaves_indexes"] = content_data["leaves_indexes"].copy()
    for key, value in content_data["steps"].items():
        return_data[key] = {}
        return_data[key]["steps"] = []
        leaves = tmp.copy()
        return_data[key]["leaves"] = leaves.copy()
        tmp = []
        for elem2 in value:
            tmp.append(elem2[0])
            if elem2[1] == 'no_op':
                return_data[key]["steps"].append((0, 0, elem2[1]))
                continue
            else:
                return_data[key]["steps"].append((elem2[2][1][0], elem2[2][1][1], elem2[1]))
                leaves.remove(elem2[2][0][0])
                leaves.remove(elem2[2][0][1])
    return return_data

def get_pixel_threshold(data, pixel):
    thresholds = []
    for index in data["initial_leaves_indexes"]:
        thresholds.append(pixel[2 + index])
    layers = {k: v for k, v in data.items() if k.startswith('layer')}
    for key, value in layers.items():
        for elem in value["steps"]:
            if elem[2] == 'no_op':
                continue
            function = mf.MyFunctions().get_function_by_name(elem[2])
            after_function_elem = function([float(thresholds[elem[0]]), float(thresholds[elem[1]])])
            for index in sorted([elem[0], elem[1]], reverse=True):
                del thresholds[index]
            thresholds.append(after_function_elem)
    return thresholds[0]
if __name__ == "__main__":
    main()