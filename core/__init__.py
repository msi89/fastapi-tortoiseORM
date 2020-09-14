from fastapi import FastAPI
from core.register import register_tortoise

from core import settings

app = FastAPI()

register_tortoise(
    app,
    config=settings.TORTOISE_ORM,
    generate_schemas=False
)


# @app.on_event('startup')
# async def startup():
#     await Tortoise.init()
#     logging.info('Tortoise-ORM started, %s, %s',
#                  Tortoise._connections, Tortoise.apps)
#     if generate_schemas:
#         logging.info('Tortoise-ORM generating schema.')
#         await Tortoise.generate_schemas()


# @app.on_event('shutdown')
# async def shutdown():
#     await Tortoise.close_connections()
#     logging.info('Tortoise-ORM shutting down.')
