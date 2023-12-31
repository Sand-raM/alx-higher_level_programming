#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        r = fct(*args)
    except Exception as i:
        sys.stderr.write("Exception: {}\n".format(i))
        r = None

    return (r)
