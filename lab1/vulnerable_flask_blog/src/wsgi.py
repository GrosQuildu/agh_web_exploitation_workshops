from app import app
from blog import seed

if __name__ == "__main__":
    seed()
    app.run()