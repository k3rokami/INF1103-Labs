from abc import ABC, abstractmethod

#Using Abstract class
class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total: float) -> float:
        pass

#When there's no discount
class NoDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total

#The % of dicount to use
class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float) -> None:
        self.percentage = percentage

    def apply(self, total: float) -> float:
        return total * (1 - self.percentage / 100)


class BulkDiscount(DiscountStrategy):
    def __init__(self, threshold: float, amount: float) -> None:
        self.threshold = threshold
        self.amount = amount

    def apply(self, total: float) -> float:
        if total >= self.threshold:
            return total - self.amount
        return total


class StudentDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total * 0.95
