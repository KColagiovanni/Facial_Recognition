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
        print('Please include the path to the directory and only the path to '
              'the directory where the images are located as an argument.')
        sys.exit(1)

    BASE_PATH=sys.argv[1]
    SEPARATOR=";"

    file_to_write = open('faces.txt', 'w')

    label = 0
    dirname_dict = {}
    for dirname, dirnames, filenames in os.walk(BASE_PATH):
        if len(dirname) > 0:
            dir_count = 0
            for dir in dirnames:
                dirname_dict[dir] = dir_count
                dir_count += 1
        for subdirname in dirnames:
            subject_path = os.path.join(dirname, subdirname)
            print(f'subject_path is: {subject_path}')
            for filename in os.listdir(subject_path):
                abs_path = "%s/%s" % (subject_path, filename)
                # print(f'Path is: {abs_path}{SEPARATOR}{label}')
                file_to_write.write(f'{abs_path}{SEPARATOR}{label}\n')
            label = label + 1

    file_to_write.close()