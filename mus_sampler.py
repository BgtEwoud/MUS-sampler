# -*- coding: utf-8 -*-
"""
Monetary Unit Sampling (MUS) script.
Created on Fri Oct 25 12:16:23 2024
@author: Ewoud Bogaert
"""

import pandas as pd
import numpy as np

def load_data(file_path):
    """Load Excel data from the specified file path."""
    return pd.read_excel(file_path, sheet_name="input")

def get_sample_count():
    """Prompt user to input number of sample items, handle invalid inputs."""
    while True:
        try:
            return int(input("Enter the number of sample items you want: "))
        except ValueError:
            print("Please enter a valid integer.")

def calculate_cumulative_amount(df):
    """Add a cumulative sum column to DataFrame for sampling calculations."""
    df['CUMULATIVE_AMOUNT'] = df['AMOUNT'].cumsum()

def perform_mus_sampling(df, num_samples):
    """Perform MUS sampling and return updated DataFrame."""
    total_amount = df['AMOUNT'].sum()
    sampling_interval = total_amount / num_samples
    start_point = np.random.uniform(0, sampling_interval)
    sample_points = [start_point + i * sampling_interval for i in range(num_samples)]
    df['MUS_SELECT'] = "NO"

    for point in sample_points:
        sampled_index = df[df['CUMULATIVE_AMOUNT'] >= point].index[0]
        df.at[sampled_index, 'MUS_SELECT'] = "YES"
    
    return df

def main():
    """Main function to execute MUS sampling."""
    file_path = r"C:\Users\EwoudBogaert\OneDrive - Bogaert-Audit\3 - Automatisatie\044. MUS Sampler\Input.xlsx"
    df = load_data(file_path)
    num_samples = get_sample_count()
    calculate_cumulative_amount(df)
    df = perform_mus_sampling(df, num_samples)
    print("DataFrame with Monetary Unit Sampling selection:")
    print(df)

if __name__ == "__main__":
    main()
