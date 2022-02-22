#!/bin/bash

TEST_DIR="test"

python3 daily_runs.py TEST_DIR

echo "Ran daily_runs.py, dumped output to download_path/$TEST_DIR."
echo "Cleaing up..."

# Filter pl_daily_runs_with_paths to only the download paths
# Append the test directory to the end of them
DOWNLOAD_PATHS= grep "/home" pl_daily_runs_with_paths.txt | sed "s/$/$TESTDIR\//g"

# Run rm -r on all of them
# Iterate over 
echo "$DOWNLOAD_PATHS" | while IFS= read -r line ; do rm -r $line; done
# https://unix.stackexchange.com/questions/275794/iterating-over-multiple-line-string-stored-in-variable