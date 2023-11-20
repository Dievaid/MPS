import csv
from sys import argv
import csv

def read_csv_file(file_path):
    data_2d_array = []

    try:
        with open(file_path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            
            for row in csv_reader:
                data_2d_array.append(row)
                
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
    except Exception as e:
        print(f"Error: {e}")

    return data_2d_array
def main():
    file_path = './GlobalInput/LUTTrain.csv'
    data = read_csv_file(file_path)
    if data:
        print("Data from CSV file:")
        row = int(argv[1])
        col = int(argv[2])
        print(f"Elem at data[{row}][{col}]: {data[row][col]}")    

    
    
if __name__ == "__main__":
    main()