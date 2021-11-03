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

class pyclibase(object):
    def __init__(self, args, name):
        self.logger = None
        self.args = args
        self.name = name
        self.format= "%(message)s"
        self.initLogger()
        self.printTitle()

    def initLogger(self):
        # Create logger
        logging.basicConfig(
                format=self.format,
                datefmt="[%X]",
                level="NOTSET",
                handlers=[RichHandler(rich_tracebacks=True, markup=True)]
        )
        self.logger = logging.getLogger(self.name)
        traceback.install()

        # Filter out this warning about Rich TQDM progress bars
        warnings.filterwarnings("ignore", message="rich is experimental/alpha")
        #self.logger.setLevel(logging.DEBUG)

        # Create console handler and set level to debug
        #ch = logging.StreamHandler()
        #ch.setLevel(logging.DEBUG)

        # Create formatter
        #formatter = logging.Formatter('[%(asctime)s][%(name)s][%(levelname)s]: %(message)s')

        # Add formatter to ch
        #ch.setFormatter(formatter)

        # Add ch to logger
        #self.logger.addHandler(ch)

    def printTitle(self):
        pass
        #title = pyfiglet.figlet_format(self.name, font='slant')
        #print(f'[blue]{title}[/blue]')
        #custom_fig = Figlet(font='graffiti')
        #print(custom_fig.renderText(self.name))


    def execute_cmd(self, cmd:str):
        """Run shell command
        Args:
            cmd (string): The shell command to execute
        Returns:
            stderr and error code
        """
        # Run command

        ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, executable='/bin/bash')
        while True:
            retcode = ps.poll()
            # THIS TRY, EXCEPT IS ADDED AS PRINT LINE MIGHT FAIL RANDOMLY FOR UNICODEENCODEERROR
            try:
                line = ps.stdout.readline().decode('ISO-8859-1')
                self.logger.info(line)
                #sys.stdout.write(line)
                #sys.stdout.flush()
            except UnicodeEncodeError as err:
                self.logger.error("\nException occured while trying to print line.\n{0}".format(err))
            if retcode is not None and line == '':
                break

        return ps.returncode

    def execute_cmd_get_output(self, cmd:str):
        output = None
        try:
            output = subprocess.check_output(cmd, timeout=60*60, shell=True, stderr=subprocess.DEVNULL)
        except Exception as generic_exception:
            self.logger.error('Caught Exception: {}'.format(generic_exception))

        return output
