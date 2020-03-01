#!/usr/bin/python

from jinja2 import Template, FileSystemLoader, Environment
import os.path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", help="source jinja2 template")
args = parser.parse_args()

def usage():
    print("Usage: TODO", file=sys.stderr)

if args.file:
    filename = args.file
    if os.path.exists(filename) and os.path.isfile(filename):
        templateLoader = FileSystemLoader(searchpath=os.path.dirname(filename))
        templateEnv = Environment(loader=templateLoader)
        templateFile = os.path.basename(filename)
        template = templateEnv.get_template(templateFile)
        print("# DO NOT EDIT this auto-generated file - edit template:", filename)
        print(template.render())
    else:
        print("File not found!", file=sys.stderr)
        exit(1)
else:
    usage()
