#!/usr/bin/env python3

# Creates a git blob from a string.
# An example of the format is:
# blob 25\u0000This is the README file.\n
#
# Author: Tim Silhan

import sys
import zlib
from hashlib import sha1
from run_commands import run_command

content = 'Hello World\n'
if len(sys.argv) > 1:
    content = sys.argv[1]

print('Input: ', content)

header = f'blob {len(content)}\u0000'
print('Header:', header)

store = header + content
print('Store:', store)

digest = sha1(store.encode('utf-8')).hexdigest()
print('Digest:', digest)
print('Dir:', digest[:2])
print('File:', digest[2:])

compressed = zlib.compress(store.encode('utf-8'))
print('\nCompressed:', compressed)

run_command(f'mkdir -p .git/objects/{digest[:2]}')
with open(f'.git/objects/{digest[:2]}/{digest[2:]}', 'wb') as blob:
    blob.write(compressed)
