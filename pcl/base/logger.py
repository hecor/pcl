#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging, os


class Logger:
    logger = None

    @classmethod
    def init_logging(cls, name, log_file_path = None, console = True):
        logging.ColorFormatter = ColorFormatter
        cls.logger = logging.getLogger(name)
        cls.logger.setLevel(logging.DEBUG)
        cls.logger.propagate = False

        if console:
            fh = logging.StreamHandler()
            fh.setLevel(logging.DEBUG)
            formatter = logging.ColorFormatter("%%(asctime)s [%s] [%%(levelname)s] %%(message)s" %(name))
            fh.setFormatter(formatter)
            cls.logger.addHandler(fh)

        if log_file_path:
            if os.path.isdir(log_file_path):
                # by day
                fh = logging.TimedRotatingFileHandler(log_file_path, backupCount=30, when='D')
                fh.suffix = "%Y-%m-%d"
                # by hour
                #fh = TimedRotatingFileHandler(log_file_path, backupCount=24*7, when='H')
                #fh.suffix = "%Y%m%d%H"
                #fh.extMatch = re.compile(r"^\d{4}\d{2}\d{2}\d{2}$")
            else:
                fh = logging.FileHandler(log_file_path)

            fh.setLevel(logging.DEBUG)
            formatter = logging.Formatter("%(asctime)s [%(filename)s] [%(levelname)s] %(message)s")
            fh.setFormatter(formatter)
            cls.logger.addHandler(fh)

    
    @classmethod
    def info(cls, msg):
        cls.logger.info(msg)

    @classmethod
    def debug(cls, msg):
        cls.logger.debug(msg)

    @classmethod
    def error(cls, msg):
        cls.logger.error(msg)
        
    @classmethod
    def critical(cls, msg):
        cls.logger.critical(msg)


class ColorFormatter(logging.Formatter):
    '''
    cool class
    '''
    Black            = '0;30'
    Red              = '0;31'
    Green            = '0;32'
    Brown            = '0;33'
    Blue             = '0;34'
    Purple           = '0;35'
    Cyan             = '0;36'
    Light_Gray       = '0;37'

    Dark_Gray        = '1;30'
    Light_Red        = '1;31'
    Light_Green      = '1;32'
    Yellow           = '1;33'
    Light_Blue       = '1;34'
    Light_Purple     = '1;35'
    Light_Cyan       = '1;36'
    White            = '1;37'

    COLORS = {
        'DEBUG'    : Dark_Gray, #WHITE
        'INFO'     : Light_Blue,
        'NOTICE'   : Light_Green,
        'WARNING'  : Yellow,
        'ERROR'    : Light_Red,
        'CRITICAL' : Yellow,
    }

    RESET_SEQ = "\033[0m"
    COLOR_SEQ = "\033[%sm"
    BOLD_SEQ  = "\033[1m"


    def __init__(self, *args, **kwargs):
        # can't do super(...) here because Formatter is an old school class
        logging.Formatter.__init__(self, *args, **kwargs)

    def format(self, record):
        levelname = record.levelname
        color     = ColorFormatter.COLOR_SEQ % (ColorFormatter.COLORS[levelname])
        message   = logging.Formatter.format(self, record)
        return color + message + ColorFormatter.RESET_SEQ



