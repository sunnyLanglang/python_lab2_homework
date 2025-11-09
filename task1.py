# 任务1：统计书名长度超过30字符的记录数量 - 使用分号分隔符
# Задача 1: Подсчет количества записей с названиями длиннее 30 символов
count = 0

try:
    with open('books-en.csv', 'r', encoding='latin-1') as file:
        # 读取标题行（使用分号分隔）
        # Читаем заголовки (разделитель - точка с запятой)
        headers = file.readline().strip().split(';')
        
        print("Столбцы файла:")
        for i, header in enumerate(headers):
            print(f"  Столбец {i}: {header}")
        
        # 找到书名列的索引（应该是第1列，索引1）
        # Индекс столбца с названиями книг
        title_index = 1  # Book-Title列# Столбец Book-Title
        
        # 统计长书名
        # Подсчет длинных названий
        for line_num, line in enumerate(file, 2):
            fields = line.strip().split(';')  # 使用分号分隔
                                              # Используем точку с запятой как разделит
            if len(fields) > title_index and len(fields[title_index]) > 30:
                count += 1
                if count <= 3:  # 显示前3个长书名作为示例
                                # Показываем первые 3 длинных названия как пример
                    print(f"  Пример длинного названия: '{fields[title_index]}'")
    
    print(f"\nКоличество записей с названиями длиннее 30 символов: {count}")

except FileNotFoundError:
    print("Ошибка: Файл 'books-en.csv' не найден")
except Exception as e:
    print(f"Ошибка: {e}")