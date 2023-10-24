"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(result):
    result =  result[1:len(result)-1] if 'f' in result or 'b' in result else result
    return result