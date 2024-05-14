def test_varParams(*numbers, **namedParams):
    print("------ Позиционные параметры")
    print(numbers)
    print("------ Именованные параметры")
    for key, value in namedParams.items():
        print(f"{key}: {value}")

def my_factorial(n):
    if n == 1:
        return 1
    else:
        return n * my_factorial(n-1)

print("------ Функция с произвольным количеством параметров")
test_varParams(1,2,3,4,5, Dog="Рекс", Cat="Мурка", Cow="Бурёнка")
print("------ Мой Факториал")
for i in range(1,5):
    print(f"{i}! = {my_factorial(i)}")