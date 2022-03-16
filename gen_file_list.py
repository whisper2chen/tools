#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import json

# this script generate sources (.c .h) from compile_command.json
# then source insight to add file from this list

# convert directory from linux to windows to make source insight happy
linux_dir = "/home/chentao/workspace"
win10_dir = "Z:"


def convert_source_file_path(path):
    path = path.replace(linux_dir, win10_dir)
    path = path.replace("/", "\\")
    return path


def convert_include_file_path(command):
    include_dirs = set()
    for item in command.split():
        if item.startswith("-I/"):
            path = item[2:].replace(linux_dir, win10_dir)
            path = path.replace("/", "\\")
            include_dirs.add(path)
    return include_dirs


def add_specific_include_dir(hint):
    if hint.endswith("hal\include"):
        print(hint+"\hal")
    print(hint)


def gen_file(json_file):
    source_files = set()
    include_dir = set()
    with open(json_file, "r") as f:
        data = json.load(f)
        for item in data:
            source_files.add(convert_source_file_path(item['file']))
            include_dir.update(convert_include_file_path(item['command']))
    for i in source_files:
        print(i)
    for i in include_dir:
        add_specific_include_dir(i)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(255)
    gen_file(sys.argv[1])
