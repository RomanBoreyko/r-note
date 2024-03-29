
*1

Архитектура транзакций первого епизода первой арки проекта r-comedy.
Арка 1. "Трип Марка":
Заголовок: "Тревожный шаг"
Цели: "Тестирование наполнением, паттерна архитектуры Моно-Трипа по R0_."
Событие: "Контракт Марка"

Тема:
_Идея(Центр автора): 
    Выстраивание архитектуры моно-трипа и натягивание Марка на нее.
_Сверх-задача(амбиции автора. широкое и длительное воздействие на сюжет):
    Генерация мемов для Начальства, через Бардо Суок.
_Сквозное-действие(стремление к сверх-задаче):
    Описание архитектуры моно-трипа и Бардо Суок. Демонстрация практического применения их модулей на бытовом уровне в транзакциях, Играх.
    Сокрытие _Сверх-задачи и _Сквозного-действия от читателя, через алегории и вуалированые лозунги.
_Действие(выполнение-сквозного-действия):
    Марк завершает "Игра на улице", находит\дает себе разрешение прекратить в это играть. Cходит с рельс "Игра на улице" и берет Игру "Карьерист", в ходе которой приобретает навыки генерации мемов для Начальства и осваивает входы в Бардо Суок.
_Контр-свозное-действие:
    Раскрытие _Сверх-задачи и _Сквозного-действия читателю, через работу Орфа. Раскрытие Орфом процесса и итогов генережки мемов для Начальства.
_Конфликт:
    Следак Орф, по запросу инквизитора, цепляет за Марком хвоста. Их интерес, это безопасность Столицы, а Начальство и Администрация ведут себя как отдельное государство и не делятся своими планами и целями, отказывают в приеме.
    # Крысинный Пророк видит Линии. Через Марка, он знает о целях Приманки и стремится им все испортив вмешиваясь в Линии, надеясь сделать не возможным подключение Капкана.

*2

Игры которые будут использованы автором в этом эпизоде или трипе: ""

Участники: "Марк, Орф, хвост, Времяед, Суфлеры, Трагики, Ящики, Пауки, инквизитор, следак, Оператор."

C:\Users\New\Downloads\r-note\ДоХХХХоrm\dev-note\Beta0\Mark\mark-arch.py
C:\Users\New\Downloads\r-note\ДоХХХХоrm\dev-note\content\oper-arch.py

Роли Участников:

-- Игрок: "Оператор"
- Какая роль у этого персонажа: "Подключать Капканы к Линиям таймлайна"
- Дополнительная информация о роли: "Функция Шарда Аббадона из кластера Приманки. Он не появляется в мире Марка физически. Он обитает в Бардо Суок, в Квантовом Поле, во снах Марка."

-- Подыгрывающий: "Марк"
- Какая роль у этого персонажа: "Стать Пустой Шкурой для Оператора. Служить укрытием от Суок."
- Дополнительная информация о роли: "Принимает Контракт от Начальства, устраиваясь курьером."

-- Спаситель\Преследователь: "Орф"
- Какая роль у этого персонажа: "Собирать данные про Начальство и противодействовать ему в интересах Инквизитора."
- Дополнительная информация о роли: "Подсылает к Марку хвост. Готовит рейд в Театре."

-- Простак\Спонсор: "Времяед"
- Какая роль у этого персонажа: ""
- Дополнительная информация о роли: ""

-- Зачинщик/Подстрекатель: "Начальство"
- Какая роль у этого персонажа: "Отдает приказы персоналу Театра и генерит мемы для Хоста для связывания этого Круга с таймлайном продакшына."
- Дополнительная информация о роли: "Притворяется четверным агентом."

Ландшафт:
__Локация:  "Столица"
_цвета - "Серый. Темно синий. Серебро. Черные тени."
_настроение - "Осень"
__Инструмменты: ""



*3





































Локация(Столица, Театр):

'''

    Он пришел к нам под утро, просился пускать его на ночевку. Я отвел его на задний двор к пруду, показал на рыб и сказал кормить их месяц, если не здохнут, будем пускань на ночь.

    Он трогал скамейки на площади перед Театром, стены Театра и слизывал налет с пальцев, привыкая к нашим культурам.
'''


^Отвержение призыва:
    Герой сначала отказывается от призыва.

'''
    А рыбы таки сдохли. Начальство загрузило новых, а Марку предложили работать за кров на ночь. Он отказался, но уйти не смог. Ему стало плохо и он свалился в колодец за Театром.
'''
_ТемаМотив(): Потеря власти

%2. Мотивация. Стимул.
    ^Помощь или запрет: 
        Герою предлагается помощь или дается запрет на выполнение задачи.

(7.1.) Вход
    @1(Оператор-Марк): "Крючок-наживка(Провокация)" 
    _Слабость {Марк траванулся культурой Начальства}
    _Подставка {Оператор предлагает Марку Контракт на лечение и спонсорство}
_ТемаМотив(): Воспитание волшебниками
{
    Оператор: " - В кои-то веки удалось коту с печки спрыгнуть, и то лапки отшиб."
    Марк: " - Не смешно."
    Оператор: " - Хорошая шутка не обязана быть смешной. Она должна быть... красивой."
    Марк: " - Где я?"
    Оператор: " - А на что это похоже?"
    Марк{Смотрит на звезды. На тьму во всех сторонах и черный туман под ногами. На собеседника,черную, матовую, не подвижную фигуру в густых тенях, блестящуюю двумя зеленоватыми точками глаз. От нее по полу раскинулись толстые гладкие хвосты. Он поднимает с земли свою палку и говорит ей}: " - Если бы это был сон, я бы не подозревал что это сон, а значит это постанова. У нас собеседование?"
    Оператор: " - И ты прошел первый этап, поздравляю! Второй этап, проверка знания теории. Если вы готовы."
    Марк: " - А как отсюда уйти?"

    Оператор: " - Так же как проснутся, вы это делает каждую ночь. Как прийдет время, быстро разберетесь. Я вас тут не держу."
    Марк{расхаживает вокруг, трогает носком хвосты, они твердые и не подвижные, думает пробежатся во тьму}: " - Давай свои вопросы."
    Оператор: " - Что такое Пустые Шкуры?"
    Марк: " - Прилипалы. Потеряные. Просящие их заполнить."
    Оператор: " - Как их носят?"
    Марк: " - Следующий."
    Оператор: " - Что занешь про нашу валюту?"
    Марк: " - Мемасики. Добываются из Игр. Меняются, покупаются, сшиваются, разрабатываются. Ценятся новые. Чем старше тем сильнее подвержен инфляции. Итоговая ценность назначается Начальством."
    Оператор: " - Хорошо. Работал курьером?"
    Марк: " - Доставлял приглашения в Институт и Канцелярию."
    Оператор: " - Мне нужно почти тоже самое, только вместо бумажек нужно доставлять меня. Приходим на адрес, распаковуемся. Я делаю работу и обратно запаковуемся идем на следующий адрес. Плачу новыми мемами про которые у Начальства еще не слы ..."
    Марк: " - Где взял? Как? Сколь..."
}

@2(Оператор-Марк): "Переключение\включение:"
    Оператор{цепляет за ногу и швыряет в небо, оно оказывается низким бумажным потолком, за ним, звезды это тусклые Линии уходящие в хаотичное прядево за которым зияет, Колыбель Суок отторгающая частички не комфортные за стремлении к порядку. Они зажигаются, падают и вытягиваются в Линии переплетаясь с другими чье излучение ... }: " - Запомни это, а еще метафизическое пространство и квантовое поле. Замыкающий мем получишь когда рабта будет сделана. Работаем?"

@3(Оператор-Марк): "Замешательство\невмешательство:"
    ^Встреча с наставником: 
        Герой встречает наставника, который предоставляет ему знания и инструменты.

@4(Оператор-Марк): "Расплата(Выигрыш\кукиш):" (Марк)
{
    Принимает Контракт стажировку курьером и культуру Начальства. Когда или тогда его вытащили из Колодца. Кивает сосредоточено запоминая все ему врученное и поглядывает на бескрайнее, целое, звездное небо.
}


(6) Что происходит снаружи, наука, техника, бизнес, политика.

&АктБ. Инициация. Плато.:
_Функция(): Вылазка из дома
_ТемаМотив(): Путешествие
    ^Пересечение первого порога: 
        Герой начинает свое путешествие.
_Функция(Марк): Герой служит или работает

(7.2.) Плато {}
    @2(Начальство-Марк): "Переключение\включение:"
Локация(Столица, Канцелярия):

'''
    письма в 
    Мы носились по мостовым Столицы. 

    За такими нужен гдлаз да глаз пока не научатся. Потом можно будет проведовать время от времени, чтобы они сильно не забывались.

'''
Локация(Столица, Институт Инквизиции):
'''
Орф
'''
Локация(Столица, Мертвый Дом):
'''
Пауки и Ящики
'''
Локация(Столица, Поместье Лиличей):
'''
Нина, Аглая, Меркин.
'''































