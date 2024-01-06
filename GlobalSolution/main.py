import sys
import DataLoader as dl
import logging
import generator


def setup_logger():
    # Create a logger
    logger = logging.getLogger("mps_logger")
    
    # If the logger already has handlers, don't add more
    if not logger.handlers:
        logger.setLevel(logging.INFO)

        # Create a file handler and set the level to INFO
        file_handler = logging.FileHandler("mps.log")
        file_handler.setLevel(logging.INFO)

        # Create a formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Add the formatter to the file handler
        file_handler.setFormatter(formatter)

        # Add the file handler to the logger
        logger.addHandler(file_handler)

    return logger


def main():
    logger = setup_logger()
    
    if len(sys.argv) <= 2:
        print("Usage: python3 main.py <GlobalTrain_filepath> <LUTTrain_filepath>")
        logger.error(f"Incorrect usage. Arguments: {sys.argv[1:]}")
        return
    
    globaltrain_filepath = str(sys.argv[1])
    logger.info(f"The path to GlobalTrain.csv: {globaltrain_filepath}")
    
    luttrain_filepath = str(sys.argv[2])
    logger.info(f"The path to LUTTrain.csv: {globaltrain_filepath}")
    

    data_loader = dl.DataLoader(globaltrain_filepath, luttrain_filepath)
    data_loader.load_data()
    logger.info(f"{data_loader.globaltrain_data}")
    logger.info(f"{data_loader.luttrain_data}")

    # Predictor generates a json
    g = generator.Generator(data_loader)
    g.generate_solution_tree()
    g.save_best_iteration_to_json('./output/output_file.json', \
        '../LocalSolution/output/best_tree_file.json')
    
    
if __name__ == "__main__":
    main()