Задание:

Необходимо написать класс/интерфейс Algorithm, в котором будет, как минимум, один метод apply, который может 
принимать аргументы при необходимости.
Предполагается, что на основе данного интерфейса будут реализовываться различные алгоритмы.

Пример алгоритма:
Подсчет среднего времени ответа, алгоритм на вход принимает список кортежей, первый элемент - код ответа
(число в диапазоне от 100 до 600), второй элемент - время ответа (число от 0.0 до 100.0). 
В ответе необходимо вывести 3 числа - среднее время ответа за последние 5, 10 и 20 записей по каждому коду ответа. 
При этом, если данных в текущем запросе недостаточно, должны быть взяты данные из предыдущего запроса.

Необходимо:
1.	Написать класс/интерфейс
2.	Предусмотреть различные сложности с алгоритмами, при необходимости расширить интерфейс
3.	Предусмотреть обработку ошибок в самих алгоритмах
4.	(Опционально) Написать реализацию класса для алгоритма из примера.
5.	(Опционально) Написать веб-сервис, который будет применять алгоритм из примера, на GET-запрос, 
     формат запроса и ответа - не важен, главное, чтобы его можно было прочитать.
     
     
Структура:

1. Файл Code_example.ipynb:
   Реализация кода для пунктов 1-4 с примерами
   
2. Файл algo/urls.py
   В нем определен урл, по которому можно вызвать фунцию, выдающую ответ для алгоритма из задания
   
3. Файл algo/views.py
   В этом файле описаны все используемые функции
   
4. Файл algo/tests.py
   Тест, проверяющий работу основной функции
   
   В остальных файлах нет какой-то существенной информации


