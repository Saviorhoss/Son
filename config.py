import os
API_ID = int(os.getenv("API_ID", 14699743))
API_HASH = os.getenv("API_HASH", "0cef89ed2c8025c16d2b4d42a1b8d792")
BOT_TOKEN = os.getenv("BOT_TOKEN", "5585143449:AAF_SWZKSBTA6KwzdmewPamUJPQqDcgL07M")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://nohari3255:lK4QeDDOZKefymH0@cluster0.rka3l8x.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = list({int(x) for x in os.environ.get("OWNER_ID", "5059280908").split()})
