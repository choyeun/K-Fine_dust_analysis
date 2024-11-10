import pandas as pd

# 파일 이름을 수동으로 배열에 넣기
files = [
    "./202310.csv", "./202311.csv", "./202312.csv",
    "./202401.csv", "./202402.csv", "./202403.csv",
    "./202404.csv", "./202405.csv", "./202406.csv",
    "./202407.csv", "./202408.csv", "./202409.csv"
]
output_file_path = './merged_sorted.csv'

# 병합 작업
merged_data = pd.DataFrame()

for file in files:
    try:
        data = pd.read_csv(file)
        merged_data = pd.concat([merged_data, data], ignore_index=True)
    except FileNotFoundError:
        print(f"파일 {file}이(가) 없습니다. 건너뜁니다.")

# 날짜 열을 기준으로 정렬 (열 이름이 'date'인 경우)
if '날짜' in merged_data.columns:
    merged_data = merged_data.sort_values(by='날짜')

# 병합된 데이터 저장
merged_data.to_csv(output_file_path, index=False)
print(f"병합된 데이터가 {output_file_path}에 저장되었습니다.")