import asyncio
import importlib
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from flask import Flask
from aswyne import LOGGER 
from aswyne.app import app  
from aswyne.plugins import ALL_MODULES  

executor = ThreadPoolExecutor(max_workers=200)

async def init():
    plugins_path = Path("aswyne/plugins")  
    for module_path in plugins_path.glob("*.py"):
        if module_path.stem == "__init__":
            continue 
        module_name = module_path.stem
        module = importlib.import_module(f"aswyne.plugins.{module_name}")
        if hasattr(module, "blueprint"):
            app.register_blueprint(module.blueprint)
    
    LOGGER("aswyne.plugins").info("Successfully imported and registered all plugins.")
    loop = asyncio.get_event_loop()
    loop.run_in_executor(executor, app.run, {"host": "0.0.0.0", "port": 5000})

if __name__ == "__main__":
    try:
        asyncio.get_event_loop().run_until_complete(init())
    except KeyboardInterrupt:
        LOGGER("aswyne").info("Stopping the website...")
