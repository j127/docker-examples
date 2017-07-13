# Notes About Mariadb

See [this post](https://mariadb.com/kb/en/mariadb/installing-and-using-mariadb-via-docker/).

This command will create a container

    $ docker container run --name mariadbtest -e MYSQL_ROOT_PASSWORD=mypass -d mariadb

This command will stop it:

    $ docker container stop mariadbtest

If you don't remove the container, but just stop it, the data will still be there when it's restarted like this:

    $ docker container start mariadbtest

