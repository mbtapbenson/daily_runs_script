import sys
import selenium

sys.path.append('/Users/pbenson/Documents/')
print(sys.path)

import ducktape
from ducktape import fmis_controller_class


if not sys.argv[1]:
    raise ValueError('Please provide a date string as argument')

date = sys.argv[1]

dlpath = '/home/rubix/Desktop/Project-Ducttape/data/contract_data/' + date + '/'

# Instantiate the controller object
controller = fmis_controller_class.FmisController(dlpath)
# These are assigned so they can be closed later. 
display, browser = controller.get_browser_elements()

# Queries
direct_query_list = ['PL_BUYER_BACKLOG', 'PL_CHNG_ORDER_INSERTS', 'PL_CONTRACTS_DAILY', 
                    'PL_OPEN_PO_SUMMARY', 'PL_PO_PARTICIPATION_DBE', 'PL_REQ_ACTIVITY', 'PL_REQUISITION_DATA',
                    'PL_REQUISITION_DATA_PT1', 'PL_VOUCHER_PYMTS_PT7', 'PL_WF_PO_APPR_FULL_STEPS_V2', 
                    'PL_WF_PO_APPR_HISTORY', 'PL_WO_DESCRIPTIONS', 'PL_CNT_ACTIVITY', 
                    'PL_PURCH_ORDER_DATA_PT5', 'PL_PURCH_ORDER_DATA_PT6', 'PL_PURCH_ORDER_DATA_PT7']

# Loops through all direct queries in the given list and runs a direct query for them.
controller.get_direct_queries(direct_query_list)

ducktape.chrome_close(display, browser)