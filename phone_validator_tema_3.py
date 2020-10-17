def eroare():
    print('Telefonul nu este valid')


str_phone = '07'

phone = input('Introduceti un nr. de telefon: \n\n')

try:
    type(phone) == int
except ValueError:
    eroare()

phone = str(phone)

if len(phone) == 10 and phone[0] == str_phone[0] and phone[1] == str_phone[1]:
    print('Numarul Dvs de telefon este: ' + phone)
else:
    eroare()
