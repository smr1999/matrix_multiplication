from matrix_generations import *
from matrix_products import *
from matrix_loggers import *
from utils.file_util import (
    FileUtil,
)
from config import (
    Config,
)


class Main:
    def __init__(self) -> None:
        self.__initalize_objects()
        self.__calculate()
        self.__write_results()

    def __initalize_objects(self) -> None:
        self.matrix_first: MatrixGeneration = MatrixGeneration(
            x_dimension=Config.M,
            y_dimension=Config.K,
            sparsity_ratio=Config.first_matrix_sparsity_ratio
        )
        self.matrix_second: MatrixGeneration = MatrixGeneration(
            x_dimension=Config.K,
            y_dimension=Config.N,
            sparsity_ratio=Config.second_matrix_sparsity_ratio
        )

        self.matrix_first.generate()
        self.matrix_second.generate()

        self.inner_product_logger: MatrixLogger = MatrixLogger(
            x_dimension=Config.M,
            y_dimension=Config.N
        )
        self.outer_product_logger: MatrixLogger = MatrixLogger(
            x_dimension=Config.M,
            y_dimension=Config.N
        )
        self.gustavson_product_logger: MatrixLogger = MatrixLogger(
            x_dimension=Config.M,
            y_dimension=Config.N
        )

        self.inner_product: InnerProduct = InnerProduct(
            first_matrix=self.matrix_first.result,
            second_matrix=self.matrix_second.result,
            matrix_logger=self.inner_product_logger
        )
        self.outer_product: OuterProduct = OuterProduct(
            first_matrix=self.matrix_first.result,
            second_matrix=self.matrix_second.result,
            matrix_logger=self.outer_product_logger
        )
        self.gustavson_product: GustavsonProduct = GustavsonProduct(
            first_matrix=self.matrix_first.result,
            second_matrix=self.matrix_second.result,
            matrix_logger=self.gustavson_product_logger
        )

    def __calculate(self) -> None:
        self.inner_product.calculate()
        self.outer_product.calculate()
        self.gustavson_product.calculate()

    def __write_results(self) -> None:
        self.inner_product_logger.write_to_file(
            FileUtil.write_file(
                file_name=f'result_files/{Config.inner_product_log_file}.csv'
            )
        )
        self.outer_product_logger.write_to_file(
            FileUtil.write_file(
                file_name=f'result_files/{Config.outer_product_log_file}.csv'
            )
        )
        self.gustavson_product_logger.write_to_file(
            FileUtil.write_file(
                file_name=f'result_files/{Config.gustavson_product_log_file}.csv'
            )
        )


if __name__ == '__main__':
    Main()
