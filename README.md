# Итоговое задание №3

Используя полученные в этом блоке знания вам необходимо написать программу, которая будет анализировать данные о продажах продуктов в магазине и строить графики наглядного представления информации.

В ходе создания программы вам необходимо реализовать следующие функции:

read_sales_data(file_path), которая принимает путь к файлу и возвращает список продаж. Продажи в свою очередь являются словарями с ключами product_name, quantity, price, date (название, количество, цена, дата).
total_sales_per_product(sales_data), которая принимает список продаж и возвращает словарь, где ключ - название продукта, а значение - общая сумма продаж этого продукта.
sales_over_time(sales_data), которая принимает список продаж и возвращает словарь, где ключ - дата, а значение общая сумма продаж за эту дату.
 

Входные данных должны храниться в файле (файл должен быть в том же репозитории проекта, чтобы мы могли проверить задание в полной мере), последовательность данных в файле выбирается на ваше усмотрение, с учетом правила "одна строка - один товар".

Пример входных данных:

яблоки, 10, 15, 2024-06-21
груши, 16, 11, 2024-06-22
сливы, 20, 15, 2024-06-19
печенье, 16, 23, 2024-06-20
сливы, 21, 15, 2024-06-16
яблоки, 16, 15, 2024-06-20
конфеты Рот-Фронт, 11, 22, 2024-06-24
сливы, 6, 15, 2024-06-20
 

В ходе анализа данных из файла необходимо вывести на экран два значения:

Определить, какой продукт принес наибольшую выручку.
Определить, в какой день была наибольшая сумма продаж.
 

В завершении работы вашей программы необходимо построить два графика:

Построить график общей суммы продаж по каждому продукту.
Построить график общей суммы продаж по дням.
