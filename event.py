import csv


class Date:
    year: int = None
    month: int = None
    day: int = None

    def __init__(self, day: int, month: int, year: int) -> None:
        self.year = year
        self.month = month
        self.day = day

    def __str__(self) -> str:
        return f"{self.day}/{str(self.month).zfill(2)}/{self.year}"

    def add_days(self, days: int) -> None:
        if self.month in (1, 3, 5, 7, 8, 10, 12):
            if self.day + days > 31:
                self.day = (self.day + days) % 31
                self.month += 1
            else:
                self.day += days
        elif self.month in (4, 6, 9, 11):
            if self.day + days > 30:
                self.day = (self.day + days) % 30
                self.month += 1
            else:
                self.day += days
        else:
            if self.day + days > 28:
                self.day = (self.day + days) % 28
                self.month += 1
            else:
                self.day += days


class Task:
    name: str = None
    description: str = None

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description


class TaskList:
    dishes: Task = Task(
        "Kuchyň", "Každý večer si udělá čas na zkontrolování kuchyně a bude-li potřeba, tak upozorní autory nepořádku, aby po sobě uklidili. Na konci týdne udělá větší čistění linky, stolu a okolí, než se začne uklízet podlaha.")
    floor: Task = Task(
        "Podlaha", "Na konci týdne, než odjede domů si udělá čas na to, aby umyl podlahu.")
    hygiene_places: Task = Task(
        "Záchod + koupelna", "Na konci týdne, než odjede domů si udělá čas na to, aby zkontroloval stav koupelny a záchodu a uzná-li za vhodné, tak vyčistí co je potřeba.")
    vacuuming: Task = Task(
        "Luxování", "Na konci týdne, než odjede domů si udělá čas na to, aby vyluxoval.")


class Event:
    start_date: Date = None
    end_date: Date = None
    task: Task = None
    person: str = None

    def __init__(self, start_date: Date, end_date: Date, task: Task, person: str) -> None:
        self.start_date = start_date
        self.end_date = end_date
        self.task = task
        self.person = person

    def __generate_row(self) -> dict:
        return {
            "Subject": f'{self.person.upper()} - {self.task.name}',
            "Start Date": str(self.start_date),
            "Start Time": '',
            "End Date": str(self.end_date),
            "End Time": '',
            "All day event": 'TRUE',
        }

    def write_to_csv(self, file: csv.DictWriter) -> None:
        file.writerow(self.__generate_row())