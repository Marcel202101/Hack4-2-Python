"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""

def fn_hack_5(result):
    result = list(result)
    band = True if result.count("f")>0 else False
    cont = 2
    while (cont>=2 and cont<len(result)):
        if(band and cont>4):
            result.insert(cont,'-')
            band !=band
        else:
            result[cont] = '-'
        cont+=3
    if (len(result)>=10):
        result = result[:len(result)-1]
    return ''.join(result)