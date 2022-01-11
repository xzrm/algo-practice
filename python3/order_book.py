from dataclasses import dataclass, field
from typing import List, Tuple
from itertools import count


@dataclass
class Task:
    description: str
    programmer: str
    workload: int
    finished: bool = False
    __id: int = field(default_factory=count(1).__next__, init=True)

    @property
    def id(self):
        return self.__id

    def mark_finished(self) -> None:
        self.finished = not self.finished

    def is_finished(self) -> bool:
        return self.finished

    def __str__(self) -> str:
        status = "FINISHED" if self.finished else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"


class OrderBook:
    def __init__(self):
        self.__orders: List[Task] = []

    def add_order(self, description: str, programmer: str, workload: int) -> None:
        self.__orders.append(Task(description, programmer, workload))

    def all_orders(self):
        return self.__orders

    def mark_finished(self, id: int) -> None:
        for t in self.__orders:
            if t.id == id:
                t.mark_finished()
                return None
        else:
            raise ValueError

    def finished_orders(self) -> List[Task]:
        return [i for i in self.all_orders() if i.is_finished() == True]

    def unfinished_orders(self) -> List[Task]:
        return [i for i in self.all_orders() if i.is_finished() == False]

    def programmers(self) -> List[str]:
        return list(set([i.programmer for i in self.__orders]))

    def status_of_programmer(self, programmer: str) -> Tuple[int, int, int, int]:
        programmer_tasks = list(
            filter(lambda x: x.programmer == programmer, self.__orders)
        )
        finished_tasks = [i for i in programmer_tasks if i.is_finished()]
        unfinished_tasks = [i for i in programmer_tasks if not i.is_finished()]
        return (
            len(finished_tasks),
            len(unfinished_tasks),
            sum([i.workload for i in finished_tasks]),
            sum([i.workload for i in unfinished_tasks]),
        )


orders = OrderBook()
orders.add_order("program webstore", "Adele", 10)
orders.add_order("program mobile app for workload accounting", "Adele", 25)
orders.add_order("program app for practising mathematics", "Adele", 100)
orders.add_order("program the next facebook", "Eric", 1000)

orders.mark_finished(1)
orders.mark_finished(2)

status = orders.status_of_programmer("Adele")
print(status)
