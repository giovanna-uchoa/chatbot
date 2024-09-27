#/bin/bash
#!./.venv/python

# Exit immediately if a command exits with a non-zero status
set -e

# Define directories
DIR='.'

# Create and activate a Python virtual environment
echo "Setting up Python virtual environment..."
python3 -m venv "${DIR}/.venv"
source "${DIR}/.venv/bin/activate"

# Install Python dependencies
echo "Installing Python dependencies..."
python -m pip install -r "${DIR}/requirements.txt"

# Deactivate the Python virtual environment
deactivate

echo "Setup complete!"
