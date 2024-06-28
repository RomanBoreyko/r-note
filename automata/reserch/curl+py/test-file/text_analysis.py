from transformers import pipeline

# Загрузка предобученной модели для анализа текстов
nlp = pipeline("sentiment-analysis")

# Пример текста для анализа
text = "This is an example text for sentiment analysis."

# Анализ текста
result = nlp(text)

# Вывод результата
print(result)

