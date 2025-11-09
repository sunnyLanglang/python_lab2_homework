import xml.etree.ElementTree as ET

# 任务4：解析currency.xml，提取NumCode和CharCode
# Задача 4: Парсинг currency.xml, извлечение NumCode и CharCode
try:
    tree = ET.parse('currency.xml')
    root = tree.getroot()
    
    num_codes = []
    char_codes = []
    
    # 查找所有Valute元素
    # Поиск всех элементов Valute
    for valute in root.findall('.//Valute'):
        num_code_elem = valute.find('NumCode')
        char_code_elem = valute.find('CharCode')
        
        if num_code_elem is not None and num_code_elem.text:
            num_codes.append(num_code_elem.text)
        
        if char_code_elem is not None and char_code_elem.text:
            char_codes.append(char_code_elem.text)
    
    print(f"Извлеченный список NumCode ({len(num_codes)} элементов):")
    for i, code in enumerate(num_codes, 1):
        print(f"  {i}. {code}")
    
    print(f"\nИзвлеченный список CharCode ({len(char_codes)} элементов):")
    for i, code in enumerate(char_codes, 1):
        print(f"  {i}. {code}")

except FileNotFoundError:
    print("Ошибка: Файл 'currency.xml' не найден")
except Exception as e:
    print(f"Ошибка: {e}")