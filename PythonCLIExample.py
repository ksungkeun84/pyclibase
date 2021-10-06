
import argparse
from PythonCLIBase import PythonCLIBase


class PythonCLIExample(PythonCLIBase):
    def __init__(self, args):
        super().__init__(args)


    def runExample(self):
        cmd = 'ls -l'
        self.logger.info('Executing cmd: {0}'.format(cmd))
        super().execute_cmd('ls -l')


def main(args):
    pythonCLIExample = PythonCLIExample(args)
    pythonCLIExample.runExample()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description="PythonCLIExample Program")

    #parser.add_argument("-l", "--llvm-path",
    #        type=str, help="Path to llvm binaries", required=True)
    #parser.add_argument("-r", "--build-path",
    #        type=str, help="Path to build", required=True)
    #parser.add_argument("-o", "--output-path",
    #        type=str, help="Path to output of dot file", required=True)

    args = parser.parse_args()
    main(args)
