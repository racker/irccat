#!/usr/bin/python
import os, sys, re, subprocess

path = '/usr/share/irccat/'

args = sys.argv[1]
bits = args.split(' ')
command = bits[3]

found = False
if re.match('^[a-z0-9]+$', command):
    for file in os.listdir(path):

        if re.match('^%s\.[a-z]+$' % command, file):
            found = True
            
            procArgs = [path + file]
            procArgs.extend(bits)
            proc = subprocess.Popen(procArgs, stdout=subprocess.PIPE)
            stdout = proc.stdout

            while True:
                # We do this to avoid buffering from the subprocess stdout
                print os.read(stdout.fileno(), 65536),
                sys.stdout.flush()

                if proc.poll() != None:
                    break

if found == False:
    print "Unknown command '%s'" % command
