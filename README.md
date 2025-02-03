# chem_scripts

# Molecule Intersections Finder

This project reads a CSV file containing molecule data with start and finish times and finds molecule intersections over time.

## Table of Contents
- [Installation Guide](#installation-guide)
- [Running the Script](#running-the-script)
- [Expected Input](#expected-input)
- [Expected Output](#expected-output)
- [Troubleshooting](#troubleshooting)
- [Acknowledgments](#acknowledgments)

---

## Installation Guide

### 1. Install Python

#### Windows
1. Go to the [Python Download Page](https://www.python.org/downloads/).
2. Download the latest version of Python for Windows.
3. Run the installer.
4. **Important:** Select the checkbox "Add Python to PATH" during installation.

### 2. Clone or Download the Project
1. Open your terminal (or command prompt on Windows).
2. Navigate to a directory where you want the project:
   ```bash
   cd ~/path-to-your-directory
   ```
3. Clone the project from GitHub:
   ```bash
   git clone git@github.com:dvdmakeev/chem_scripts.git
   ```
   Alternatively, download the ZIP file from GitHub and extract it.

### 3. Create a Virtual Environment (Recommended)
This keeps dependencies isolated:
```bash
python -m venv venv
```

### 4. Activate the Virtual Environment
- **Windows:**
  ```cmd
  .\venv\Scripts\activate
  ```
  
### 5. Install Dependencies
Install the required packages:
```bash
pip install -r requirements.txt
```

## Running the Script

1. Prepare your CSV input file.
2. In the terminal, run the script as follows:
   ```bash
   python src/find_molecul_intersections.py <input_file_name.csv> <output_file_name.csv>
   ```
   Example:
   ```bash
   python src/find_molecul_intersections.py data/input.csv results/output.csv
   ```

## Input File Format

The input file must be a CSV with the following format:

```csv
Molecule, Start, Finish
TAG 15:0-15:0-15:0, 17.9, 18.9
TAG 17:0-17:0-17:0, 22.5, 23.5
TAG 16:0-16:0-18:1, 20.2, 21.2
```

## Expected Output
The output CSV will contain:
- Time intervals when molecule intersections occur.
- Number of active molecules.
- List of molecules at each interval.

Example:
```csv
17.9, 1, TAG 15:0-15:0-15:0
18.0, 2, TAG 15:0-15:0-15:0;TAG 16:0-16:0-18:3
19.0, 3, TAG 16:0-16:0-18:3;TAG 16:0-16:0-18:2;TAG 15:0-15:0-15:0
```

