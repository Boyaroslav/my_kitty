from random import choice

def answer(msg):
    ors = ["or", "или"]
    msg = msg.rstrip("?")
    msg = msg.split()
    #  text separated by ors
    variants = []
    buf = []
    isd = 0
    for i in msg:
        if i in ors:
            isd = 1
    if isd:

        for i in msg:
            if i not in ors:
                buf.append(i)
            else:
                variants.append(' '.join(buf))
                buf.clear()
        if buf:
            variants.append(' '.join(buf))
        print(variants)

        return choice(variants)

