import random

# 任务3：生成参考文献引用 - 使用分号分隔符
# Задача 3: Генерация библиографических ссылок
try:
    with open('books-en.csv', 'r', encoding='latin-1') as file:
        headers = file.readline().strip().split(';')  # 使用分号分隔# Разделитель - точка с запятой
        all_lines = file.readlines()
    
    print("Столбцы файла:")
    for i, header in enumerate(headers):
        print(f"  Столбец {i}: {header}")
    
    # 根据列名设置索引
    # Индексы столбцов
    author_index = 2  # Столбец Book-Author
    title_index = 1   # Столбец Book-Title
    year_index = 3    # Столбец Year-Of-Publication
    
    # 随机选择20条记录
    # Случайный выбор 20 записей
    if len(all_lines) < 20:
        num_citations = len(all_lines)
    else:
        num_citations = 20
    
    selected_lines = random.sample(all_lines, num_citations)
    
    # 生成引用
    # Генерация ссылок
    citations = []
    for i, line in enumerate(selected_lines, 1):
        fields = line.strip().split(';')  # 使用分号分隔# Используем точку с запятой как разделитель
        if len(fields) > max(author_index, title_index, year_index):
            author = fields[author_index]
            title = fields[title_index]
            year = fields[year_index]
            citation = f"{author}. {title} - {year}"
            citations.append(f"{i}. {citation}")
    
    # 保存到文件
    # Сохранение в файл
    with open('citations.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(citations))
    
    print(f"Сгенерировано {num_citations} библиографических ссылок, сохранено в citations.txt")
    
    # 显示前5条引用作为示例
    # Показываем первые 5 ссылок как пример
    print("\nПримеры первых 5 ссылок:")
    for i in range(min(5, len(citations))):
        print(f"  {citations[i]}")

except FileNotFoundError:
    print("Ошибка: Файл 'books-en.csv' не найден")
except Exception as e:
    print(f"Ошибка: {e}")