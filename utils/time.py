import logging
from datetime import datetime
from functools import wraps

from utils.log import get_custom_logger

# Custom logger setup
logger = get_custom_logger('TIME')


def log_time(message):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            result = func(*args, **kwargs)
            end_time = datetime.now()
            logger.info(f'{message} - Time taken: {end_time - start_time}')
            return result

        return wrapper

    return decorator
