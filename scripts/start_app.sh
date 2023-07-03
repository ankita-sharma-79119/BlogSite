#!/bin/bash

sudo systemctl daemon-reload
sudo systemctl start gunicorn.service    # starts up the service
sudo systemctl status gunicorn.service   # prints the status to the log