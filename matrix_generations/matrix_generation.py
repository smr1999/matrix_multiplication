import random
import math


class MatrixGeneration:
    def __init__(self, x_dimension: int, y_dimension: int, sparsity_ratio: float = 0.5) -> None:
        self.__x_dimension: int = x_dimension
        self.__y_dimension: int = y_dimension
        self.__sparsity_ratio: float = sparsity_ratio

        self.__result: list[list[float]] = []

    @property
    def result(self) -> list[list[float]]:
        return self.__result

    def __generate_list(self, num_items: int, fill_zero: bool = False) -> list[float]:
        result: list[float] = []

        if fill_zero:
            for _ in range(num_items):
                result.append(0.0)
        else:
            for _ in range(num_items):
                result.append(round(random.random() * 100, 2))

        return result

    def generate(self) -> None:
        for _ in range(self.__x_dimension):
            zero_items: list[float] = self.__generate_list(
                num_items=math.floor(
                    self.__sparsity_ratio * self.__y_dimension),
                fill_zero=True
            )
            non_zero_items: list[float] = self.__generate_list(
                num_items=(self.__y_dimension -
                           math.floor(self.__sparsity_ratio * self.__y_dimension))
            )

            row_items: list[float] = zero_items + non_zero_items
            random.shuffle(row_items)

            self.__result.append(row_items)
