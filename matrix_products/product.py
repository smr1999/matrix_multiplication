from matrix_loggers.matrix_logger import (
    MatrixLogger,
)


class Product:
    def __init__(self, first_matrix: list[list[float]], second_matrix: list[list[float]], matrix_logger: MatrixLogger = None) -> None:
        self.__first_matrix: list[list[float]] = first_matrix
        self.__second_matrix: list[list[float]] = second_matrix
        self.__result: list[list[float]] = self.__initial_result
        self.__matrix_logger: MatrixLogger = matrix_logger

        self.number_of_operations: int = 0
        self.number_of_memory_access: int = 0

        self.previous_first_matrix_index_access: tuple[int, int] = (-1, -1)
        self.previous_second_matrix_index_access: tuple[int, int] = (-1, -1)
        self.previous_result_matrix_index_access: tuple[int, int] = (-1, -1)

    @property
    def first_matrix(self) -> list[list[float]]:
        return self.__first_matrix

    @property
    def second_matrix(self) -> list[list[float]]:
        return self.__second_matrix

    @property
    def result(self) -> list[list[float]]:
        return self.__result

    @property
    def matrix_logger(self) -> MatrixLogger:
        return self.__matrix_logger

    def __check_dimensions(self) -> None:
        for row in self.__first_matrix:
            assert len(row) == len(self.__second_matrix)

    @property
    def __initial_result(self) -> list[list[float]]:
        self.__check_dimensions()

        result_dimensions: tuple(int, int) = \
            len(self.__first_matrix), len(self.__second_matrix[0])

        result: list[list[float]] = []

        for row_index in range(result_dimensions[0]):
            row_values: list[float] = []
            for column_index in range(result_dimensions[1]):
                row_values.append(0.0)
            result.append(row_values)

        return result

    def check_new_access(self, new_first_matrix_index_access: tuple[int, int], new_second_matrix_index_access: tuple[int, int], new_result_matrix_index_access: tuple[int, int]):
        if new_first_matrix_index_access != self.previous_first_matrix_index_access:
            self.number_of_memory_access += 1
            self.previous_first_matrix_index_access = new_first_matrix_index_access

        if new_second_matrix_index_access != self.previous_second_matrix_index_access:
            self.number_of_memory_access += 1
            self.previous_second_matrix_index_access = new_second_matrix_index_access

        if new_result_matrix_index_access != self.previous_result_matrix_index_access:
            self.number_of_memory_access += 1
            self.previous_result_matrix_index_access = new_result_matrix_index_access

    def calculate(self) -> list[list[float]]:
        # different from each multiplication
        pass
