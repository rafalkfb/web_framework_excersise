import inspect
import logging


def custom_log(log_level=logging.DEBUG):
    # gets the name of the class / method from where this method is called
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)

    # by default, log all messages
    logger.setLevel(logging.DEBUG)

    # below is if you wish to log every class to different files
    # file_handler = logging.FileHandler("{0}.log".format(logger_name), mode='w')
    file_handler = logging.FileHandler("automation.log".format(logger_name), mode='a')
    file_handler.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
