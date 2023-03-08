# Systemd files readme

This directory contains an example systemd unit file, and configuration environment file.

## prom433.service
This is the systemd unit file for managing the prom433 service. It may need to be modified for your environment.  See comments in the file.  It assumes that you have created a "prom433" user and group.  You can create these with the following commands if they do not exist on your system (e.g. if installed manually).

```
groupadd -r prom433
useradd -r -g prom433 -s /sbin/nologin -c "prom433 user" prom433
```

## prom433.example
This is an example of a configuration file you can use as a basis for `/etc/sysconfig/prom433` to control the options passed to the prom433 binary.
This file is only required if you don't want to use the defaults specified in the above systemd unit file. You must remove the `.example` suffix when placing it in the `/etc/sysconfig` directory.