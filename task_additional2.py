# 附加任务2：获取最受欢迎的20本书 - 使用分号分隔符
# Дополнительная задача 2: Получение 20 самых популярных книг
try:
    with open('books-en.csv', 'r', encoding='latin-1') as file:
        headers = file.readline().strip().split(';')  # 使用分号分隔
                                                      # Разделитель - точка с запятой
        print("Столбцы файла:")
        for i, header in enumerate(headers):
            print(f"  Столбец {i}: {header}")
        
        # 根据列名设置索引
        # Индексы столбцов
        title_index = 1   # Book-Title列# Столбец Book-Title
        author_index = 2  # Book-Author列# Столбец Book-Author
        downloads_index = 5  # Downloads列（作为受欢迎度指标）# Столбец Downloads (как показатель популярности)
        
        books = []
        for line in file:
            fields = line.strip().split(';')  # 使用分号分隔# Используем точку с запятой как разделитель
            if len(fields) > max(title_index, author_index):
                title = fields[title_index]
                author = fields[author_index]
                
                # 获取下载量（作为受欢迎度指标）
                # Получаем количество загрузок (как показатель популярности)
                downloads = 0
                if downloads_index != -1 and len(fields) > downloads_index:
                    try:
                        downloads = int(fields[downloads_index])
                    except ValueError:
                        downloads = 0
                
                books.append({
                    'title': title,
                    'author': author,
                    'downloads': downloads
                })
        
        # 按下载量排序
        # Сортировка по количеству загрузок
        books.sort(key=lambda x: x['downloads'], reverse=True)
        
        # 取前20本
        # Берем первые 20 книг
        top_books = books[:20]
        
        print(f"\nСамые популярные {len(top_books)} книг (по количеству загрузок):")
        print("=" * 60)
        for i, book in enumerate(top_books, 1):
            print(f"{i:2d}. {book['title']} ({book['author']}) - Загрузок: {book['downloads']}")

except FileNotFoundError:
    print("Ошибка: Файл 'books-en.csv' не найден")
except Exception as e:
    print(f"Ошибка: {e}")