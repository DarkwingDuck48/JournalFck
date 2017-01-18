#  coding: utf-8

import json


def AccountMapping(mapping, mString):
    line = mString
    if len(line) == 12:
        if line[0] == mapping["Source"]['account']:
            line[0] = mapping["Target"]['account']
        if (line[1] == mapping["Source"]['ICP'] or mapping["Source"]['ICP'] == "*") and mapping["Target"]["ICP"] != "*":
            line[1] = mapping["Target"]['ICP']
        if (line[2] == mapping["Source"]['MovProd'] or mapping["Source"]['MovProd'] == "*") and mapping["Target"]["MovProd"] != "*":
            line[2] = mapping["Target"]['MovProd']
        if (line[3] == mapping["Source"]['VarLob'] or mapping["Source"]['VarLob'] == "*") and mapping["Target"]["VarLob"] != "*":
            line[3] = mapping["Target"]['VarLob']
        if (line[4] == mapping["Source"]['MktOvr'] or mapping["Source"]['MktOvr'] == "*") and mapping["Target"]["MktOvr"] != "*":
            line[4] = mapping["Target"]['MktOvr']
        if (line[5] == mapping["Source"]['AuditDim'] or mapping["Source"]['AuditDim'] == "*") and mapping["Target"]["AuditDim"] != "*":
            line[5] = mapping["Target"]['AuditDim']
        if (line[6] == mapping["Source"]['RelPartDisc'] or mapping["Source"]['RelPartDisc'] == "*") and mapping["Target"]["RelPartDisc"] != "*":
            line[6] = mapping["Target"]['RelPartDisc']
        if (line[7] == mapping["Source"]['CostCenterDisc'] or mapping["Source"]['CostCenterDisc'] =="*") and mapping["Target"]["CostCenterDisc"] != "*":
            line[7] = mapping["Target"]['CostCenterDisc']
        if (line[8] == mapping["Source"]['CustomType'] or mapping["Source"]['CustomType'] == "*") and mapping["Target"]["CustomType"] != "*":
            line[8] = mapping["Target"]['CustomType']
    if len(line) == 13:
        if line[1] == mapping["Source"]['account']:
            line[1] = mapping["Target"]['account']
        if (line[2] == mapping["Source"]['ICP'] or mapping["Source"]['ICP'] == "*") and mapping["Target"]["ICP"] != "*":
            line[2] = mapping["Target"]['ICP']
        if (line[3] == mapping["Source"]['MovProd'] or mapping["Source"]['MovProd'] == "*") and mapping["Target"]["MovProd"] != "*":
            line[3] = mapping["Target"]['MovProd']
        if (line[4] == mapping["Source"]['VarLob'] or mapping["Source"]['VarLob'] == "*") and mapping["Target"]["VarLob"] != "*":
            line[4] = mapping["Target"]['VarLob']
        if (line[5] == mapping["Source"]['MktOvr'] or mapping["Source"]['MktOvr'] == "*") and mapping["Target"]["MktOvr"] != "*":
            line[5] = mapping["Target"]['MktOvr']
        if (line[6] == mapping["Source"]['AuditDim'] or mapping["Source"]['AuditDim'] == "*") and mapping["Target"]["AuditDim"] != "*":
            line[6] = mapping["Target"]['AuditDim']
        if (line[7] == mapping["Source"]['RelPartDisc'] or mapping["Source"]['RelPartDisc'] == "*") and mapping["Target"]["RelPartDisc"] != "*":
            line[7] = mapping["Target"]['RelPartDisc']
        if (line[8] == mapping["Source"]['CostCenterDisc'] or mapping["Source"]['CostCenterDisc'] == "*") and mapping["Target"]["CostCenterDisc"] != "*":
            line[8] = mapping["Target"]['CostCenterDisc']
        if (line[9] == mapping["Source"]['CustomType'] or mapping["Source"]['CustomType'] == "*") and mapping["Target"]["CustomType"] != "*":
            line[9] = mapping["Target"]['CustomType']
    return ";".join(line)

#Read mappings for accounts
with open("Mapping.json", "r", encoding="utf-8") as file:
    alldict = json.load(file)
    mappings = alldict["Mappings"]

convertedJournals = open("ConvJourn2016_NovDec.txt", 'w', encoding="utf-8")
log = open('logs.txt', 'w', encoding="utf-8")

with open("DAILYHFM_Journal.txt", "r") as journal:
    for line in journal:
        if line.isspace():
            convertedJournals.write(line)
        elif line.startswith("!"):
            convertedJournals.write(line)
            if line.startswith("!JOURNAL") or line.startswith("!Period"):
                log.write(line + '\n')
        else:
            if line.strip().split(";")[0].isdigit():
                for acc in mappings.keys():
                    if line.startswith(acc):
                        accountmap = mappings[acc]
                        mappedline = line.strip().split(";")
                        mstring = AccountMapping(accountmap, mappedline)+"\n"
                        line = mstring
                        log.write(mstring)
            elif not(line.strip().split(";")[0].isdigit()):
                for acc in mappings.keys():
                    mappedline = line.strip().split(";")
                    if mappedline[1] == acc:
                        accountmap = mappings[acc]
                        mstring = AccountMapping(accountmap, mappedline) + "\n"
                        line = mstring
                        log.write(mstring)
            convertedJournals.write(line)

convertedJournals.close()
log.close()

print("Done!")