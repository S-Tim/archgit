#!/usr/bin/env python3

# Creates a git blob from a string.
# An example of the format is:
# blob 25\u0000This is the README file.\n
#
# Author: Tim Silhan

import os
import sys
import zlib
from hashlib import sha1

content = 'Hello World\n'
if len(sys.argv) > 1:
    content = sys.argv[1]

print('Input: ', content)

header = f'blob {len(content)}\x00'
print('Header:', header)

store = header + content
print('Store:', store)

digest = sha1(store.encode('utf-8')).hexdigest()
print('Digest:', digest)
print('Dir:', digest[:2])
print('File:', digest[2:])

compressed = zlib.compress(store.encode('utf-8'))
print('\nCompressed:', compressed)

os.makedirs(os.path.dirname(f'.git/objects/{digest[:2]}/'))
with open(f'.git/objects/{digest[:2]}/{digest[2:]}', 'wb') as blob:
    blob.write(compressed)
