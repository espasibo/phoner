import re
pattern = u"(>| | \\r\\n|\\n)(\+7|7|8)?([ -\(]{1,2})?([0-9]{3})?([ -\)]{1,2})?([0-9]{3})([- ])?([0-9]{2})([- ])?([0-9]{2})(<| |\\r\\n|\\n)";

def parse(string):
    prog = re.compile(pattern)
    result = []
    for i in prog.finditer(string):
        phone = "8"
        if (i.group(4)):
            phone += i.group(4)
        else:
            phone += "495"
        phone = phone + i.group(6) + i.group(8) + i.group(10)
        if phone not in result:
            result.append(phone)
    return result
