#!/bin/bash

PYTHON_FILE="main.py"  
LOG_FILE="script_log_$(date +%Y%m%d_%H%M%S).log"
LOG_DIR="~/log"
PYTHON_EXEC="python3"  

# Check if Python file exists
if [ ! -f "~/.kaggle/kaggle.json" ]; then
    echo "Error: kaggle API key not found"
    exit 1
fi

# Log start time
echo "=== Script Execution Started: $(date) ===" >> "$LOG_FILE"

# Run Python script and append output to log file
echo "Running $PYTHON_FILE..." | tee -a "$LOG_FILE"
source etl-venv/bin/activate
$PYTHON_EXEC "$PYTHON_FILE" >> "$LOG_FILE" 2>&1

# Check if Python script executed successfully
if [ $? -eq 0 ]; then
    echo "Script executed successfully" | tee -a "$LOG_FILE"
else
    echo "Error: Script failed with exit code $?" | tee -a "$LOG_FILE"
fi

# Log end time
echo "=== Script Execution Ended: $(date) ===" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"