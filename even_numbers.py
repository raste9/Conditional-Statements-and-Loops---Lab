# numbers = int(input())
#
# for i in range(numbers):
#     numbers = int(input())
#     if not numbers % 2 == 0:
#         print(f'{numbers} number is odd')
#         break
# else:
#     print(f'All numbers are even.')

number = int(input())

for _ in range(number):
    current_number = int(input())

    if current_number % 2 != 0:
        print(f'{current_number} is odd!')
        break
else:
    print(f'All numbers are even.')
