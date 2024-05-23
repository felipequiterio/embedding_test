import uvicorn

from utils.log import get_custom_logger

logger = get_custom_logger('SERVER')
logger.info('Starting server...')
# http://localhost:9000/docs#/

if __name__ == '__main__':
    uvicorn.run("server:app", port=9000, host="0.0.0.0", reload=True)
