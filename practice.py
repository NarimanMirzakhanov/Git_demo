def reverse(st):
    new_ls = st.replace('   ', ' ').replace('  ', ' ').split(' ')
    ls_rev = []
    for i in new_ls:
        ls_rev.insert(0, i)
    new_st = ' '.join(ls_rev).strip()
    return new_st.strip()


print(reverse('Hello   World '), 'World Hello')
print(reverse('Hi   There. '), 'There. Hi')