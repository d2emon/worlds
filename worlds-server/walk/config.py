import os
from config import Config as FlaskConfig


class Config:
    UAF_RAND = os.path.join(FlaskConfig.MEDIA_FOLDER, "uaf.rand")
    ROOMS = os.path.join(FlaskConfig.MEDIA_FOLDER, "TEXT/ROOMS/")
    LOG_FILE = os.path.join(FlaskConfig.MEDIA_FOLDER, "mud_syslog")
    BAN_FILE = os.path.join(FlaskConfig.MEDIA_FOLDER, "banned_file")
    NOLOGIN = os.path.join(FlaskConfig.MEDIA_FOLDER, "nologin")
    RESET_T = os.path.join(FlaskConfig.MEDIA_FOLDER, "reset_t")
    RESET_N = os.path.join(FlaskConfig.MEDIA_FOLDER, "reset_n")
    RESET_DATA = os.path.join(FlaskConfig.MEDIA_FOLDER, "reset_data")
    MOTD = os.path.join(FlaskConfig.MEDIA_FOLDER, "TEXT/gmotd2")
    GWIZ = os.path.join(FlaskConfig.MEDIA_FOLDER, "TEXT/gwiz")
    HELP1 = os.path.join(FlaskConfig.MEDIA_FOLDER, "TEXT/help1")
    HELP2 = os.path.join(FlaskConfig.MEDIA_FOLDER, "TEXT/help2")
    HELP3 = os.path.join(FlaskConfig.MEDIA_FOLDER, "TEXT/help3")
    WIZLIST = os.path.join(FlaskConfig.MEDIA_FOLDER, "TEXT/wiz.list")
    CREDITS = os.path.join(FlaskConfig.MEDIA_FOLDER, "TEXT/credits")
    EXAMINES = os.path.join(FlaskConfig.MEDIA_FOLDER, "EXAMINES/")
    LEVELS = os.path.join(FlaskConfig.MEDIA_FOLDER, "TEXT/level.txt")
    PFL = os.path.join(FlaskConfig.MEDIA_FOLDER, "user_file")
    PFT = os.path.join(FlaskConfig.MEDIA_FOLDER, "user_file.b")
    EXE = os.path.join(FlaskConfig.MEDIA_FOLDER, "mud.exe")
    EXE2 = os.path.join(FlaskConfig.MEDIA_FOLDER, "mud.1")
    SNOOP = os.path.join(FlaskConfig.MEDIA_FOLDER, "SNOOP/")
    HOST_MACHINE = "HOST_MACHINE"
