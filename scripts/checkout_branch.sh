# Create a new branch that reference the given commit
# Let HEAD point to this new branch
# The working tree is not constructed by just pointing HEAD to a new branch
# git reset --hard HEAD can be used to build the working tree
#
# Author: Tim Silhan

echo $1 > .git/refs/heads/custom-branch
echo ref: refs/heads/custom-branch > .git/HEAD

# To build the working tree
# git reset --hard HEAD
