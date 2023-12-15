from io import (
    TextIOWrapper,
)
import csv


class MatrixLogger:
    def __init__(self, x_dimension: int, y_dimension: int) -> None:
        self.__x_dimension: int = x_dimension
        self.__y_dimension: int = y_dimension

        self.__logger: list[list[list[str]]] = self.__initial_logger
        self.__counter: int = 0

    @property
    def __initial_logger(self) -> list[list[list[str]]]:
        assert self.__x_dimension > 0
        assert self.__y_dimension > 0

        logger: list[list[list[str]]] = []

        for row_index in range(self.__x_dimension):
            row_logger: list[list[str]] = []
            for column_index in range(self.__y_dimension):
                row_logger.append([])
            logger.append(row_logger)

        return logger

    def add_log(self, row_index: int, column_index: int, current_value: float) -> None:
        assert row_index >= 0 and row_index < self.__x_dimension
        assert column_index >= 0 and column_index < self.__y_dimension

        self.__logger[row_index][column_index].append(
            f'{self.__counter}({current_value})'
        )
        self.__counter += 1

    def write_to_file(self, output_object: TextIOWrapper) -> None:
        csv_object = csv.writer(
            output_object,
            lineterminator='\n'
        )

        for row_index in range(self.__x_dimension):
            row_values: list[str] = []
            for column_index in range(self.__y_dimension):
                row_values.append(
                    '->'.join(self.__logger[row_index][column_index]))
            csv_object.writerow(row_values)
