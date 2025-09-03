import logging

""" Logs have different severity levels. Debug=10,Info=20,Warning=30,Error=40,Critical=50. 
By default Python will only log those with severity over 20, meaning Info will be skipped. We need to configure this for our needs.
We want our log file to be as complete as possible, so we confgure as DEBUG to show as much details as possbile.
On the other hand we don't want a bunch of logs in the console so we set it up as INFO to skip only DEBUG messages.
"""
class Logger:
    _configured = False

    @staticmethod
    def set_up():
        if Logger._configured:
            return
        
        logger = logging.getLogger("testsuite") #logger name can be anything
        logger.setLevel(logging.DEBUG)

        #File config
        fh = logging.FileHandler('testlog.log',mode='w')
        fh.setLevel(logging.DEBUG)

        # Format
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        fh.setFormatter(formatter)

        #Opctonal: console
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)
        Logger._configured = True

    @staticmethod
    def debug_msg(msg: str):
        logging.getLogger("testsuite").debug(msg)

    @staticmethod
    def info_msg(msg: str):
        logging.getLogger("testsuite").info(msg)

    @staticmethod
    def warning_msg(msg: str):
        logging.getLogger("testsuite").warning(msg)

    @staticmethod
    def error_msg(msg: str):
        logging.getLogger("testsuite").error(msg)
