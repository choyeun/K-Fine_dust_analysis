# K-미세먼지 분석

## 데이터 수집

최근 1년간의 미세먼지 데이터를 수집하였습니다.<br/>
데이터는 한국환경공단의 에어코리아 사이트에서 2023년 10월 부터 2024년 9월까지의 데이터를 수집하였습니다.<br/>

<br/>
데이터는 xls 파일로 제공되었습니다.<br/>
xls를 일단 csv로 변환하였습니다.<br/>
<br/>
[merge_csv.py](merge_csv.py)를 이용하여 csv 파일을 하나로 합쳤습니다.<br/>
<br/>

## 데이터 분석

[main.ipynb](main.ipynb)을 통해 데이터를 분석하였습니다.<br/>
<br/>
제공된 데이터는 매일 전국의 미세먼지 지수였기에
이를 월별 계졀별 데이터로 나타내고자 하였습니다.<br/>

처음에는 백지도를 이용해서 미세먼지 수치에 따라서 해당 지역의 색상을 변경하여 미세먼지 지도를 만들고자 하였으나 제대로 된 백지도를 찾지 못하여 지도 구현을 실패하였습니다.<br/>


월 평균 미세먼지 농도 구하는 과정에서 평균을 구할때 https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.groupby.DataFrameGroupBy.mean.html 를 참고했습니다
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html 을 사용해 문자열 일수도 있는것을 숫자로 변환했습니다

오른쪽 상단에 범주를 띄우기 해서 https://matplotlib.org/2.0.2/api/pyplot_api.html#matplotlib.pyplot.legend 를 참고하였습니다

계절별 미세먼지 농도를 구하기 위해서 계절을 구하는 함수를 만들었습니다.


## 데이터 시각화 결과

결과 사진을 보면 1년중 미세먼지 농도가 가장 높은 수치를 기록한 도시는 세종시이고
가장 낮은 수치를 기록한 도시는 울산입니다

또한 미세먼지는 대체로 겨울에 가장 수치가 높고 여름이 가장 수치가 낮았습니다.
이는 중국에서 영향을 끼치는 기단(앙쯔강 기단, 시베리아 고기압)이 주로 겨울철에 한국에 영향을 끼친다는것을 의미합니다

### 월 평균 미세먼지 농도 - 지역별

![img.png](img.png)

### 월 평균 미세먼지 농도 - 대한민국 전체
![img_1.png](img_1.png)

### 계절별 미세먼지 농도 - 지역별
![img_2.png](img_2.png)

### 계절별 미세먼지 농도 - 대한민국 전체
![img_3.png](img_3.png)
