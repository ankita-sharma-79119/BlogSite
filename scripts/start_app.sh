#!/bin/bash

sudo systemctl daemon-reload
sudo systemctl start app.service    # starts up the service
sudo systemctl status app.service   # prints the status to the log