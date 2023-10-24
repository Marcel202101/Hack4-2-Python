"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(result):
    resultado = {}
    result.pop("bar")
    for item in result.items():
        resultado[item[0].capitalize()] = ''.join(list(item[1].capitalize())).replace('k','')
    return resultado