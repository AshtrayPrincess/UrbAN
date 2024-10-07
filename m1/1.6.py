# Словари и множества

dct = {'sasha': 2001, 'anton': 1987, 'denis': 2005}
print(dct)
dct['oleg'] = 2000
print(dct['sasha'])
print(dct['oleg'])

dct.update({'fenya': 1987,
        'grisha': 1977})
del dct['sasha']
print(dct)

####

st = {1,2,3,4,5,4,3,2,1, "str"}
st.add(6)
st.remove(1)
print(st)