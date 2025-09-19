from event import *
from itertools import cycle
import copy
import sys


class Main:
    start_date: Date = None
    end_date: Date = None
    num_weeks: int = None
    persons: list = None
    events: list = []

    def __init__(self, start_date: Date, num_weeks: int, persons: list) -> None:
        self.start_date = start_date
        self.end_date = copy.deepcopy(start_date)
        self.end_date.add_days(7)
        self.num_weeks = num_weeks
        self.persons = persons

    def __generate_events(self) -> None:
        person_iterator = cycle(self.persons)
        activities = cycle(
            [
                TaskList.dishes,
                TaskList.dishes,
                TaskList.floor,
                TaskList.hygiene_places,
                TaskList.vacuuming,
            ]
        )
        for week in range(self.num_weeks):
            # self.events.append(Event(copy.deepcopy(self.start_date), copy.deepcopy(self.end_date), TaskList.dishes, next(person_iterator)))
            # self.events.append(Event(copy.deepcopy(self.start_date), copy.deepcopy(self.end_date), TaskList.dishes, next(person_iterator)))
            # self.events.append(Event(copy.deepcopy(self.start_date), copy.deepcopy(self.end_date), TaskList.floor, next(person_iterator)))
            # self.events.append(Event(copy.deepcopy(self.start_date), copy.deepcopy(self.end_date), TaskList.hygiene_places, next(person_iterator)))
            # self.events.append(Event(copy.deepcopy(self.start_date), copy.deepcopy(self.end_date), TaskList.vacuuming, next(person_iterator)))
            for _ in range(len(self.persons)):
                self.events.append(
                    Event(
                        copy.deepcopy(self.start_date),
                        copy.deepcopy(self.end_date),
                        next(activities),
                        next(person_iterator),
                    )
                )

            if len(self.persons) == 5:
                next(activities)

            self.start_date.add_days(7)
            self.end_date.add_days(7)

    def make_output(self) -> None:
        self.__generate_events()

        with open("calendar_data.csv", "w", newline="", encoding="utf-8") as csvfile:
            headers = (
                "Subject",
                "Start Date",
                "Start Time",
                "End Date",
                "End Time",
                "All day event",
                "Description",
            )
            writer = csv.DictWriter(csvfile, fieldnames=headers, delimiter=",")
            writer.writeheader()
            for event in self.events:
                event.write_to_csv(writer)


def main():
    persons = ["Maka", "Feela", "Radim", "Monty", "Anička"]
    start_date = Date(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    num_weeks = int(int(sys.argv[4]))
    main = Main(start_date, num_weeks, persons)
    main.make_output()


if __name__ == "__main__":
    main()
