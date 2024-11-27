#!/bin/bash

# File paths and settings
input_file="input.csv"
output_file="shuffled_output.csv"
BANDWIDTH_LIMIT="200k"
USER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"

# Check if input CSV exists
[[ ! -f "$input_file" ]] && { echo "Input CSV file not found!"; exit 1; }

# Step 1: Create unique directories from column B
awk -F, '{print $2}' "$input_file" | sort -u | xargs -I {} mkdir -p "{}"

# Step 2: Randomize the rows of the CSV and save to a new file
shuf "$input_file" > "$output_file"
echo "CSV randomized and saved as $output_file"
