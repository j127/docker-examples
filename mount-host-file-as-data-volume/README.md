From [here](https://docs.docker.com/engine/tutorials/dockervolumes/#mount-a-host-file-as-a-data-volume):

    $ docker run --rm -it -v ~/.bash_history:/root/.bash_history ubuntu /bin/bash

It will copy your host's `.bash_history` to the container. When the container exits, the commands that were typed in the container's `bash` will be in the host's `~/.bash_history` file. (It waits to update the host's history file, because of the way bash history updates from memory.)

![Container active](./docker-v-0.png)

![Container destroyed](./docker-v-1.png)

You can also do this to save bash history from containers:

    $ docker container run -e HIST_FILE=/root/.bash_history \
        -v=$HOME/.bash_history:/root/.bash_history \
        -it ubuntu /bin/bash

and/or put something like this in your `aliases` file:

    alias dockbash='docker container run -e HIST_FILE=/root/.bash_history \
        -v=$HOME/.bash_history:/root/.bash_history'
