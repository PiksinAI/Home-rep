print('Задача 6. Маятник ')


def fading(ampl):
    ampl = ampl * 0.916
    return ampl


entire_ampl = float(input('Введите начальную амплитуду маятника: '))
stop_ampl = float(input('Введите амплитуду остановки: '))
count = 0
while entire_ampl > stop_ampl:
    entire_ampl = fading(entire_ampl)
    count += 1
print('Маятник качнется раз:', count)