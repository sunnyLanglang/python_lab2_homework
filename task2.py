# 任务2：按作者搜索书籍（价格≥200卢布）- 使用分号分隔符
# Задача 2: Поиск книг по автору (цена ≥ 200 рублей)
try:
    with open('books-en.csv', 'r', encoding='latin-1') as file:
        headers = file.readline().strip().split(';')  # 使用分号分隔
                                                      # Разделитель - точка с запятой
        print("Столбцы файла:")
        for i, header in enumerate(headers):
            print(f"  Столбец {i}: {header}")
        
        # 根据列名设置索引
        # Индексы столбцов
        author_index = 2  # Book-Author列# Столбец Book-Author
        title_index = 1   # Book-Title列# Столбец Book-Title
        price_index = 6   # Price列
        
        # 获取作者名
        # Получаем имя автора
        author_name = input("Введите имя автора (Enter для использования 'Tolstoy' по умолчанию): ").strip()
        if not author_name:
            author_name = "Tolstoy"
        
        results = []
        for line in file:
            fields = line.strip().split(';')  # 使用分号分隔# Используем точку с запятой как разделитель
            if len(fields) > max(author_index, price_index, title_index):
                if author_name.lower() in fields[author_index].lower():
                    try:
                        price = float(fields[price_index])
                        if price >= 200:
                            results.append({
                                'title': fields[title_index],
                                'author': fields[author_index],
                                'price': price
                            })
                    except ValueError:
                        continue
        
        print(f"\nНайдено {len(results)} книг автора {author_name} (цена ≥ 200 рублей):")
        for i, book in enumerate(results, 1):
            print(f"{i}. {book['title']} - {book['price']} руб.")

except FileNotFoundError:
    print("Ошибка: Файл 'books-en.csv' не найден")
except Exception as e:
    print(f"Ошибка: {e}")