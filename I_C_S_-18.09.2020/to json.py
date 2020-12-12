import json

from tovar import nounlist

with open("D:\Student\ICS_18.09.2020\I_C_S_-18.09.2020\tovar_json.json", 'w') as write_file:
    json.dump(nounlist, write_file)

from price import nounlist

with open("D:\Student\ICS_18.09.2020\I_C_S_-18.09.2020\price_json.json", 'w') as write_file:
    json.dump(nounlist, write_file)

