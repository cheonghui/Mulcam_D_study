## BOJ_Python 배우기3

21. BOJ_2935


`소음`

```python
num1 = int(input())
operator = input()
num2 = int(input())

if operator == '*':
    print(num1 * num2)
else:
    print(num1 + num2)
```



21. BOJ_9498


`시험 성적`

```python
score = int(input())

result = 0
if score >= 90 and score <= 100:
    result = 'A'
elif score >= 80 and score <= 89:
    result = 'B'   
elif score >= 70 and score <= 79:
    result = 'C'
elif score >= 60 and score <= 69:
    result = 'D'
else:
    result = 'F'

print(result)
```



23. BOJ_10817

`세 수 ` ❕❕

```python
a, b, c = map(int, input().split())
if a > b:
    if b > c:
        print(b)
    else:
        if a > c:
            print(c)
        else:
            print(a)
else: #b > a
    if a > c:
        print(a)
    else:# a가 최소값
        if b > c:
            print(c)
        else:
            print(b)
```



24. BOJ_11653

`소인수분해` ❕❕

```python
n = int(input())
m = 2
while n != 1:	# n이 1이 아니라면 반복한다. 
    if n % m == 0:	# 소수(제일 작은 2부터 시작)로 나눠 주고 나머지가 0이라면 해당 소수를 출력한다
        print(m)	
		n = n // m	# 몫(정수형)을 n에 할당해준다
    else:
        m += 1	# 나머지가 0이 아니라면 m에 1을 더해주고 다시 while문을 돌게된다 (반복문이 충족될 때 까지)
```



25. BOJ_1789

`수들의 합`

```python
s = int(input())

ilst = []
isum = 0
for i in range(1, s+1): # for문을 돌려가며 i의 값을 살핀다
    isum += i	
    if isum > s: # i와 isum의 합이 s를 넘지 않는다는 조건으로
        break
    else:
        ilst.append(i)	#i의 값들을 리스트에 추가
        
print(max(ilst))	#max()를 이용하여 리스트 안에 있는 i의 최대값을 구한다
```



26. BOJ_2753

`윤년`

```python
leap_year = int(input())

if (leap_year % 4 == 0) & (leap_year % 100 != 0) | (leap_year % 400 == 0):
    # 윤년 조건 - 4의 배수이면서 100의 배수이거나 400의 배수인 조건
    print(1)
    # 조건에 충족하면 1을 출력 
else:
    print(0)
    # 충족하지 않으면 0을 출력
```



27. BOJ_10039

`평균 점수`

```python
total = 0

for i in range(5):
    scores = int(input())
    if scores < 40:
        scores = 40 
    total += scores
print(total // 5)
```



28. BOJ_1934

`최소공배수` 😭

```python
def gcd(a, b): #최대공약수 구하기
    if (b == 0):
        return a
    return gcd(b, a % b)

def lcm(a, b): #최소공배수 구하기
    return a * b // gcd(a, b)

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    print(lcm(a, b))
    
```



29. BOJ_2480

`주사위 세개`

```python
a, b, c = map(int, input().split())
if a == b == c:
    print(10000 + a * 1000)
elif a == b:
    print(1000 + a * 100)
elif b == c:
    print(1000 + b * 100)
elif a == c:
    print(1000 + a * 100)
else:
    print(max(a, b, c) * 100)
```



30. BOJ_4101

`크냐?`

```python
while True:
    num1, num2 = map(int,input().split())
    if num1 == 0 & num2 ==0:
        break
    if num1 > num2:
        print('Yes')
    else:
        print('No')
```

