import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager, rc

# Windows에서 한글 폰트 설정 (예: 맑은 고딕)
font_path = "C:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)


# 데이터 읽기 및 타입 변환
data = pd.read_csv('./merged_sorted.csv')
data['날짜'] = pd.to_datetime(data['날짜'])

# 월별 평균 구하기
data['월'] = data['날짜'].dt.to_period('M')
monthly_data = data.groupby('월').mean(numeric_only=True)  # 숫자형 데이터만 평균 계산

# 그래프 그리기
plt.figure(figsize=(14, 8))
for column in monthly_data.columns:
    plt.plot(monthly_data.index.astype(str), monthly_data[column], label=column)

plt.title("월 평균 미세먼지 농도 - 지역별")
plt.xlabel("월")
plt.ylabel("미세먼지 농도 (µg/m³)")
plt.legend(loc="upper right", ncol=2)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Calculate the monthly mean across all regions (i.e., nationwide average)
monthly_data['전국 평균'] = monthly_data.mean(axis=1)

# Plot monthly average PM levels for the entire country
plt.figure(figsize=(12, 6))
plt.plot(monthly_data.index.astype(str), monthly_data['전국 평균'], label="전국 평균", marker='o')

plt.title("월 평균 미세먼지 농도 - 대한민국 전체")
plt.xlabel("월")
plt.ylabel("미세먼지 농도 (µg/m³)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# '계절' 컬럼을 추가
def get_season(month):
    if month in [12, 1, 2]:
        return '겨울'
    elif month in [3, 4, 5]:
        return '봄'
    elif month in [6, 7, 8]:
        return '여름'
    else:
        return '가을'

data['계절'] = data['날짜'].dt.month.apply(get_season)

# 계절별 평균값 계산 (숫자형 데이터만 포함)
seasonal_data = data.groupby('계절').mean(numeric_only=True)

# 그래프 그리기
plt.figure(figsize=(14, 8))
for column in seasonal_data.columns:
    plt.plot(seasonal_data.index, seasonal_data[column], label=column, marker='o')

plt.title("계절별 미세먼지 농도 - 지역별")
plt.xlabel("계절")
plt.ylabel("미세먼지 농도 (µg/m³)")
plt.legend(loc="upper right", ncol=2)
plt.tight_layout()
plt.show()

# Calculate the seasonal mean across all regions (i.e., nationwide average)
seasonal_data['전국 평균'] = seasonal_data.mean(axis=1)

# Plot seasonal average PM levels for the entire country
plt.figure(figsize=(10, 6))
plt.plot(seasonal_data.index, seasonal_data['전국 평균'], label="전국 평균", marker='o')

plt.title("계절별 미세먼지 농도 - 대한민국 전체")
plt.xlabel("계절")
plt.ylabel("미세먼지 농도 (µg/m³)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

