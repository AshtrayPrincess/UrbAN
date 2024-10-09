# Словари и множества

dct = {'sasha': 2001, 'anton': 1987, 'denis': 2005}
print(dct)
dct['oleg'] = 2000
print(dct['sasha'])
print(dct['oleg'])

dct.update({'fenya': 1987,
        'grisha': 1977})
del dct['sasha'] # del используется для удаления элементов
b = dct.pop('denis')  #метод "pop" используется при том случае, когда нужно извлечь значение или ключ как в данном случае
print(dct)
print(b)

####

st = {1,2,3,4,5,4,3,2,1, "str"}
st.add(6)
st.add("trs")
st.remove(1) #discard и remove используется для удаления элементов во множестве, различие в том что если использовать discard то программа не выдаст ошибку при ненаходе элемента, в отличии от remove
st.discard("str")
print(st)