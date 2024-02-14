#!/bin/bash
echo "Installing Python dependencies from requirements.txt..."
pip install -r requirements.txt

echo "Downloading the spaCy language model..."
python -m spacy download en_core_web_sm