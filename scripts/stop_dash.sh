#!/bin/bash

SERVICE_FILE=/etc/systemd/system/dash.service
if test -f "$SERVICE_FILE"; then
    sudo systemctl stop dash.service   # shutdown the service
    sudo rm "$SERVICE_FILE"
fi