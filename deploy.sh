#!/bin/bash
echo "Starting deployment script"
pip install -r requirements.txt

echo "Starting the Flask application..."
python3 main.py