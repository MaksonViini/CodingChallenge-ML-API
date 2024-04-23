import joblib
import os

global model_path, sc_path

current_file_dir = os.path.dirname(os.path.realpath(__file__))
model_path = os.path.join(current_file_dir, "serialized_models", "v1", "model.joblib")
sc_path = os.path.join(current_file_dir, "serialized_models", "v1", "sc.joblib")


def load_model():
    """
    Load a model from a specified path using joblib.

    Returns:
    - model: Loaded model object.
    """
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"The specified path '{model_path}' does not exist.")

    try:
        model = joblib.load(model_path)
        print(f"Model loaded from {model_path}")
        return model
    except Exception as e:
        print(f"An error occurred while loading the model from {model_path}: {e}")
        return None


def load_scaler():
    """
    Load a scaler from a specified path using joblib.

    Returns:
    - scaler: Loaded scaler object.
    """
    if not os.path.exists(sc_path):
        raise FileNotFoundError(f"The specified path '{sc_path}' does not exist.")

    try:
        model = joblib.load(sc_path)
        print(f"Scaler loaded from {sc_path}")
        return model
    except Exception as e:
        print(f"An error occurred while loading the scaler from {sc_path}: {e}")
        return None
