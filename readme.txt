Простая программа для заучивания любых данных, представленных в виде карточек. Писалась, как инструмент для изучения английских фраз.

Суть проста - отображается карточка с английской фразой (или иной информацией), перевод фразы изначально скрыт, отображается при наведении курсора на фразу. Карточку можно пропустить, или поставить отметку "не показывать снова". Соответсвенно, карточки с пометкой "не показывать снова" при следующих запусках программы отображены не будут.
Пары фраза-перевод, а также, соответствующий им атрибут "не показывать снова" читаются из .xlsx-файла.

Для отображения карточек необходим файл .xlsx, состоящий из трех колонок.
Первая колонка - английские фразы. Данные из строк этой колонки будут отображаться сразу.
Вторая колонка - перевод английских фраз. Эти данные будут отображаться только после наведения курсора на карточку с английской фразой.
Третья колонка - признак, отображать ли карточку снова, значение 1 или 0 в их числовом эквиваленте (число, а не строка).
1 - отображаем карточку при повторном запуске программы или после отображения всех карточек по кругу. 0 - карточку не отображаем пока.

Файл с фразами прилагается в ./files/words.xlsx. Фразы брал из русско-английского разговорника. Вместо английских слов можно использовать, например, иторические даты с их описанием,
физические формулы или еще что-то, что можно заучить с помощью описанного выше принципа карточек.