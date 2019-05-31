# Archgit - How to create a commit from scratch

If you are interested in Git on a bytelevel and always wanted to create a commit without using git commands but instead using Python this is the right place for you!

## Scripts
The scripts directory contains all the scripts that you need to create a commit from scratch. Feel free to play around with the code and extend or improve them as you like. The scripts do not offer a lot of configuration in order to keep them simple.

## Archgit
The archgit directory contains a Jupyter notebook with which you can interactively learn how to create a commit from scratch. It provides the theory to understand the scripts and guides you through all the steps to create your own git repository and commits without using git commands.

To start the notebook you can either use the provided Dockerfile to build and run an image containing the notebook (Docker is required) or you can start your own Jupyter server if you have Jupyter installed locally.

### Docker
1. Build the image by running `docker build -t archgit .` from the root directory of this repo
2. Start an instance of the image with `docker run -p 8888:8888 archgit`
3. Open the notebook with the link that is shown in your terminal (e.g.
http://127.0.0.1:8888/?token=783bb9c1ddee9b6d402ce5b87495b35cedd36ffb20131ea9)

### Jupyter
1. Start the server by running `jupyter notebook` from the *archgit* directory in this repo
2. The notebook should open in your browser automatically