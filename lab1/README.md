# ML Automation Pipeline

This project demonstrates a simple machine learning automation pipeline using Python and bash scripting. The pipeline covers data creation, preprocessing, model training, and model testing.

## Project Structure

- `data_creation.py`: Creates synthetic datasets with potential anomalies or noise, saving some for training (`train/`) and some for testing (`test/`).
- `model_preprocessing.py`: Preprocesses the data using `sklearn.preprocessing.StandardScaler`.
- `model_preparation.py`: Trains a machine learning model (linear regression) on the preprocessed training data.
- `model_testing.py`: Tests the trained model on the preprocessed testing data, providing evaluation metrics such as Mean Squared Error (MSE) and R^2 score.
- `pipeline.sh`: Bash script to run all the above Python scripts in sequence.

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Al-ta-iR/mlops_s2_hw1_automation_pipeline.git
    cd mlops_s2_hw1_automation_pipeline
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the pipeline:**
    ```bash
    ./pipeline.sh
    ```

   This script will sequentially run the following steps:
   - `data_creation.py`: Creates training and testing datasets.
   - `model_preprocessing.py`: Preprocesses the datasets.
   - `model_preparation.py`: Trains the model on the training data.
   - `model_testing.py`: Evaluates the model on the testing data.

## File Descriptions

- **data_creation.py**:
    - Generates synthetic datasets for training and testing.
    - Saves datasets in `train/` and `test/` directories.

- **model_preprocessing.py**:
    - Loads the datasets from `train/` and `test/` directories.
    - Applies `StandardScaler` to the datasets.
    - Saves the preprocessed datasets back to `train/` and `test/` directories.

- **model_preparation.py**:
    - Loads the preprocessed training data.
    - Trains a linear regression model.
    - Saves the trained model to the `model/` directory.

- **model_testing.py**:
    - Loads the preprocessed testing data and the trained model.
    - Evaluates the model using MSE and R^2 score.

- **pipeline.sh**:
    - Sequentially runs all the Python scripts to complete the machine learning pipeline.

## Notes

- Ensure that the `train/` and `test/` directories exist before running the pipeline.
- The project uses a linear regression model for simplicity, but you can replace it with any other model suitable for your use case.

## Contributing

Feel free to open issues or submit pull requests if you find any bugs or have suggestions for improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
