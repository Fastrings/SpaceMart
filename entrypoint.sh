#!/bin/bash

# Wait for the database container to start
while !</dev/tcp/db/5432; do sleep 1; done;

# Connect to the database container
echo "Connecting to the database container..."
python initialize-db.py