#!/bin/env python3

"""

Docstring goes here

"""
import _version

PROG_NAME = 'SubDomScan'
AUTHOR = 'Taylor-Jayde Blackstone <t.blackstone@inspyre.tech>'
LICENSE = 'MIT'
DESCRIPTION = 'Scans output files from SubDomSpy scans to see what hosts respond to pings.'
VERSION = 1.0

banner_attrs = [f'Name: {PROG_NAME}', f'Author: {AUTHOR}', f'Version: {VERSION}',
                f'License: {LICENSE}', f'Description: {DESCRIPTION}']


def banner():
    for attr in banner_attrs:
        print(attr)


def parse_args():
    from argparse import ArgumentParser

    parser = ArgumentParser(
            prog=f'{PROG_NAME}',
            description=DESCRIPTION
    )

    verbosity_parser = parser.add_mutually_exclusive_group()
    verbosity_parser.add_argument('-v', '--verbose',
                                  action='store_true',
                                  required=False,
                                  dest='verbose',
                                  default=False,
                                  help='Instructs the program to output verbosely.')

    verbosity_parser.add_argument('-d', '--debug',
                                  action='store_true',
                                  required=False,
                                  dest='debug',
                                  default=False,
                                  help='Instructs the program to output all output it can.')

    verbosity_parser.add_argument('-q', '--quiet',
                                  action='store_true',
                                  required=False,
                                  dest='quiet',
                                  default=False,
                                  help='Instructs the program to suppress all but the most critical output')

    return parser.parse_args()


def ping_host(address):
    pass


def main():
    args = parse_args()

    if not args.quiet:
        banner()


if __name__ == '__main__':
    main()
