#!/usr/bin/env python

def mangle_string(string):
    """
    Turns an arbitrary string into a decent foldername/filename
    (no underscores allowed)!
    """
    string = string.replace(' ', '-')
    string = string.strip(",./;'[]\|_=+<>?:{}!@#$%^&*()`~")
    string = string.strip('"')

    return string

