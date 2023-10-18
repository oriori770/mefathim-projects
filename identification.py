def id_chek(id_number):
    if len(id_number) != 9 or not id_number.isdigit():
        id_number = input('please enter 9 numbers ')
    the_sum_of_all_numbers = 0
    for i in range(len(id_number)):
        temp = int(id_number[i]) * (i % 2 + 1)
        the_sum_of_all_numbers += temp // 10 + temp % 10
    return the_sum_of_all_numbers % 10 == 0
idn = input('please enter id: ')
# idn = '318633534'
print(id_chek(idn))

