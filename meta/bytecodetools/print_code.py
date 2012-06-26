'''
Created on May 10, 2012

@author: sean
'''
from .bytecode_consumer import ByteCodeConsumer

class ByteCodePrinter(ByteCodeConsumer):

    def generic_consume(self, instr):
        print instr

def main():
    try:
        from argparse import ArgumentParser
    except ImportError:
        print 'Python 2.7 required for argparse'
        return
    parser = ArgumentParser()
    parser.add_argument()

if __name__ == '__main__':
    main()
