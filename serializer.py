def serialize_to_hcl(расписание):
    lines = []
    lines.append(f'день = "{расписание["день"]}"\n\n')

    for i, занятие in enumerate(расписание["занятия"], start=1):
        lines.append(f'занятие "{i}" {{\n')
        lines.append(f'  предмет = "{занятие["предмет"]}"\n')
        lines.append(f'  тип = "{занятие["тип"]}"\n')
        lines.append(f'  начало = "{занятие["время"]["начало"]}"\n')
        lines.append(f'  конец = "{занятие["время"]["конец"]}"\n')
        lines.append(f'  недели = {занятие["недели"]}\n')
        lines.append(f'  группа = "{занятие["группа"]}"\n')
        lines.append(f'  аудитория = "{занятие["аудитория"]}"\n')
        lines.append(f'  корпус = "{занятие["корпус"]}"\n')
        lines.append(f'  тип_аудитории = "{занятие["тип_аудитории"]}"\n')
        lines.append(f'  формат = "{занятие["формат"]}"\n')
        lines.append("}\n\n")

    return "".join(lines)
