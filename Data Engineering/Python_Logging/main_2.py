import logging

def logging_init():
    logging.basicConfig(level=logging.DEBUG, filename = "sample.log", filemode='w',
    format = "%(asctime)s - %(levelname)s - %(message)s") #can only run once. So run at the beginning of the program

def main():
    logging_init()

    logger = logging.getLogger(__name__) #Creating a logger for this module specifically. But you need to configure a handler to write it to a separate file
    file_handler = logging.FileHandler("sample_2.log")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.info("Testing the custom logger")


if __name__ == "__main__":
    main()
