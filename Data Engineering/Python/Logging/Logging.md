# Logging

Logging is essential in Python code. It is important so that you can track back and see where a certain piece of code has gone wrong in some cases. 

The usual amateur practice of using `print()` blocks to output results are okay but that's not the best practice when it comes to scalable, productionized code in team environments. 

The library used is `logging`. And the below is how you define a simple logger object which then later can be used to add log messages.

```python
import logging

def logging_init():
    logging.basicConfig(
        level=logging.DEBUG, 
        filename = "sample.log", 
        filemode='w',
        format = "%(asctime)s - %(levelname)s - %(message)s"
    ) #can only run once. So run at the beginning of the program
```

There are a few key parameters to set here.

1. `level`- The level of logs you wish to log. Logging has 5 different levels as below.
    - DEBUG
    - INFO
    - CRITICAL
    - WARNING
    - ERROR
2. `filename`- The file name with location where all the logs will be written into
3. `filemode`- To overwrite the log file each time the logger is invoked, use 'w'. To append use 'a'
4. `format`- This is how the log file will log each message. First the time, then log level, then the messae. This format can be customized as you want.

## Example 01

```python
def logging_init():
    logging.basicConfig(level=logging.DEBUG, filename = "sample.log", filemode='w',
    format = "%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging_init() # Initiating the logger object

    x = 5

    logging.debug(f"Value of x is {x}") # Result in a log message in the log  file

    try:
        1/0
    except ZeroDivisionError as e:
        logging.error("ZeroDivisionError", exc_info = True)
        logging.exception("ZeroDivisionError") #Much easier to use this one

    logging.debug("Debug") # Will add a log message as "Debug", level as DEBUG
    logging.info("info") # Will add a log message as "info", level as INFO
    logging.warning("WARNING")
    logging.critical("CRITICAL!")
    logging.error("ERROR")


if __name__ == "__main__":
    main()
```

## Example 02

Another different way of instantiating the logger object to work with

```python
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
```