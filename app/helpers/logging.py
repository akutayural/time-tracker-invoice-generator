import logging


class Logging:
    def __init__(self, name):
        self.logger = logging.getLogger(name=name)
        self.logger.setLevel(logging.DEBUG)
        self.__set_conf()

    def get_logger(self):
        return self.logger

    def __set_conf(self):
        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        self.logger.addHandler(ch)
