## BOJ_ Python 배우기1

[문제보러가기](https://www.acmicpc.net/workbook/view/459)

1. BOJ_2557

` Hello World`

```python
# Hello World! 출력
print('Hello World!')
# 문자열이기 때문에 ''안에 묶어주고 print로 출력
```



2. BOJ_1000

`A+B`

```python
# 입력받은 A,B를 더하기
a, b = map(int,input().split())
# input() 값을 입력받는 함수(입력받은 값은 자동으로 문자열로 변함)
# 공백을 두고 입력받기 때문에 .split()으로 잘라줌
# map 함수를 이용하여 a,b를 정수타입(int)으로 바꿔줌

print(a + b)
```



3. BOJ_10998

`AxB`

```python
# 입력받은 A,B를 곱하기
a, b = map(int,input().split())

print(a * b)
# 곱셈연산자 *
```



4. BOJ_1001

`A-B`

```python
# 입력받은 A,B를 빼기
a, b = map(int,input().split())

print(a - b)
```



5. BOJ_1008

`A/B`

```python
# 입력받은 A,B를 나누기
a, b = map(int,input().split())

print(a / b)
# 나눗셈연산자(몫) /
```



6. BOJ_10869

`사칙연산`

```python
a, b = map(int,input().split())

print(a + b)
print(a - b)
print(a * b)
print(a // b)
# 나눗셈 연산자 // 몫의 소수점 아랫자리를 버리게 됨
print(a % b)

```



7. BOJ_10430

`나머지`

```python
a, b, c = map(int,input().split())

print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)
```



8. BOJ_2558

`A+B-2`

```python
#두 줄로 입력받은 후 덧셈
a = int(input())
b = int(input())

print(a + b)
```



9. BOJ_2588

`곱셈`

```python
#(세 자리 수) × (세 자리 수)
num_1 = int(input())
num_2 = input()

#문자열 인덱싱으로 곱해 줄 값을 빼온 후 다시 정수형태로 바꿔줌
print(num_1 * int(num_2[2]))
print(num_1 * int(num_2[1]))
print(num_1 * int(num_2[0]))
print(num_1 * int(num_2))
```



10. BOJ_3046

`R2`

```python
# r1과 s를 이용하여 r2구하기

r1, s = map(int, input().split())

# (r1 + r2) / 2 = s 
# r2 = s * 2 - r1 
print(s * 2 - r1)
```

