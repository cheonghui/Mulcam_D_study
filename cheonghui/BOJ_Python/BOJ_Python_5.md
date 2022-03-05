## BOJ_Python 배우기5

41. BOJ_5086

`배수와 약수`

```python
while True:
    a, b = map(int, input().split())
    if (a, b) == (0, 0):    # a와 b가 0이라면 멈춘다.
        break				
    if b % a == 0:
        print('factor')     
    elif a % b == 0:
        print('multiple')
        
    else:
        print('neither')

```



42. BOJ_5717

`상근이의 친구들`

```python
while True:
    m, f = map(int,input().split())
    if (m,f) != (0, 0):
        print(m + f)
    else:
        break
  
# 반복하는 동안 m과 f가 0이 아니라면 상근이의 친구 수를 출력
# 0이라면 반복을 멈춘다.
```



43. BOJ_9610

`사분면` ❕

```python
n = int(input())

axis = 0    
q1 = 0      
q2 = 0      
q3 = 0      
q4 = 0      

for i in range(n):
    x, y = map(int, input().split())
    
    if x == 0 or y == 0: 	# x or y 값이 0이면 축에 해당
        axis += 1
    elif x > 0 and y > 0:	# 둘 다 양수일 때 Q1에 해당
        q1 += 1
    elif x < 0 and y > 0:	# X의 값이 음수라면 Q2에 해당
        q2 += 1
    elif x < 0 and y < 0:	# 둘 다 음수라면 Q3에 해당
        q3 += 1
    else:					# y의 값이 음수라면 Q4에 해당
        q4 += 1

# f-string 이용하여 값 출력
print(f'Q1: {q1}')
print(f'Q2: {q2}')
print(f'Q3: {q3}')
print(f'Q4: {q4}')
print(f'AXIS: {axis}')

```



44. BOJ_8958

`OX퀴즈` ❕ 

```python
t = int(input())

for _ in range(t):		# 2중 for문 - 1.t 만큼 ox를 돌면서 2.ox의 값을 반복하며 조건문 수행
    ox = list(input())

    total = 0
    s = 1
    for i in ox:
        if i == 'O':     # 값이 0이라면
            total += s   # 점수에 s를 더해주고
            s += 1       # s는 1씩 증가
        else:            # 값이 x가 되면 s를 1로 초기화
            s = 1
    print(total)

```



45. BOJ_9506

`약수들의 합`  ❕ 

```python
while True:
    n = int(input())
    if n == -1:
        break

    lst = []
    for i in range(1, n+1):
        if n % i == 0:      # n이 i로 나누어 떨어지면
            lst.append(i)   # 리스트에 추가

    if sum(lst[:-1]) == n:  # sum(lst[:-1]) ->자기 자신을 제외한 값들의 합
        result = ' + '.join(map(str, lst[:-1])) # 값을 문자열로 변환하고, ' + ' 넣어줌
        print(f'{n} = {result}')
    
    else:
        print(f'{n} is NOT perfect.')
```



46. BOJ_10162

`전자레인지`  ❕ 

```python
t = int(input())


if t % 10 != 0 : # 10초 단위가 아니라면
    print(-1)
else:
    a = b = c = 0
    a = t // 300 
    b = (t % 300) // 60
    c = ((t % 300) % 60) // 10
    print(a, b, c)
```



47. BOJ_10103

`주사위 게임`

```python
n = int(input())

c_score = 100
s_score = 100
for i in range(n):
    c, s = map(int, input().split())
    if c < s:		# 상덕이의 점수가 더 큰 경우
        c_score -= s
    
    elif c > s:		# 창영이의 점수가 더 큰 경우
        s_score -= c

print(c_score)
print(s_score)
```



48. BOJ_10214

`Baseball`

```python
# 왜 2중 for문 쓰는지 잘 모르겠음..
t = int(input())
for _ in range(t):
    y_score = 0
    k_score = 0
    for _ in range(9):
        y, k = map(int, input().split())
        y_score += y
        k_score += k
    
    if y_score > k_score:
        print('Yonsei')
    elif y_score < k_score:
        print('Korea')
    else:
        print('Draw')
```



49. BOJ_11557

`Yangjojang of The Year`   ❕ 

```python
t = int(input())
for _ in range(t):
    n = int(input())

    lst_s, lst_l = [], []
    for i in range(n):
        s, l = input().split()
        lst_s.append(s)
        lst_l.append(int(l))

    print(lst_s[lst_l.index(max(lst_l))])
    # l 리스트에서 가장 큰값의 인덱스번호 
```



50. BOJ_10757

`큰 수 A+B`

```python
a, b = map(int,input().split())
print(a + b)
```



