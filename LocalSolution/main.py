from DataLoader import DataLoader
def main():
    # entrypoint
    dl = DataLoader('LocalInput/*.CSV')
    dl.load_data()
    

if __name__ == "__main__":
    main()