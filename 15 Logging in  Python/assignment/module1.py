import logging

logger = logging.getLogger('Arithmatic')
logger.propagate = True

class Arithmetic:

    @staticmethod
    def add(a,b):
        result=a+b
        logger.debug(f"add({a}, {b}) = {result}")
        return result

    @staticmethod
    def subtraction(a,b):
        result=a-b
        logger.debug(f"subtraction({a}, {b}) = {result}")
        return result

    @staticmethod
    def multiplication(a,b):
        result=a*b
        logger.debug(f"multiplication({a}, {b}) = {result}")
        return result

    @staticmethod
    def divison(a,b):
        try:
            result=a/b
            logger.debug(f"division({a}, {b}) = {result}")
            return result
        except ZeroDivisionError:
            logger.exception("Division by zero error")
            return None

