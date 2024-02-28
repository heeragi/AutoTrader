from dotenv import load_dotenv, find_dotenv

from src.engine.v1 import run

if __name__ == '__main__':
    load_dotenv(find_dotenv())
    run()