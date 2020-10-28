# CE, LE 계산

## LE 90

### 1) 관측값 평균이 0일 경우
LE_XX = P(확률계수)  *  𝜎𝑧 (표준편차)

1) 관측값에 대한 표준편차를 구함
2) 아래의 표에서 p=90/100(0.90) 에 대한 확률 계수인 1.6449를 구함
3) 표준편차와  확률 계수(P)를 곱함
=> LE_90 = 1.6449 * (표준편차)

![LE 확률계수](https://user-images.githubusercontent.com/33948753/97400754-03a36b00-1933-11eb-85e7-90f02947494f.png)

### 2) 관측값 평균이 0이 아닐 경우

1) 기준점과 측정점을 통해 표준편차와 평균을 구함
2) 위의 식(누적분포함수)에서 p 값을 계산
3) p 값에 대해 오차 역함수(Inverse Error Function)을 구함
4) 아래의 식을 통해 LE를 계산
