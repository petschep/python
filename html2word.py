import os
import sys
import pypandoc
path = input("Please enter something: ")
for root, subdirs, files in os.walk(path):

    for file in os.listdir(root):

        filePath = os.path.join(root, file)

        if os.path.isdir(filePath):
            pass

        else:
            f = open (filePath, 'r')
            if file.endswith('.html'):
                fname = filePath
                # parse the html as you wish
                output = pypandoc.convert_file(fname, 'docx',outputfile=fname+".docx")
                assert output == ""