#!/bin/bash

SERVICE_FILE=/etc/systemd/system/gunicorn.service
if test -f "$SERVICE_FILE"; then
    sudo systemctl stop gunicorn.service   # shutdown the service
    sudo rm "$SERVICE_FILE"
fi
rm -r /home/ec2-user/app