# This script is a reference for a live presenatation.
# It includes the the create_blob, create_tree and create_commit functionality.
# 
# Author: Tim Silhan

# git init -q ./bloated
# tree ./bloated/.git/
# rm -rf ./bloated

# mkdir -p basicrepo/.git/refs/heads
# mkdir -p basicrepo/.git/objects
# echo "ref: refs/heads/master" >> ./basicrepo/.git/HEAD

import os
import zlib
import time
from hashlib import sha1


# Create the blob object
blob_content = 'Hello World\n'
blob_header = f'blob {len(blob_content)}\x00'
blob_store = (blob_header + blob_content).encode('utf-8')

blob_digest = sha1(blob_store).hexdigest()
blob_compressed = zlib.compress(blob_store)

blob_dir = f'.git/objects/{blob_digest[:2]}/'
blob_file = blob_dir + blob_digest[2:]

os.makedirs(os.path.dirname(blob_dir))
with open(blob_file, 'wb') as blob:
    blob.write(blob_compressed)



# Create the tree object
tree_filename = 'hello.txt'
tree_content = b'100644 ' + tree_filename.encode('utf-8') + b'\x00' + bytes.fromhex(blob_digest)
tree_header = f'tree {len(tree_content)}\x00'
tree_store = tree_header.encode('utf-8') + tree_content

tree_digest = sha1(tree_store).hexdigest()
tree_compressed = zlib.compress(tree_store)

tree_dir = f'.git/objects/{tree_digest[:2]}/'
tree_file = tree_dir + tree_digest[2:]

os.makedirs(os.path.dirname(tree_dir))
with open(tree_file, 'wb') as tree:
    tree.write(tree_compressed)



# Create commit object
# Parent hash is not mandatory and is excluded here
author_name = 'John Doe'
author_email = 'jd@someplace.com'
seconds_since_epoch = int(time.time())
time_zone = '+0000'
commit_message = 'This is it! We made it!\n'

commit_content = f'tree {tree_digest}'
commit_content += f'\nauthor {author_name} <{author_email}> {seconds_since_epoch} {time_zone}'
commit_content += f'\ncommitter {author_name} <{author_email}> {seconds_since_epoch} {time_zone}'
commit_content += f'\n\n{commit_message}'

commit_header = f'commit {len(commit_content)}\x00'
commit_store = commit_header.encode('utf-8') + commit_content.encode('utf-8')

commit_digest = sha1(commit_store).hexdigest()
commit_compressed = zlib.compress(commit_store)

commit_dir = f'.git/objects/{commit_digest[:2]}/'
commit_file = commit_dir + commit_digest[2:]

os.makedirs(os.path.dirname(commit_dir))
with open(commit_file, 'wb') as commit:
    commit.write(commit_compressed)

# echo [sha1] > basicrepo/.git/refs/heads/custom-branch
# git branch
# git switch custom-branch