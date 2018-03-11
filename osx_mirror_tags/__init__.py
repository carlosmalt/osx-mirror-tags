'''
Mirror Finder tags in OS X from src directory tree to a mirrored dst directory tree (assuming all paths in src also exist in dst). 

Example use: When switching from the old version of Google Drive to Google File Stream's "My Drive", this program copies all Finder tags from files and directories in Google Drive to My Drive (Tip: use "/Volumes/GoogleDrive/My Drive" as destination). This also works when none of My Drive's files are actually downloaded.
'''

import os
import sys
from osx_tags import * # https://github.com/scooby/osx-tags

def transferTags(src, dst):
        t = Tags(src)
        tags = t.read()
        if tags:
                t = Tags(dst)
                apply(t.write, list(tags))  

def walk(srcDir, dstDir):
        for (root, dirs, files) in os.walk(srcDir):
                prefix = os.path.commonprefix((root, srcDir))
                if prefix == root:
                         transferTags(srcDir, dstDir)
                         for f in files:
                                 transferTags('%s/%s' % (srcDir, f), '%s/%s' % (dstDir, f))
                else:
                        tail = root[len(prefix):]
                        tail = tail.strip('/')
                        transferTags('%s/%s' % (srcDir, tail), '%s/%s' % (dstDir, tail))
                        for f in files:
                                transferTags('%s/%s/%s' % (srcDir, tail, f), '%s/%s/%s' % (dstDir, tail, f))
                        
if __name__ == '__main__':
        srcDir = sys.argv[1]
        dstDir = sys.argv[2]
        walk(srcDir, dstDir)