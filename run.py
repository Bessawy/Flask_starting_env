from app import app
from dotenv import load_dotenv

if __name__ == "__main__":
    # Load env virables
    load_dotenv()
    app.run()