#!/bin/bash

sudo systemctl daemon-reload
sudo systemctl start dash.service    # starts up the service
sudo systemctl status dash.service   # prints the status to the log