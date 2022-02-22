import sys
import selenium

sys.path.append('/Users/pbenson/Documents/')
sys.path.append('/home/rubix/Desktop/Project-Ducttape')
print(sys.path)

import ducktape
from ducktape import fmis_controller_class

with open('/home/rubix/Desktop/Project-Ducttape/PeterBenson_Projects/daily_runs_script/direct_query_names.txt', 'r') as f:
    direct_query_list = f.readlines()
    # This should be of the format 'Query name \t Download path'

# Instantiate the controller object
controller = fmis_controller_class.FmisController('/home/rubix/Desktop/Project-Ducttape')
# These are assigned so they can be closed later. 

# Queries
"""
direct_query_list = ['PL_BUYER_BACKLOG', 'PL_CHNG_ORDER_INSERTS', 'PL_CONTRACTS_DAILY', 
                    'PL_OPEN_PO_SUMMARY', 'PL_PO_PARTICIPATION_DBE', 'PL_REQ_ACTIVITY', 'PL_REQUISITION_DATA',
                    'PL_REQUISITION_DATA_PT1', 'PL_VOUCHER_PYMTS_PT7', 'PL_WF_PO_APPR_FULL_STEPS_V2', 
                    'PL_WF_PO_APPR_HISTORY', 'PL_WO_DESCRIPTIONS', 'PL_CNT_ACTIVITY', 
                    'PL_PURCH_ORDER_DATA_PT5', 'PL_PURCH_ORDER_DATA_PT6', 'PL_PURCH_ORDER_DATA_PT7']
"""

# Loops through all direct queries in the given list and runs a direct query for them.
controller.get_direct_queries(direct_query_list)

# Also need to get the download paths for each query.
# Loop through the query file (query, filename) and execute the query. 

controller.logout()