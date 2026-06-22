import numpy as np
from fractions import Fraction as fr
import sympy as sp

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

def vfr(x,y=1):
    f = lambda z:fr(z,y)
    return np.vectorize(f)(x)

icollatz_vec_lr = lambda x:np.array((vfr((x-1),3),vfr(2*x)),dtype=object)

def icollatz_vec_ord(x):
    result = np.zeros(np.size(x)*2,dtype=object)
    result[0::2]=vfr((x-1),3)
    result[1::2]=vfr(2*x)
    return result

def icollatz_set_level(x,l=1):
    r=np.array(x).copy()
    for n in range(l):
        r=icollatz_vec_ord(r)
    return r

def icollatz_tree(x,l=5,pr=True,sv=False,mode='w+',name=None):
    if sv:
        if name is None:
            name=input('Enter file name: ')
            if name =='':
                name='mycollatztree'
        myfile = open(f'{name}.txt',mode)

    xx=np.array(x).copy()
    sets=[xx]

    for n in range(l):
        xx=icollatz_vec_ord(xx)
        sets.append(xx)

    ncmax=0
    for n in xx:
        ncthis=len(str(n))
        if ncthis>ncmax:
            ncmax=ncthis
    
    nclinemax=(ncmax+2)*len(xx)

    for s in sets:
        strings=[]
        if is_iterable(s):
            for f in s:
                strings.append(str(f))
        else:
            strings.append(str(s))
        line=' | '.join(strings)
        print(line.center(nclinemax,' ')) if pr else _
        myfile.write(line.center(nclinemax,' ')+'\n') if sv else _

    if sv:
        myfile.close()

    return

def icollatz_lefts(x,l=5,pr=True,sv=False,mode='w+',name=None):
    if sv:
        if name is None:
            name=input('Enter file name: ')
            if name =='':
                name='mycollatzlefts'
        myfile = open(f'{name}.txt',mode)

    xx=np.array(x).copy()
    sets=[xx]

    for n in range(l):
        sets.append(icollatz_vec_lr(xx)[0])
        xx=icollatz_vec_ord(xx)

    ncmax=0
    for n in xx:
        ncthis=len(str(n))
        if ncthis>ncmax:
            ncmax=ncthis
    
    nclinemax=(ncmax+2)*len(xx)

    for s in sets:
        strings=[]
        if is_iterable(s):
            for f in s:
                strings.append(str(f))
        else:
            strings.append(str(s))
        line=' | '.join(strings)
        print(line.center(nclinemax,' ')) if pr else _
        myfile.write(line.center(nclinemax,' ')+'\n') if sv else _

    if sv:
        myfile.close()

    return

def icollatz_rights(x,l=5,pr=True,sv=False,mode='w+',name=None):
    if sv:
        if name is None:
            name=input('Enter file name: ')
            if name =='':
                name='mycollatzrights'
        myfile = open(f'{name}.txt',mode)

    xx=np.array(x).copy()
    sets=[xx]

    for n in range(l):
        sets.append(icollatz_vec_lr(xx)[1])
        xx=icollatz_vec_ord(xx)

    ncmax=0
    for n in xx:
        ncthis=len(str(n))
        if ncthis>ncmax:
            ncmax=ncthis
    
    nclinemax=(ncmax+2)*len(xx)

    for s in sets:
        strings=[]
        if is_iterable(s):
            for f in s:
                strings.append(str(f))
        else:
            strings.append(str(s))
        line=' | '.join(strings)
        print(line.center(nclinemax,' ')) if pr else _
        myfile.write(line.center(nclinemax,' ')+'\n') if sv else _

    if sv:
        myfile.close()

    return

def icollatz_show_all(x,l=5,pr=True,sv=False,name=None):
    if sv:
        if name is None:
            name=input('Enter file name: ')
            if name =='':
                name='mycollatzall'
    
    icollatz_tree(x,l,pr,sv,'w+',name)
    icollatz_lefts(x,l,pr,sv,'a',name)
    icollatz_rights(x,l,pr,sv,'a',name)

    print('Collatz!')

    return

def ixs_values_level(x,l=5,bitflip=False):
    xx = icollatz_set_level(x,l) if l>0 else x
    ixs = []
    vals=[]

    i=1
    for f in xx:
        if f.denominator==1 and f.numerator != 0 and f.numerator != 2**l:
            ixs.append(2**l-i) if not bitflip else ixs.append(i)
            vals.append(int(f.numerator))
        i+=1
    
    return ixs[::-1],vals[::-1]

def list_binary_ixs(x,l=5):
    r=[]
    for n in range(l+1):
        if n>=3:
            r.append((n,[f'{el:07b}' for el in ixs_values_level(x,n)[0]]))
    return r

#icollatz_show_all(1,11,True,True,'mycollatzall')