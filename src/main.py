from crowling_data import crowling_data
from googletrans import Translator
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import time

# 데이터 크롤링
data_list = crowling_data("18166545")  # 카카오맵 ID (예시: "18166545")

# 데이터 리스트를 최대 50개로 제한
data_list = data_list[:50]

# Translator 객체 생성
translator = Translator()

# 리스트의 모든 항목을 영어로 번역
sentences = []
print(len(data_list))
for i in data_list:
    try:
        translated_text = translator.translate(i, dest="en").text
        sentences.append(translated_text)
        time.sleep(0.1)  # 0.1초 대기 후 재시도
    except Exception as e:
        print(f"번역 오류: {i}")

# SentimentIntensityAnalyzer 객체 생성
analyzer = SentimentIntensityAnalyzer()

# 감정 점수를 저장할 리스트
ratings = []

for sentence in sentences:
    vs = analyzer.polarity_scores(sentence)  # 점수 dictionary
    compound_score = vs["compound"]
    # compound 점수를 기반으로 별점 계산
    rating = (compound_score + 1) * 2.5  # -1 ~ 1을 0 ~ 5로 변환
    ratings.append(rating)
    print("{:-<65} {}".format(sentence, str(vs)))
    print("Calculated Rating: {:.2f}".format(rating))

# 별점을 출력
print("Ratings:", ratings)
