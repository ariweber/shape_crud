import logging


def create_log(filename="shape.log"):
    logger = logging.getLogger(filename)
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    handler = logging.FileHandler(filename, encoding="utf-8")
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
