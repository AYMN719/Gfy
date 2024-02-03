import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6863593658:AAG_w2gQP0EqipwblNbaf_MkMSTvI-zNnow")

    APP_ID = int(os.environ.get("APP_ID", 27035698))

    API_HASH = os.environ.get("API_HASH", "160b55b0989039875a61e45d8cc57c95")
