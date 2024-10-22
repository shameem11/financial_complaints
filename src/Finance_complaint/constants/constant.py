from dataclasses import dataclass
from datatime import datetime # type: ignore
import os

@dataclass
class Enviromentveriables:
    mongo_db_uri = os.getenv("MONGO_DB_URL")

env_var = Enviromentveriables()

