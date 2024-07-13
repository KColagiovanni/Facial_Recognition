# Source: https://docs.opencv.org/4.x/da/d60/tutorial_face_main.html
#!/usr/bin/env python

import sys
import os.path

# This is a tiny script to create a CSV file from a face database with a similar hierarchy:
#
#  philipp@mango:~/facerec/data/at$ tree
#  .
#  |-- README
#  |-- s1
#  |   |-- 1.pgm
#  |   |-- ...
#  |   |-- 10.pgm
#  |-- s2
#  |   |-- 1.pgm
#  |   |-- ...
#  |   |-- 10.pgm
#  ...
#  |-- s40
#  |   |-- 1.pgm
#  |   |-- ...
#  |   |-- 10.pgm
#

if __name__ == "__main__":

    print(sys.argv)

    if len(sys.argv) != 2:
        print("usage: create_csv <base_path>")
        sys.exit(1)

    BASE_PATH=sys.argv[1]
    SEPARATOR=";"

    print(f'BASE_PATH is: {BASE_PATH}')

    label = 0
    for dirname, dirnames, filenames in os.walk(BASE_PATH):
        print(f'dirname is: {dirname}')
        print(f'dirnames is: {dirnames}')
        print(f'filenames is: {filenames}')
        for subdirname in dirnames:
            subject_path = os.path.join(dirname, subdirname)
            print(f'subject_path is: {subject_path}')
            for filename in os.listdir(subject_path):
                abs_path = "%s/%s" % (subject_path, filename)
                print(f'Path is: {abs_path}{SEPARATOR}{label}')
            label = label + 1