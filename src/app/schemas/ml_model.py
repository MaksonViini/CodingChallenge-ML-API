from pydantic import BaseModel


class Input(BaseModel):
    """Input data class for the ML model."""

    sample_code_number: int
    clump_thickness: int
    uniformity_of_cell_size: int
    uniformity_of_cell_shape: int
    marginal_adhesion: int
    single_epithelial_cell_size: int
    bare_nuclei: float | int
    bland_chromatin: int
    normal_nucleoli: int
    mitoses: int


class Output(BaseModel):
    """Output data class for the ML model."""

    Predicted: int
