#!/bin/bash
echo "Starting deployment script"
pip install -r requirements.txt && python -m spacy download en_core_web_sm