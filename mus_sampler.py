# -*- coding: utf-8 -*-
"""
Monetary Unit Sampling (MUS) script with a GUI.
Created on Fri Oct 25 12:16:23 2024
@author: Ewoud Bogaert
"""

import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import sys  # Importing sys to exit the program


class MUSSamplerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Monetary Unit Sampling (MUS) Sampler")
        self.root.geometry("400x300")

        # Input file selection
        self.file_path = ""
        self.label_file = tk.Label(root, text="Select Input Excel File:")
        self.label_file.pack(pady=10)

        self.entry_file = tk.Entry(root, width=40)
        self.entry_file.pack(pady=5)

        self.button_browse = tk.Button(root, text="Browse", command=self.browse_file)
        self.button_browse.pack(pady=5)

        # Sample count input
        self.label_samples = tk.Label(root, text="Enter number of sample items:")
        self.label_samples.pack(pady=10)

        self.entry_samples = tk.Entry(root, width=10)
        self.entry_samples.pack(pady=5)

        # Submit button
        self.button_submit = tk.Button(root, text="Run MUS Sampling", command=self.run_sampling)
        self.button_submit.pack(pady=20)

        # Exit button
        self.button_exit = tk.Button(root, text="Exit", command=self.exit_app)
        self.button_exit.pack(pady=5)

        # Status label
        self.label_status = tk.Label(root, text="", fg="green")
        self.label_status.pack(pady=10)

        # Bind the window close event to exit the application
        self.root.protocol("WM_DELETE_WINDOW", self.exit_app)

    def browse_file(self):
        """Open a file dialog to select an Excel file."""
        self.file_path = filedialog.askopenfilename(
            title="Select the Input Excel File",
            filetypes=[("Excel files", "*.xlsx *.xls")]
        )
        self.entry_file.delete(0, tk.END)
        self.entry_file.insert(0, self.file_path)

    def load_data(self):
        """Load Excel data from the specified file path."""
        return pd.read_excel(self.file_path)

    def get_sample_count(self):
        """Get number of samples from user input."""
        try:
            return int(self.entry_samples.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid integer for sample count.")
            return None

    def calculate_cumulative_amount(self, df):
        """Add a cumulative sum column to DataFrame for sampling calculations."""
        df['CUMULATIVE_AMOUNT'] = df['AMOUNT'].cumsum()

    def perform_mus_sampling(self, df, num_samples):
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

    def save_results(self, df):
        """Save the resulting DataFrame to an Excel file with '-MUS Sampling' suffix."""
        base_name = os.path.basename(self.file_path)
        file_name, file_extension = os.path.splitext(base_name)
        output_file = os.path.join(os.path.dirname(self.file_path), f"{file_name}-MUS Sampling{file_extension}")
        df.to_excel(output_file, index=False)
        return output_file

    def run_sampling(self):
        """Run the MUS sampling process."""
        if not self.file_path:
            messagebox.showerror("File Error", "Please select an input Excel file.")
            return

        num_samples = self.get_sample_count()
        if num_samples is None:
            return

        # Load data from the selected file
        df = self.load_data()

        # Perform MUS sampling
        self.calculate_cumulative_amount(df)
        df = self.perform_mus_sampling(df, num_samples)

        # Save the resulting DataFrame to a new Excel file
        output_file = self.save_results(df)

        # Output the DataFrame with selected samples
        print("DataFrame with Monetary Unit Sampling selection saved to:")
        print(output_file)

        # Update status
        self.label_status.config(text=f"Sampling completed. Results saved to: {output_file}")

    def exit_app(self):
        """Exit the application."""
        self.root.destroy()  # Close the Tkinter window
        sys.exit()  # Exit the program


def main():
    """Main function to start the MUS sampler GUI application."""
    root = tk.Tk()
    app = MUSSamplerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
