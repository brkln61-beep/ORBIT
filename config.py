import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "ORBIT")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
VERSION = os.getenv("VERSION", "0.1.0")