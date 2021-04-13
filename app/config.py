import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN=os.environ.get("BOT_TOKEN")
api_id=os.environ.get("API_ID")
api_hash=os.environ.get("API_HASH")
