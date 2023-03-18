import os
import dotenv


PATH_TO_ENV = os.path.join(os.path.dirname(__file__), ".env")
dotenv.load_dotenv(PATH_TO_ENV)

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
print(TELEGRAM_BOT_TOKEN)

