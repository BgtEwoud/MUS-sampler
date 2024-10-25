# Monetary Unit Sampling (MUS) Sampler

This repository contains a Python script to perform Monetary Unit Sampling (MUS) on a dataset. MUS is commonly used in audit and accounting practices for selecting sample items based on monetary values. 

## Features
- Reads data from an Excel file
- Randomly selects sample items using MUS
- Prompts the user for the number of desired sample items
- Adds a `MUS_SELECT` column to identify the selected sample items

## Getting Started

### Prerequisites
- Python 3.x
- The following Python libraries:
  - `pandas`
  - `numpy`

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/MUS_Sampler.git
    cd MUS_Sampler
    ```

2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure you have an input Excel file located at:
    ```
    C:\Users\EwoudBogaert\OneDrive - Bogaert-Audit\3 - Automatisatie\044. MUS Sampler\Input.xlsx
    ```
    or modify the file path in the `mus_sampler.py` script.

### Usage

1. Run the script by executing:
    ```bash
    python mus_sampler.py
    ```

2. You will be prompted to enter the number of sample items:
    ```plaintext
    Enter the number of sample items you want:
    ```

3. The output will display the DataFrame with an additional `MUS_SELECT` column, indicating the sampled items.

### Example Output
An example DataFrame output with the `MUS_SELECT` column would look like:
| Index | AMOUNT | CUMULATIVE_AMOUNT | MUS_SELECT |
|-------|--------|-------------------|------------|
| 0     | 100.5  | 100.5            | NO         |
| 1     | 200.0  | 300.5            | YES        |
| ...   | ...    | ...               | ...        |

### License
This project is licensed under the MIT License.

### Author
Ewoud Bogaert
