arab = (1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000)
roman = ('I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M')

def toRoman(number):
    if not isinstance(number, int):
        raise ValueError("It is impossible to imagine not integer value in Roman")

    if number <= 0:
        raise ValueError("It is impossible to imagine a negative or zero in Roman")

    ret = ''
    i = len(arab) - 1
    while number > 0:
        if number >= arab[i]:       
            ret = ret + roman[i]
            number = number - arab[i]
        else:       
            i = i - 1    
    return ret


def toArab(str):
    if len(str) == 0:
        raise ValueError("Roman number zero length")
    str = str.upper()
    
    str_copy = str[:]
    for r_symb in roman:
        str_copy = str_copy.replace(r_symb,'')
    
    if len(str_copy) > 0:
        raise ValueError("Unknown Roman number")

    ret = 0
    i = len(arab) - 1
    pos = 0
    while i >= 0 and pos < len(str):    
        if str[pos:pos+len(roman[i])] == roman[i]:
            ret = ret + arab[i]
            pos = pos + len(roman[i])
        else:
            i = i - 1
    return ret
