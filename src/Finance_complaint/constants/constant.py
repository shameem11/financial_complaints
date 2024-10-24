from dataclasses import dataclass
from datatime import datetime # type: ignore
import os

TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")

@dataclass
class Enviromentveriables:
    mongo_db_uri = os.getenv("MONGO_DB_URL")

env_var = Enviromentveriables()

