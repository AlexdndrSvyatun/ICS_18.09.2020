import json
from tovar import nounlist2
from price import nounlist1

def  convertToJSON():
 with open("D:\Student\ICS_18.09.2020\I_C_S_-18.09.2020\price_json.json", 'w') as write_file:
    json.dump(nounlist1, write_file)
def convertInJSON():
 with open("D:\Student\ICS_18.09.2020\I_C_S_-18.09.2020\ tovar_json.json", 'w') as write_file:
    json.dump(nounlist1, write_file)

