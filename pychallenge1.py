strs = 'abcdefghijklmnopqrstuvwxyz'

def shift_text(shift):
    inp = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    data = []
    for i in inp:
        if i.strip() and i in strs:
            data.append(strs[(strs.index(i) + shift) % 26])    
        else:
            data.append(i)
    output = ''.join(data)
    return output

print shift_text(3)
