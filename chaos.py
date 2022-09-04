import pyperclip



def pr(px, rem=24):
    output = px/rem
    pyperclip.copy(f"{output}rem")
    return output


def pp(px, px_width=1512):
    output = (pr(px)/pr(px_width)) * 100
    pyperclip.copy(f"{output}%")
    return output
