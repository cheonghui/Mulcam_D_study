## BOJ_Python 배우기2



11. BOJ_2163


`초콜릿 자르기`

```python
# N*M 크기의 초콜릿을 1×1 크기의 초콜릿으로 쪼개기 위한 최소 쪼개기 횟수 구하기
n, m = map(int, input().split())
print(n*m-1)
# 왜 n*m-1인지 대충 이해는 했으나 정확히 이해하지못함 ❗
```



11. BOJ_11021 


`A+B - 7`

```python
t = int(input())
# 첫째 줄에 입력받을 값을 T에 할당한다.

for i in  range(t):
# for문을 이용해 입력받은 t만큼 아래의 과정을 반복한다.
  a, b = map(int, input().split())
  # 변수a, b에 공백을 포함한 정수를 입력받는다.
  print(f'Case #{i+1}: {a+b}')
  #f-string 문자열 내에서 변수를 사용 
```



11. BOJ_11022


`A+B - 8 `

```python
t = int(input())
# 첫째 줄에 입력받을 값을 T에 할당한다.

for i in  range(t):
# for문을 이용해 입력받은 t만큼 아래의 과정을 반복한다.
  a, b = map(int, input().split())
  # 변수a, b에 공백을 포함한 정수를 입력받는다.
  print(f'Case #{i+1}: {a} + {b} = {a+b}')
  #f-string 문자열 내에서 변수를 사용 
```



11. BOJ_10699


`오늘 날짜`  ❕ 

```python
import datetime
# datatime모듈을 이용해 현재시간을 가져온다.

d = datetime.datetime.utcnow() + datetime.timedelta(hours=9)# 9시간을 더해준다
# 힌트 잘 봐야함!! 채점서버시간대UTC+0, 서울시간대 UTC+9 -> 9시간이 차이나기 때문에 채점서버시간대UTC+0에 9시간을 더해줌

# 출력 답1
print(d.strftime('%Y-%m-%d'))
# strftime - 출력 포맷을 설정

# 출력 답2
# print(str(d)[:10])
# d를 문자열 타입으로 바꿔 준 후 슬라이싱


# 만약 서버 채점시간대가 UTC+9로 설정되어있었다면?
# d = datetime.datetime.now()
# print(d.isoformat())
```

참고사이트: https://www.daleseo.com/python-datetime/

11. BOJ_7287


`등록`

```python
# 맞은 문제의 수와 아이디를 그대로(중요@!) 출력

print('27')
# 백준 사이트 내에서 내가 맞은 문제의 개수를 확인
print('cheongh22')
# ID
```



11. BOJ_2525


`오븐 시계`

```python
start_h, start_m = map(int,input().split())
# 요리 시작 시간,분을 공백을 두고 정수로 입력받는다.

cooktime = int(input())
# 요리시간(분)을 입력받는다.
end_h = (start_h * 60 + start_m + cooktime) // 60 #//몫의 소수점 자리는 버리고 가져옴
end_m = (start_h * 60 + start_m + cooktime) % 60 


if end_h >= 24:
    print(end_h % 24, end_m)
    # 요리시간이 24 이상일 경우 24를 나눈 나머지 값을 구한다.
else:
    print(end_h, end_m)
```



11. BOJ_2530


`인공지능 시계` ❕

```python
# 오븐구이가 끝나는 시각(시(0~23), 분, 초) 구하기

a, b, c = map(int, input().split())
# 현재시간 시,분,초를 공백을 포함한 정수형태로 입력받는다.

d = int(input())
# 요리시간(초)

s = (c + d) % 60
m = (b + (c + d) // 60) % 60
h = (a + (b + (c + d) // 60) // 60) % 24

print(h, m, s)
# 시, 분, 초 출력
```



11. BOJ_2914


`저작권`

```python
# 적어도 몇 곡이 저작권이 있는 멜로디인지 구하기

a, i = map(int, input().split())
print(a * (i-1)+1)
# ? / a = i -> ?= i * a
# i는 평균값에서 올림된 값이기 때문에 -1을 해준다.
# 최소값을 구해야하기 때문에 마지막에 1을 더해줌
```



11. BOJ_5355


`화성수학` ❕

```python
t = int(input())

for _ in range(t):
    mars = list(input().split())
    answer = 0
    for i in mars:
        if i == '@':
            answer *= 3
        elif i == '%':
            answer += 5
        elif i == '#':
            answer -= 7
        else:
            answer += float(i)

    print('%0.2f' % answer)
   	# answer의 값을 소수점 둘째 자리까지 출력
```



11. BOJ_2675


`문자열 반복`

```python
t = int(input())

for _ in range(t):
    r, s = input().split()
    for i in s:
        print(int(r) * i, end='')
    print()
```



