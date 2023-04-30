nums = []
i = 0
while i < 5:
    num = int(input("Enter a number: "))
    nums.append(num)
    i += 1

mayor = max(nums)
menor = min(nums)
x10 = 0
for num in nums:
    if num % 10 == 0:
        x10 += 1

print("\nR E S U L T A D O S")
print("=======================")
print(f"El mayor valor es..................: {mayor}")
print(f"El menor valor es..................: {menor}")
print(f"Cantidad de num. multiplos de 10...: {x10}")