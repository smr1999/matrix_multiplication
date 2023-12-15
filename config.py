class Config:
    """
    Matrix dimensions
    """
    M: int = 6
    K: int = 10
    N: int = 20

    """
    Sparsity ratio
    """
    first_matrix_sparsity_ratio: float = 0.7
    second_matrix_sparsity_ratio: float = 0.9

    """
    Logger file names
    """
    inner_product_log_file: str = 'inner_product_log'
    outer_product_log_file: str = 'outer_product_log'
    gustavson_product_log_file: str = 'gustavson_product_log'
