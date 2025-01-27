import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        logging.FileHandler("website_log.txt"), 
        logging.StreamHandler(), 
    ],
)

logging.getLogger("werkzeug").setLevel(logging.ERROR) 
logging.getLogger("httpx").setLevel(logging.ERROR)  
logging.getLogger("sqlalchemy").setLevel(logging.ERROR) 

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
