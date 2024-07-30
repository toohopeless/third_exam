import csv
from collections import defaultdict
import matplotlib.pyplot as plt


def read_sales_data(file_path):
    sales_data = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            sales_data.append({
                'product_name': row[0],
                'quantity': int(row[1]),
                'price': float(row[2]),
                'date': row[3]
            })
    return sales_data


def total_sales_per_product(sales_data):
    sales_per_product = defaultdict(float)
    for sale in sales_data:
        total_price = sale['quantity'] * sale['price']
        sales_per_product[sale['product_name']] += total_price
    return sales_per_product


def sales_over_time(sales_data):
    sales_per_date = defaultdict(float)
    for sale in sales_data:
        total_price = sale['quantity'] * sale['price']
        sales_per_date[sale['date']] += total_price
    return sales_per_date


def plot_total_sales_per_product(sales_per_product):
    products = list(sales_per_product.keys())
    sales = list(sales_per_product.values())

    plt.figure(figsize=(10, 6))
    plt.bar(products, sales, color='red')
    plt.xlabel('Продукты')
    plt.ylabel('Общая сумма продаж')
    plt.title('Общая сумма продаж по продуктам')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


def plot_sales_over_time(sales_per_date):
    dates = list(sales_per_date.keys())
    sales = list(sales_per_date.values())

    plt.figure(figsize=(10, 6))
    plt.plot(dates, sales, marker='o', linestyle='-', color='b')
    plt.xlabel('Дата')
    plt.ylabel('Общая сумма продаж')
    plt.title('Общая сумма продаж по дням')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


# Основной блок программы
if __name__ == "__main__":
    file_path_sales = 'sales_data.csv'
    sales_data_list = read_sales_data(file_path_sales)

    total_sales_per_product_dict = total_sales_per_product(sales_data_list)
    total_sales_per_date_dict = sales_over_time(sales_data_list)

    # Определяем продукт с наибольшей выручкой
    max_product = max(total_sales_per_product_dict, key=total_sales_per_product_dict.get)
    print(f"Продукт с наибольшей выручкой: {max_product}, сумма: {total_sales_per_product_dict[max_product]}")

    # Определяем день с наибольшей суммой продаж
    max_date = max(total_sales_per_date_dict, key=total_sales_per_date_dict.get)
    print(f"День с наибольшей суммой продаж: {max_date}, сумма: {total_sales_per_date_dict[max_date]}")

    # Строим графики
    plot_total_sales_per_product(total_sales_per_product_dict)
    plot_sales_over_time(total_sales_per_date_dict)
