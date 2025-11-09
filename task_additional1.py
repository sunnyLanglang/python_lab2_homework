# 附加任务1：获取不重复的出版商列表 - 使用分号分隔符
# Дополнительная задача 1: Получение списка уникальных издательств
try:
    with open('books-en.csv', 'r', encoding='latin-1') as file:
        headers = file.readline().strip().split(';')  # 使用分号分隔
                                                      # Разделитель - точка с запятой
        print("文件列名:")
        for i, header in enumerate(headers):
            print(f"  列 {i}: {header}")
        
        # 根据列名设置索引
        # Индекс столбца издательств
        publisher_index = 4  # Publisher列# Столбец Publisher
        
        publishers = set()
        for line in file:
            fields = line.strip().split(';')  # 使用分号分隔# Используем точку с запятой как разделитель
            if len(fields) > publisher_index and fields[publisher_index].strip():
                publishers.add(fields[publisher_index].strip())
        
        unique_publishers = sorted(list(publishers))
        
        print(f"\nКоличество уникальных издательств: {len(unique_publishers)}")
        print("\nПервые 20 издательств:")
        for i, publisher in enumerate(unique_publishers[:20], 1):
            print(f"  {i}. {publisher}")
        if len(unique_publishers) > 20:
            print(f"  ... и еще {len(unique_publishers) - 20}")

except FileNotFoundError:
    print("Ошибка: Файл 'books-en.csv' не найден")
except Exception as e:
    print(f"Ошибка: {e}")