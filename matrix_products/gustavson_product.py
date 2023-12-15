from matrix_loggers.matrix_logger import (
    MatrixLogger,
)
from matrix_products.product import (
    Product,
)


class GustavsonProduct(Product):
    def __init__(self, first_matrix: list[list[float]], second_matrix: list[list[float]], matrix_logger: MatrixLogger = None) -> None:
        super().__init__(first_matrix, second_matrix, matrix_logger)

    def calculate(self) -> None:
        for m in range(len(self.first_matrix)):  # 0 to (M-1)
            for k in range(len(self.first_matrix[0])):  # 0 to (K-1)
                for n in range(len(self.second_matrix[0])):  # 0 to (N-1)
                    self.result[m][n] += \
                        self.first_matrix[m][k] * self.second_matrix[k][n]

                    self.number_of_operations += 1

                    self.check_new_access(
                        new_first_matrix_index_access=(m, k),
                        new_second_matrix_index_access=(k, n),
                        new_result_matrix_index_access=(m, n)
                    )

                    if self.matrix_logger:
                        self.matrix_logger.add_log(
                            row_index=m,
                            column_index=n,
                            current_value=self.result[m][n]
                        )
