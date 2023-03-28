import uvicorn
from fastapi import FastAPI
from app.environment import Environment

if __name__ == "__main__":
    env = Environment()
    env.configuration.init()
    env.db_conn.init_connection()
    app = FastAPI()
    for handler in env.get_handlers():
        app.add_api_route(path=handler.path, endpoint=handler.callback_handler, methods=handler.method)
    uvicorn.run(app, host="0.0.0.0", port=8000)