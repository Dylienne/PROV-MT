#written by Dylienne Every 2127946
#Department of Computer Sciences VU AMSTERDAM
#Master Thesis

import json
import ijson
import pandas as pd
import numpy as np
import prov

#definition of contents
document = pd.read_json('Data/JSON/GOOGLPROV.json')
# print(document)
Bundles = document["bundle"]
provenance = Bundles["result:provenance"]
elementoverview = list(provenance)

#pandas dataframe
df = pd.DataFrame(provenance)
print(df.count())

#timestamp extraction
#
# #overview per node
# ajson = pd.DataFrame(provenance['wasStartedBy'])
#
#
#
#
# def time_info(provenance):
#     timestampcollection = provenance["wasStartedBy", "wasGeneratedBy", "used", "wasInvalidatedBy"]
#     df = pd.DataFrame(timestampcollection)
#


