#!/usr/bin/python3
""" __init__ models directory's magic method """
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
