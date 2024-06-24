from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Context:
    """
    Контекст определяет интерфейс, представляющий интерес для клиентов.
    """

    def __init__(self, strategy: Strategy, current_rating, new_point) -> None:
        self._strategy = strategy
        self._current_rating = current_rating
        self._new_point = new_point

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def rating(self) -> None:
        result = self._strategy.do_algorithm(self._current_rating, self._new_point)


class Strategy(ABC):
    """
    Интерфейс Стратегии объявляет операции, общие для всех поддерживаемых версий
    некоторого алгоритма.

    Контекст использует этот интерфейс для вызова алгоритма, определённого
    Конкретными Стратегиями.
    """

    @abstractmethod
    def do_algorithm(self, current_rating, new_point):
        pass


class StrategyUser(Strategy):

    def do_algorithm(self, current_rating, new_point):
        current_rating += new_point*0.1
        current_rating %= 5
        return


class StrategyProgrammers(Strategy):
    def do_algorithm(self, current_rating, new_point):
        current_rating += new_point * 0.3
        current_rating %= 5
        return

