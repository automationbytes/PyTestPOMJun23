import logging

class LogGenerator:

    @staticmethod
    def loggen():
        logger = logging.getLogger()
        fhandler = logging.FileHandler("./Logs/demo.log","w")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger