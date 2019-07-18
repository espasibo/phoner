import regular, requester

def process(url):
    line = requester.getdom(url)
    return regular.parse(line)

