
APP_NAME = "FastAPI"

DEBUG = True

TORTOISE_ORM = {
    "connections": {
        # "default": "sqlite://db.sqlite3",
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": "localhost",
                "port": "5432",
                "user": "ckam",
                "password": "123456",
                "database": "fastapi_tortoise"
            }
        },
    },
    "apps": {
        "models": {
            "models": [
                "events.models",
                "accounts.models",
                # "blog.models",
                "aerich.models"
            ],
            "default_connection": "default",
        },
    }
}

# DATABASE_URI = "postgresql://user:password@localhost:5432/db"
