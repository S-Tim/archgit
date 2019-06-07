#!/usr/bin/env python3

# This script is a reference for a live presenatation.
# It includes the the create_blob, create_tree and create_commit functionality.
# 
# Author: Tim Silhan

import os
import sys
import zlib
import time
from hashlib import sha1

# Create the blob object
print("Blob")
print("-----------------------")

blob_content = 'Hello World\n'
print('Input: ', blob_content)

blob_header = f'blob {len(blob_content)}\u0000'
print('Header:', blob_header)

blob_store = blob_header + blob_content
print('Store:', blob_store)

blob_digest = sha1(blob_store.encode('utf-8')).hexdigest()
print('Digest:', blob_digest)
blob_dir = blob_digest[:2]
print('Dir:', blob_dir)
blob_file = blob_digest[2:]
print('File:', blob_file)

blob_compressed = zlib.compress(blob_store.encode('utf-8'))
print('\nCompressed:', blob_compressed)

os.makedirs(os.path.dirname(f'.git/objects/{blob_dir}/'))
with open(f'.git/objects/{blob_dir}/{blob_file}', 'wb') as blob:
    blob.write(blob_compressed)


# Create the tree object
print("Tree")
print("-----------------------")
tree_filename = "hello.txt"

print('Ref Hash: ', blob_digest)

tree_content = b"100644 " + tree_filename.encode('utf-8') + b"\x00" + bytes.fromhex(blob_digest)
# Create a directory with a tree object
# content = b"40000 " + filename.encode('utf-8') + b"\x00" + bytes.fromhex(ref_hash)

tree_header = f'tree {len(tree_content)}\u0000'
print('Header:', tree_header)

tree_store = tree_header.encode('utf-8') + tree_content
print('Store:', tree_store)

tree_digest = sha1(tree_store).hexdigest()
print('Digest:', tree_digest)
tree_dir = tree_digest[:2]
print('Dir:', tree_dir)
tree_file = tree_digest[2:]
print('File:', tree_file)

tree_compressed = zlib.compress(tree_store)
print('Compressed:', tree_compressed)

os.makedirs(os.path.dirname(f'.git/objects/{tree_dir}/'))
with open(f'.git/objects/{tree_dir}/{tree_file}', 'wb') as tree:
    tree.write(tree_compressed)


# Create commit object
print("Commit")
print("-----------------------")

print('Tree Hash: ', tree_digest)

parent_hash = ''
if parent_hash:
    print('Parent Hash: ', parent_hash)

author_name = 'John Doe'
author_email = 'jd@someplace.com'
seconds_since_epoch = int(time.time())
time_zone = '+0000'
commit_message = 'This is it! We made it!\n'

commit_content = ''
if parent_hash:
    commit_content += f'\nparent {parent_hash}'
commit_content += f'\nauthor {author_name} <{author_email}> {seconds_since_epoch} {time_zone}'
commit_content += f'\ncommitter {author_name} <{author_email}> {seconds_since_epoch} {time_zone}'
commit_content += f'\n\n{commit_message}'
commit_content = f'tree {tree_digest}' + commit_content
print('Content:\n', commit_content)

commit_header = f'commit {len(commit_content)}\u0000'
print('Header:', commit_header)

commit_store = commit_header.encode('utf-8') + commit_content.encode('utf-8')
print('Store:', commit_store)

commit_digest = sha1(commit_store).hexdigest()
print('Digest:', commit_digest)
commit_dir = commit_digest[:2]
print('Dir:', commit_dir)
commit_file = commit_digest[2:]
print('File:', commit_file)

commit_compressed = zlib.compress(commit_store)
print('Compressed:', commit_compressed)

os.makedirs(os.path.dirname(f'.git/objects/{commit_dir}/'))
with open(f'.git/objects/{commit_dir}/{commit_file}', 'wb') as commit:
    commit.write(commit_compressed)
