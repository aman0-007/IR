def lev(a,b):
    
    if(len(a)==0):
        return len(b)
    if(len(b)==0):
        return len(a)

    if(a[0] == b[0]):
        return lev(a[1:],b[1:])

    insertion = lev(a,b[1:])
    deletion = lev(a[1:],b)
    substitution = lev(a[1:],b[1:])

    return 1 + min(insertion, deletion, substitution)


print(lev("kiasdfaaatten", "sittiasfasdfg"))
    
