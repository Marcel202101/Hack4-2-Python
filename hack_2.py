"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(result):
    abc = 'aeiou'
    result = ''.join(([x for x in result if x not in abc]))
    return result