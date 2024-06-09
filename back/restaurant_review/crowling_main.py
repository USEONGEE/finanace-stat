from .crowling_data import crowling_data
from googletrans import Translator
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from restaurant_review.models import Restaurant, Review
import time
import threading


def process_reviews(restaurant_id):
    try:
        # Restaurant 객체 가져오기
        restaurant = Restaurant.objects.get(id=restaurant_id)
        place_id = restaurant.place_id

        # 데이터 크롤링
        data_list = crowling_data(place_id)
        print(len(data_list))

        # 데이터 리스트를 최대 50개로 제한
        if len(data_list) > 50:
            print("Data list is too long. Truncating to 50 items.")
            data_list = data_list[:50]

        # Translator 객체 생성
        translator = Translator()

        # 리스트의 모든 항목을 영어로 번역
        sentences = []
        original_sentences = []
        for i in data_list:
            try:
                translated_text = translator.translate(i, dest="en").text
                sentences.append(translated_text)
                original_sentences.append(i)
                time.sleep(0.01)  # 0.1초 대기 후 재시도
            except Exception as e:
                print(f"번역 오류: {i}")

        # SentimentIntensityAnalyzer 객체 생성
        analyzer = SentimentIntensityAnalyzer()

        # 감정 점수를 저장할 리스트
        for original_sentence, sentence in zip(original_sentences, sentences):
            vs = analyzer.polarity_scores(sentence)  # 점수 dictionary
            review = Review(
                restaurant=restaurant,
                review_text=original_sentence,  # 원문 저장
                # translated_text=sentence,  # 번역된 텍스트 저장
                positive_score=vs["pos"],
                negative_score=vs["neg"],
                neu_score=vs["neu"],
                compound_score=vs["compound"],
                rating=(vs["compound"] + 1) * 2.5,  # -1 ~ 1을 0 ~ 5로 변환
            )
            review.save()
            print("{:-<65} {}".format(sentence, str(vs)))
            # TODO  rating 공식 변경 해야함
            print("Calculated Rating: {:.2f}".format(review.rating))

        # 작업이 완료되면 restaurant를 활성화
        restaurant.activate_restaurant()

    except Restaurant.DoesNotExist:
        print(f"Restaurant with id {restaurant_id} does not exist.")


# 특정 restaurant_id로 스레드를 시작하여 리뷰를 처리합니다.
def start_review_processing(restaurant_id):
    threading.Thread(target=process_reviews, args=(restaurant_id,)).start()
