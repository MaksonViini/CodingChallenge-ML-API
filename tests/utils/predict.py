import random

from src.app.schemas.ml_model import Input


def create_random_data_to_predict():
    input_data = {
        "sample_code_number": random.randrange(63375, 13454352),
        "clump_thickness": random.randrange(1, 10),
        "uniformity_of_cell_size": random.randrange(1, 10),
        "uniformity_of_cell_shape": random.randrange(1, 10),
        "marginal_adhesion": random.randrange(1, 10),
        "single_epithelial_cell_size": random.randrange(1, 10),
        "bare_nuclei": random.randrange(1.0, 10.0),
        "bland_chromatin": random.randrange(1, 10),
        "normal_nucleoli": random.randrange(1, 10),
        "mitoses": random.randrange(1, 10),
    }

    data = Input(**input_data)
    assert data is not None
    return data
