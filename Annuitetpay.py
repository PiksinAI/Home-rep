print('Задача 9. Аннуитетный платёж')


def credit_pay(sum_mon, years_meta, percent_meta):
    p = percent_meta / 100
    k = (p * (p + 1) ** years_meta) / (((p + 1) ** years_meta) - 1)
    a = k * sum_mon
    return a


def credit(s, years_start, years_fin, percent_cred):
    i = 1
    for year in range(years_start, years_fin, -1):
        print('\nПериод: ', i, '\n')
        i += 1
        print('Остаток долга на начало периода', s)
        perc_paid = s * (percent_cred / 100)
        print('Выплачено процентов:', perc_paid)
        cred_body = credit_pay(s, year, percent_cred) - perc_paid
        print('Выплачено тела кредита:', cred_body)
        s -= cred_body
    print('\nОстаток долга', round(s, 5))
    return s


sum_of_credit = float(input('Введите сумму кредита: '))
years = int(input('На сколько лет выдан кредит: '))
percent = float(input('На сколько процентов годовых? '))
sum_of_credit = credit(sum_of_credit, years, years - 3, percent)

print('=' * 40)
years_two = int(input('\nНа сколько лет продлеваем кредит: '))
new_percent = float(input('Увеличение ставки до: '))
i = 1
new_years = years_two + years - 3

credit(sum_of_credit, new_years, 0, new_percent)