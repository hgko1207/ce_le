# CE, LE 계산

## LE 90

### 1) 관측값 평균(오차 평균)이 0일 경우
- LE_XX = P(확률계수)  *  𝜎𝑧 (표준편차)

1) 관측값에 대한 표준편차를 구함
2) 아래의 표에서 p=90/100(0.90) 에 대한 확률 계수인 1.6449를 구함
3) 표준편차와  확률 계수(P)를 곱함
- LE_90 = 1.6449 * (표준편차)

![확률계수](https://user-images.githubusercontent.com/33948753/97401614-75c87f80-1934-11eb-8b69-c2eb2814d0d0.png)

### 2) 관측값 평균이 0이 아닐 경우

![누적분포함수](https://user-images.githubusercontent.com/33948753/97401162-a360f900-1933-11eb-9faf-cb3a7a4adca6.png)

1) 기준점과 측정점을 통해 표준편차와 평균을 구함
2) 위의 식(누적분포함수)에서 p 값을 계산
3) p 값에 대해 오차 역함수(Inverse Error Function)을 구함
4) 아래의 식을 통해 LE를 계산

![LE 계산](https://user-images.githubusercontent.com/33948753/97401661-8e389a00-1934-11eb-9636-ea0953ec2742.png)

## CE 90

### 1) 관측값 평균이 0일 경우

- CE_XX = R * 𝜎𝑚𝑎𝑥

1) 2x2 공분산 행렬을 계산하고, 공분산 행렬에 대해 고유값(Eigenvalue) 계산
2) 최소, 최대 고유값에 대해 제곱근으로 𝜎𝑚𝑖𝑛, 𝜎𝑚𝑎𝑥 값을 구함
    예) MATLAB은 eig(A) 함수를 사용
3) r = 𝜎𝑚𝑖𝑛/𝜎𝑚𝑎𝑥, p=90/100 두 개의 값과 표의 값을 통해 선형 보간하여 
    확률 계수(R)를 구함
    - 예) r = 0.509, p = 0.9 일 때,
        R = 0.041/0.05 * 1.7371 + 0.009/0.05 * 1.7621 = 1.7416
4) 확률 계수(R)와 𝜎𝑚𝑎𝑥를 곱함

![확률계수](https://user-images.githubusercontent.com/33948753/97403112-29327380-1937-11eb-8116-ee2af14b134c.png)

### 2) 관측값 평균이 0이 아닐 경우

![size](https://user-images.githubusercontent.com/33948753/97402998-f2f4f400-1936-11eb-9f3f-d092cfe468f9.png)

1) X, Y 축에 대해 각각 공분산 값을 구하고 2x2 공분산 행렬을 계산.
2) i 수만큼 위의 수식으로 2x1(X, Y)의 Si 를 계산.
3) Si 의 크기를 가장 작은 것부터 가장 큰 것 순으로 정렬.(크기는 아래 수식과 같음)
- ![si](https://user-images.githubusercontent.com/33948753/97402910-bc1ede00-1936-11eb-8f35-1e7d7e84afd5.png)
4) RExx는 xx% 가장 큰 크기, RE*xx는 다음으로 큰 크기를 지정.
5) CE_XX 계산은 아래 수식으로 계산.

![ce_xx](https://user-images.githubusercontent.com/33948753/97403061-1324b300-1937-11eb-8c68-e725e3591ff3.png)

## 참고

### 1) 관측값

지상기준점 - 측정점

### 2) 공분산(Covariance)

관측값에 대한 공분산

![공분산](https://user-images.githubusercontent.com/33948753/97402002-2cc4fb00-1935-11eb-85fb-a077b6a28d5a.png)

### 3) 분산(Variance)

관측값에 대한 분산

![분산](https://user-images.githubusercontent.com/33948753/97402291-a9f07000-1935-11eb-9e6a-8156f0059dc9.png)

### 4) 공분산 행렬

두 개의 확률 변수의 공분산 행렬은 각 변수 쌍에 대해 계산된 공분산 값으로 구성된 행렬

![공분산 행렬](https://user-images.githubusercontent.com/33948753/97402621-2d11c600-1936-11eb-8b23-78c26940c730.png)

### 5) 표준편차(Standard Deviation)

관측값에 대한 표준편차

![표준편차](https://user-images.githubusercontent.com/33948753/97401571-60535580-1934-11eb-8185-8775b97c8c1b.png)
