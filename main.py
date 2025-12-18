from parser import YAMLParser
from serializer import serialize_to_hcl
from pprint import pprint


def print_header(title):
    print("=" * 60)
    print(title)
    print("=" * 60)


# ---------- ЧТЕНИЕ YAML ----------
with open("schedule.yaml", "r", encoding="utf-8") as file:
    lines = file.readlines()

# ---------- ПАРСИНГ ----------
parser = YAMLParser(lines)
расписание = parser.parse()

print_header("ЭТАП 1. ДЕСЕРИАЛИЗАЦИЯ YAML → ОБЪЕКТНАЯ МОДЕЛЬ")
pprint(расписание, width=100)

# ---------- СЕРИАЛИЗАЦИЯ В HCL ----------
hcl_text = serialize_to_hcl(расписание)

print_header("ЭТАП 2. СЕРИАЛИЗАЦИЯ ОБЪЕКТНОЙ МОДЕЛИ → HCL")
print(hcl_text)

# ---------- ЗАПИСЬ В ФАЙЛ ----------
with open("schedule.hcl", "w", encoding="utf-8") as file:
    file.write(hcl_text)

print("Файл schedule.hcl успешно создан.")
