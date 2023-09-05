import random
kust = int(input("введите количество кустов: "))
berryes = list(random.randint(15, 20) for i in range(kust))
result = []
i = 0
sum = 0
while (i < kust):
    if (i == kust - 1):
        sum = berryes[i] + berryes[i - 1] + berryes[0]
    else:
        sum = berryes[i] + berryes[i - 1] + berryes[i + 1]
        result.append(sum)
        result.sort()
    i += 1
print(f'Количество ягод за один проход {result[-1]}')
    
    
