This was an experiment to try to run the container as a user with the same id as in the host OS, but there were permission errors

    $ docker run --rm --name nginx-html --user `id -u` -p 8888:80 -v `pwd`/src:/usr/share/nginx/html nginx:alpine

Result:

    $ docker run --rm --name nginx-html --user `id -u` -p 8888:80 -v `pwd`/src:/usr/share/nginx/html nginx:alpine
    2017/07/07 18:36:32 [warn] 1#1: the "user" directive makes sense only if the master process runs with super-user privileges, ignored in /etc/nginx/nginx.conf:2
    nginx: [warn] the "user" directive makes sense only if the master process runs with super-user privileges, ignored in /etc/nginx/nginx.conf:2
    2017/07/07 18:36:32 [emerg] 1#1: mkdir() "/var/cache/nginx/client_temp" failed (13: Permission denied)
    nginx: [emerg] mkdir() "/var/cache/nginx/client_temp" failed (13: Permission denied)
