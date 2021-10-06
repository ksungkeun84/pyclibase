import argparse
import subprocess
import logging
import os
import sys 

class PythonCLIBase(object):
    def __init__(self, args):
        self.logger = None
        self.args = args

        self.initLogger()

    def initLogger(self):
        # Create logger
        self.logger = logging.getLogger('PythonCLIBase')
        self.logger.setLevel(logging.DEBUG)

        # Create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # Create formatter
        formatter = logging.Formatter('[%(asctime)s][%(name)s][%(levelname)s]: %(message)s')

        # Add formatter to ch
        ch.setFormatter(formatter)

        # Add ch to logger
        self.logger.addHandler(ch)


    @staticmethod
    def execute_cmd(cmd:str):
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
                line = ps.stdout.readline().decode('utf-8')
                sys.stdout.write(line)
                sys.stdout.flush()
            except UnicodeEncodeError as err:
                self.logger.error("\nException occured while trying to print line.\n{0}".format(err))
            if retcode is not None and line == '':
                break

        return ps.returncode



