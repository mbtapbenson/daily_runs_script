#!/bin/bash

TEST_DIR="test"

python3 daily_runs.py /home/rubix/Desktop/Project-Ducttape/PeterBenson_Projects/daily_runs_script/pl_daily_runs_with_paths.txt  test

echo "Ran daily_runs.py, dumped output to download_path/test."
echo "Cleaing up..."

# Filter pl_daily_runs_with_paths to only the download paths
# Append the test directory to the end of them
# Remove the contents of these folders
grep "/home" pl_daily_runs_with_paths.txt | sed "s/$/test\//g" | xargs rm -r

echo "Done!"
