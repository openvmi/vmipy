import sys

sys.path.append('../src')

from vmilog import getLogger, LogLevelEnum, setLoggerLevel

def main():
    mylogger = getLogger(enableConsole=True, logLevel=LogLevelEnum.debug)
    mylogger.info("hello, from info")
    mylogger.debug("hello, from debug")
    mylogger.warning("hello, from warn")
    mylogger.error("hello, from error")

if __name__ == "__main__":
    main()