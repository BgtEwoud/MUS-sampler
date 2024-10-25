# Monetary Unit Sampling (MUS) Sampler

This project implements a Monetary Unit Sampling (MUS) method using a graphical user interface (GUI). The application allows users to select an Excel file containing monetary values and specify the number of samples they want to generate. The results are then saved to a new Excel file.

## Features

- **File Selection**: Browse and select an input Excel file containing monetary amounts.
- **Sample Count Input**: Specify the number of sample items to generate.
- **MUS Sampling**: Perform Monetary Unit Sampling on the selected data.
- **Output**: Save the resulting DataFrame to a new Excel file with `-MUS Sampling` appended to the original filename.
- **Exit Gracefully**: The application can be closed via the "Exit" button or by using the window's close button.

## Requirements

- Python 3.x
- Pandas
- NumPy
- Tkinter (included with standard Python installations)
- OpenPyXL (for reading and writing Excel files)

You can install the required packages using pip:

```bash
pip install pandas numpy openpyxl
Usage
Clone the Repository (if applicable):

bash
Code kopiëren
git clone <repository_url>
cd <repository_directory>
Run the Application: Ensure you have Python installed and the necessary packages. Execute the following command:

bash
Code kopiëren
python mus_sampler.py
Using the GUI:

Click on the "Browse" button to select your input Excel file (ensure it contains a sheet named input with a column labeled AMOUNT).
Enter the desired number of sample items in the provided input box.
Click "Run MUS Sampling" to generate the samples.
The results will be saved in a new Excel file in the same directory as the input file, with -MUS Sampling appended to the filename.
Click "Exit" to close the application.
Example Input
The input Excel file should have a sheet named input with at least the following column:

AMOUNT
100.00
150.50
200.00
...
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Author
Ewoud Bogaert
