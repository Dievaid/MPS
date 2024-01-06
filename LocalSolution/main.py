from DataLoader import DataLoader
import sys
import json
def main():
    # entrypoint
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <LocalTrain directory>")
        return
    best_tree_filepath = './output/best_tree_file.json'
    dl = DataLoader('LocalInput/*.CSV')
    dl.load_data()
    tree_steps = get_steps(best_tree_filepath)

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

if __name__ == "__main__":
    main()