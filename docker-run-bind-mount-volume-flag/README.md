This example will allow the host and container to share directories (change `username` to your username).

    $ docker run -v /home/username/newfolder123:/newfolder123 -it debian bash

* If the directories don't exist, they will be created.
* Changes to the container's files **DO** remain on the host after the container is shut down, but they are owned by `root`.
* Changes to files on the host **DO** show up on the container right away.
* If I edit the files on the host with Vim and save with `:w!`, the owner changes from `root` to my host's user.
* If I edit the files on the container again, the files still belong to the host's user and don't switch back to `root`.
