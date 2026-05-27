# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, raz=","):
    spicok1 = group1.split(raz)
    spicok2 = group2.split(raz)

    spicok1_clean = [name.strip() for name in spicok1]
    spicok2_clean = [name.strip() for name in spicok2]

    common = set(spicok1_clean) & set(spicok2_clean)

    return sorted(common)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

participants_first_group_d = "Иванов | Петров | Сидоров"
participants_second_group_d = "Петров | Сидоров | Смирнов"

common_participants_d = find_common_participants(participants_first_group_d, participants_second_group_d, raz=" | ")

print("Общие участники (разделитель ' | '):", common_participants_d)
