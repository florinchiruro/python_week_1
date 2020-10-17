
email = input('Introduceti adresa de e-mail \n \n')

flag_arond = False
index_arond = 0
flag_dot = False
index_dot = 0


for i in email:
    if i == '@' and email.count('@') == 1:
        flag_arond = True
        index_arond = email.index('@')
    elif i == '.' and email.count('.') == 1:
        flag_dot = True
        index_dot = email.index('.')

if flag_arond and flag_dot and index_arond < index_dot and email[index_dot+1:].isalpha():
    print('Email Valid')
else:
    print('Email Invalid')
