#!/usr/bin/env python

# http://pymotw.com/2/contextlib/

from __future__ import print_function

import win32wnet as wn
import win32netcon as nc

class ResourceEnumerator(object):
    """Blah, blah, blah, ..."""
    
    def __init__(self, scope, type_, usage):
        """Blah, blah, blah, ..."""
        self._scope = scope
        self._type = type_
        self._usage = usage

    def __iter__(self):
        """Blah, blah, blah, ..."""
        enum = wn.WNetOpenEnum(self._scope, self._type, self._usage, None)
        try:
            for rsrc in wn.WNetEnumResource(enum):
                yield rsrc
        finally:
            wn.WNetCloseEnum(enum)

def main():
    print("Begining...")
    scope = nc.RESOURCE_CONNECTED
    type_ = nc.RESOURCETYPE_DISK
    usage = nc.RESOURCEUSAGE_ALL
    for rsrc in ResourceEnumerator(scope, type_, usage):
        print("Resource:", rsrc.lpLocalName, rsrc.lpRemoteName)
    print("Finished!")

if __name__ == '__main__':
    main()

# EOF
