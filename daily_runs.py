import sys
import selenium

sys.path.append('/Users/pbenson/Documents/')
sys.path.append('/home/rubix/Desktop/Project-Ducttape')
print(sys.path)

import ducktape
from ducktape import fmis_controller_class


# The query names aren't sufficient to run queries, as each query is downloaded to a different 
# directory. We need download paths too.
if not sys.argv[1]:
    raise ValueError('Please provide a path to the query file')

query_file = sys.argv[1]

with open(query_file, 'r') as f:
    file_lines = f.read().splitlines()
    # read().splitlines() gets rid of the newlines.
    
    # This is of the format 
    # Download path
    # Corresponding queries
    # Download path 2

# Instantiate the controller object
first_download = file_lines[0]

controller = fmis_controller_class.FmisController(first_download)

# Loop through the download path list
if not sys.argv[2]:
    raise ValueError('Please provide a date string as argument')

date = sys.argv[2]

### IMPORTANT:
# Daily runs doesn't actually run the first query it receives. It is unclear why this is.
# To rectify this issue, we run a dummy query here. In this case, it's the first two lines of the query file.
print("RUNNING DUMMY QUERY:")
controller.change_download_directory(first_download + date + '/')
controller.get_direct_query(file_lines[1])


for line in file_lines:
    print(line)
    # If the line is a download path, switch to that download directory
    if line.startswith('/home'):
        controller.change_download_directory(line + date + '/')
    
    # Otherwise, run a query.
    else:
        controller.get_direct_query(line)
        
controller.logout()
