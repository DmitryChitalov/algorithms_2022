from memory_profiler import profile


@profile

def wrapper(input_number):
    def func(numb, reserved_number=''):
        if numb==0:
            return reserved_number
        else:
            digit = numb % 10
        return func(numb // 10,reserved_number + str(digit))
    
    return func(input_number)

number = 9876543345678908765434567898765432234567898765432234567898765498765433456789087654345678987654322345678987654322345678987654987654334567890876543456789876543223456789876543223456789876549876543345678908765434567898765432234567898765432234567898765498765433456789087654345678987654322345678987654322345678987654

print(f'Перевернутое число: {wrapper(number)}')


