"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(result):
    band =True
    solution = []
    cont = 1
    if(len(result)>0):
        for i in result:
            if(band):
                solution.append(str(cont))
            else:
                solution.append("-")
            cont+=1
            band = not band
    else:
        solution.append(str(0))
    return solution