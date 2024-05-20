from crowling_data import crowling_data
from googletrans import Translator
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import time

# 데이터 크롤링
data_list = crowling_data("18166545")
# Translator 객체 생성
translator = Translator()
# 리스트의 모든 항목을 영어로 번역
sentences = []
print(len(data_list))
for i in data_list:
    try:
        translated_text = translator.translate(i, dest="en").text
        sentences.append(translated_text)
        time.sleep(0.1)  # 1초 대기 후 재시도
    except Exception as e:
        print(f"번역 오류: {i}")

analyzer = SentimentIntensityAnalyzer()
for sentence in sentences:
    vs = analyzer.polarity_scores(sentence)
    print("{:-<65} {}".format(sentence, str(vs)))
