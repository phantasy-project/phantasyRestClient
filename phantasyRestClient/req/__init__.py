import requests
from phantasyRestClient.config import conf_dict
from phantasyRestClient.req.mp import MachinePortalResources

session = requests.Session()
session.verify = False
# mp resources
MachinePortalResources.SESSION = session
MachinePortalResources.URL = conf_dict['bind']
