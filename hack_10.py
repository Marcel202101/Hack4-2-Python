"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(result):
    solution = []
    band = True
    for i in range(0,len(result)*2,2):
        if(band):
            solution.append({str(i+1):str(i+2)})
        else:
            solution.append({str(i+1),str(i+2)})
        band = not band
    return solution