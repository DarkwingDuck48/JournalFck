#  coding: utf-8

import json
import time

def AccountMapping(mapping, mString):
    """

    :param mapping: take mapping dict from Mapping.json
    :param mString: String from file with mapped accounts
    :return: mapped string
    """
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
        if (line[7] == mapping["Source"]['CostCenterDisc'] or mapping["Source"]['CostCenterDisc'] == "*") and mapping["Target"]["CostCenterDisc"] != "*":
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
starttime = time.time()
#Read mappings for accounts
with open("Mapping.json", "r", encoding="utf-8") as file:
    alldict = json.load(file)
    mappings = alldict["Mappings"]

# Create target file and log file
convertedJournals = open("ConvJournals2016_ACT.txt", 'w', encoding="utf-8")
log = open('logs.txt', 'w', encoding="utf-8")

# Open file
with open("DAILYHFM_Journal_2016_Act.txt", "r") as journal:
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
                # Axe
                # Do rename for renamed elements
                if line.strip().split(";")[7] == "CC03":
                    mappedline = line.strip().split(";")
                    mappedline.remove("CC03")
                    mappedline.insert(7, "CC31")
                    line = ";".join(mappedline)+"\n"
                    log.write(line)
                if line.strip().split(";")[7] == "CC05":
                    mappedline = line.strip().split(";")
                    mappedline.remove("CC05")
                    mappedline.insert(7, "CC51")
                    line = ";".join(mappedline)+"\n"
                    log.write(line)
                # End Axe
            elif not(line.strip().split(";")[0].isdigit()):
                for acc in mappings.keys():
                    mappedline = line.strip().split(";")
                    if mappedline[1] == acc:
                        accountmap = mappings[acc]
                        mstring = AccountMapping(accountmap, mappedline) + "\n"
                        line = mstring
                        log.write(mstring)
                # Axe
                # Do rename for renamed elements
                if line.strip().split(";")[8] == "CC03":
                    mappedline = line.strip().split(";")
                    mappedline.remove("CC03")
                    mappedline.insert(8, "CC31")
                    line = ";".join(mappedline)+"\n"
                    log.write(line)
                if line.strip().split(";")[8] == "CC05":
                    mappedline = line.strip().split(";")
                    mappedline.remove("CC05")
                    mappedline.insert(8, "CC51")
                    line = ";".join(mappedline)+"\n"
                    log.write(line)
                # End Axe
            convertedJournals.write(line)

convertedJournals.close()
log.close()

print("Done! Time is - {:.3f}".format(time.time() - starttime))
