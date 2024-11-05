import asyncio
import os
import sys
import time


from utils.shared.next_step import next_step
from utils.shared.sanitize_filename import sanitize_filename

from config.config import *
from logger.logger import Logger
from llm_engine.llm_engine import LlmEngine

logger = Logger(logger_name=__name__)


async def main():

    logger.info("Begin __main__")
    logger.info("Insert program logic here...",t=5)
    logger.info("End __main__")
    sys.exit(0)


if __name__ == "__main__":
    import os
    base_name = os.path.basename(__file__) 
    program_name = os.path.split(os.path.split(__file__)[0])[1] if base_name != "main.py" else os.path.splitext(base_name)[0] 
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"'{program_name}' program stopped.")






















