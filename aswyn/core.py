from flask import Flask
from .logger import LOGGER
import config


class app:
    def __init__(self):
        LOGGER(__name__).info("Starting Flask App...")
        self.app = Flask(__name__)
        self.config = config
        self.app.config["DEBUG"] = config.DEBUG
        self.app.config["SECRET_KEY"] = config.SECRET_KEY

    def start(self):
        LOGGER(__name__).info(f"Running Flask App on {self.config.HOST}:{self.config.PORT}")
        self.app.run(host=self.config.HOST, port=self.config.PORT)

    def stop(self):
        LOGGER(__name__).info("Stopping Flask App...")

    def register_blueprint(self, blueprint):
        self.app.register_blueprint(blueprint)