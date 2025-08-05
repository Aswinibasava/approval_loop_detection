import logging

def setup_logger():
    logger = logging.getLogger("loop-detector")
    if not logger.handlers:
        handler = logging.FileHandler("loop_detector.log")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger
