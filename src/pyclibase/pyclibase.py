import argparse
import subprocess
import logging
import warnings
import os
import sys

from rich.logging import RichHandler
from rich import traceback
from rich import print
from pyfiglet import Figlet
import pyfiglet

log = None
def init_pycli(title, logger_name, log_file_name):
    os.system('cls' if os.name == 'nt' else 'clear')
    global log
    title = pyfiglet.figlet_format(title, font='slant')
    print(f'[blue]{title}[/blue]')
    FORMAT = "%(message)s"
    #logging.basicConfig(format=FORMAT, datefmt="[%X]", level="NOTSET", handlers=[RichHandler(rich_tracebacks=True, markup=True)], filename=logger_name)
    logging.basicConfig(format=FORMAT, datefmt="[%X]", level="NOTSET", filename=logger_name)
    traceback.install()

    log = logging.getLogger(logger_name)
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    file_handler = logging.FileHandler(log_file_name)
    file_handler.setFormatter(formatter)
    log.addHandler(file_handler)

class pyclibase(object):
    def __init__(self, args, name):
        self.args = args
        self.name = name
        self.format= "%(message)s"

    def execute_cmd(self, cmd:str):
        """Run shell command
        Args:
            cmd (string): The shell command to execute
        Returns:
            stderr and error code
        """
        # Run command

        log.info('Executing cmd: {0}'.format(cmd))
        ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, executable='/bin/bash')
        while True:
            retcode = ps.poll()
            # THIS TRY, EXCEPT IS ADDED AS PRINT LINE MIGHT FAIL RANDOMLY FOR UNICODEENCODEERROR
            try:
                line = ps.stdout.readline().decode('ISO-8859-1')
                log.info(line.strip())
            except UnicodeEncodeError as err:
                log.error("\nException occured while trying to print line.\n{0}".format(err))
            if retcode is not None and line == '':
                break

        return ps.returncode

    def execute_cmd_get_output(self, cmd:str):
        output = None
        try:
            log.info('Executing cmd: {0}'.format(cmd))
            output = subprocess.check_output(cmd, timeout=60*60, shell=True, stderr=subprocess.DEVNULL)
        except Exception as generic_exception:
            log.error('Caught Exception: {}'.format(generic_exception))

        return output
