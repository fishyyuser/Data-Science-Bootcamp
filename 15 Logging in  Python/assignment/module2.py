import math
import logging

logger = logging.getLogger('Scientific')
logger.propagate = True
class Scientific:

    @staticmethod
    def GCD(a, b):
        result = math.gcd(a, b)
        logger.debug(f"GCD({a}, {b}) = {result}")
        return result

    @staticmethod
    def SQRT(a):
        result = math.sqrt(a)
        logger.debug(f"SQRT({a}) = {result}")
        return result

    @staticmethod
    def sine(rad):
        result = math.sin(rad)
        logger.debug(f"sine({rad}) = {result}")
        return result