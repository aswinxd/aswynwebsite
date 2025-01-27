import asyncio
import importlib
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from flask import Flask
from aswyn import LOGGER 
from aswyn import app  
from concurrent.futures import ThreadPoolExecutor
from aswyn.plugins import ALL_MODULES  

executor = ThreadPoolExecutor(max_workers=200)

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
    app.run()