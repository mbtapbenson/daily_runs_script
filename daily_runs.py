import sys
import selenium

sys.path.append('/Users/pbenson/Documents/')
sys.path.append('/home/rubix/Desktop/Project-Ducttape')
print(sys.path)

import ducktape
from ducktape import fmis_controller_class


# The query names aren't sufficient to run queries, as each query is downloaded to a different 
# directory. We need download paths too.

with open('/home/rubix/Desktop/Project-Ducttape/PeterBenson_Projects/daily_runs_script/pl_daily_runs_with_pahts.txt', 'r') as f:
    file_lines = f.readlines()
    # This is of the format 
    # Download path
    # Corresponding queries
    # Download path 2

# Instantiate the controller object
controller = fmis_controller_class.FmisController('/home/rubix/Desktop/Project-Ducttape')

# Loop through the download path list
if not sys.argv[1]:
    raise ValueError('Please provide a date string as argument')

date = sys.argv[1]

for line in file_lines:
    # If the line is a download path, switch to that download directory
    if line.startswith('/home'):
        controller.change_download_directory(line + date + '/')
    # Otherwise, run a query.
    else:
        controller.get_direct_query(line)

controller.logout()