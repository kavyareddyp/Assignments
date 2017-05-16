"""
69.Bulk file copy.Take source and destination file paths from a file and copy the source file content into destination file.
Maintain configuration file and put the below fields there
Source not found: Skip the copy
destination found: skip/replace
maintain a remarks log. What are the files skiped from copy because no source file found. 
What are the files skip/replaced because of destination file foun in the specified path
"""
import sys
import os
import shutil
with open('remarks.log','w') as log:
            log.write('')
with open("files.txt") as f:
    files = f.readlines()
    for i in files[1:]:
        j = i.split(" ")
        source = j[0]
        x = j[1].split('\n')
        dest = x[0]
        if os.path.exists(source):
           if os.path.exists(dest):
                with open('config.txt','r') as conf:
                    data = conf.readlines()
                print data[1]
                opt = raw_input()
                if opt.lower() == 'skip':
                    print "As user input file copy is skipped"
                    with open('remarks.log','a') as log:
                        log.write('File {} skipped from copy\n'.format(dest))
                else:
                    print "copied the content from source to dest"
                    shutil.copy(source, dest)
                    with open('remarks.log','a') as log:
                        log.write('File {} copied because destination file found\n'.format(dest))
           else:
                print "destination not found so skipped the copy"
                with open('remarks.log','a') as log:
                        log.write('File {} skipped from copy because no destination file found\n'.format(dest))
        else:
            with open('config.txt','r') as conf:
                data = conf.readlines()
            print data[0]
            with open('remarks.log','a') as log:
                log.write('File {} skipped from copy because no source file found\n'.format(source))
                
