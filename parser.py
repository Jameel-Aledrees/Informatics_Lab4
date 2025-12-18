class YAMLParser:
    def __init__(self, lines):
        self.lines = [line.rstrip() for line in lines if line.strip()]
        self.index = 0

    def parse(self):
        расписание = {}

        while self.index < len(self.lines):
            line = self.lines[self.index]

            if line.startswith("день:"):
                расписание["день"] = self._parse_value(line)
                self.index += 1

            elif line.startswith("занятия:"):
                self.index += 1
                расписание["занятия"] = self._parse_classes()

            else:
                self.index += 1

        return расписание

    def _parse_classes(self):
        занятия = []

        while self.index < len(self.lines):
            line = self.lines[self.index]

            if line.strip().startswith("-"):
                занятия.append(self._parse_class())
            else:
                break

        return занятия

    def _parse_class(self):
        занятие = {}

        line = self.lines[self.index].strip()

        # случай: "- ключ: значение"
        if line.startswith("-"):
            content = line[1:].strip()
            if content:
                key, value = self._split_key_value(content)
                занятие[key] = value.strip('"')
            self.index += 1

        while self.index < len(self.lines):
            line = self.lines[self.index]

            if line.strip().startswith("-"):
                break

            if ":" in line:
                key, value = self._split_key_value(line)

                if key == "время":
                    self.index += 1
                    занятие["время"] = self._parse_time()
                    continue

                if key == "недели":
                    занятие[key] = self._parse_list(value)
                else:
                    занятие[key] = value.strip('"')

            self.index += 1

        return занятие

    def _parse_time(self):
        время = {}

        for _ in range(2):
            line = self.lines[self.index]
            key, value = self._split_key_value(line)
            время[key] = value.strip('"')
            self.index += 1

        return время

    def _parse_list(self, value):
        numbers = value.strip("[]").split(",")
        return [int(n.strip()) for n in numbers]

    def _split_key_value(self, line):
        key, value = line.strip().split(":", 1)
        return key, value.strip()

    def _parse_value(self, line):
        return line.split(":", 1)[1].strip()
