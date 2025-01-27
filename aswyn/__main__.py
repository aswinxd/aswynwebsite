import asyncio
import os
import importlib
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from flask import Flask
from aswyn import LOGGER  
from aswyn.plugins import ALL_MODULES  
app = Flask(__name__)
app.secret_key = os.urandom(24)
async def init():
    plugins_path = Path("aswyn/plugins")  
    for module_path in plugins_path.glob("*.py"):
        if module_path.stem == "__init__":
            continue 
        module_name = module_path.stem
        module = importlib.import_module(f"aswyn.plugins.{module_name}")
        if hasattr(module, "blueprint"):
            app.register_blueprint(module.blueprint)
    
    LOGGER("aswyn.plugins").info("Successfully imported and registered all plugins.")
    
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init())
    app.run(host="0.0.0.0", port=5000)
