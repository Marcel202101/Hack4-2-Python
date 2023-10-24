"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""


def fn_hack_7(result):
    band =True
    solution = []
    cont = 1
    if(len(result)>0 and result.count(0)<=0):
        for i in result:
            if(band):
                solution.append(str(cont))
            else:
                solution.append(cont)
            cont+=1
            band = not band
    else:
        solution.append(0)
    return solution

print(fn_hack_7([0]))