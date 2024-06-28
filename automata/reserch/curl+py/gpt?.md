sudo apt update
sudo apt install python3 python3-pip

sudo apt install python3-venv
python3 -m venv myenv
source myenv/bin/activate

pip install tensorflow transformers

<!-- text_analysis.py -->
from transformers import pipeline

# Загрузка предобученной модели для анализа текстов
nlp = pipeline("sentiment-analysis")

# Пример текста для анализа
text = "This is an example text for sentiment analysis."

# Анализ текста
result = nlp(text)

# Вывод результата
print(result)

<!--  -->

python text_analysis.py

проблема
возникла ошибка при сборке пакета h5py

решение

    подготовка
        sudo apt update
        sudo apt install python3 python3-pip
        sudo apt install python3-venv
        python3 -m venv myenv
        source myenv/bin/activate
        pip install tensorflow transformers

    исправление
        sudo apt install libhdf5-dev
        pip install --upgrade pip setuptools wheel
        pip install tensorflow transformers
        sudo apt install build-essential python3-dev
        pip install numpy
        pip install h5py

    запуск
        pip install tensorflow transformers




from transformers import pipeline

# Загрузка предобученной модели для анализа текстов
nlp = pipeline("sentiment-analysis")

while True:
    text = input("Введите текст для анализа (или 'exit' для выхода): ")
    if text.lower() == 'exit':
        break

    # Анализ текста
    result = nlp(text)

    # Вывод результата
    print(result)
