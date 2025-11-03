import logging

def logging_init():
    logging.basicConfig(level=logging.DEBUG, filename = "sample.log", filemode='w',
    format = "%(asctime)s - %(levelname)s - %(message)s") #can only run once. So run at the beginning of the program

def main():
    logging_init()

    x = 5

    logging.debug(f"Value of x is {x}")

    try:
        1/0
    except ZeroDivisionError as e:
        # logging.error("ZeroDivisionError", exc_info = True)
        logging.exception("ZeroDivisionError") #Much easier to use this one

    # logging.debug("Debug")
    # logging.info("info")
    # logging.warning("WARNING")
    # logging.critical("CRITICAL!")
    # logging.error("ERROR")


if __name__ == "__main__":
    main()
