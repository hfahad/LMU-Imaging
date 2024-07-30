# LMU-Imaging

# ESRF Jupyter-Slurm Setup Guide

## Overview
At ESRF Jupyter-Slurm, installing libraries directly into the environment can be challenging due to restrictions. However, you can bypass these limitations by creating a virtual environment and connecting it to Jupyter-Slurm. This guide will walk you through the necessary steps to set up and configure your virtual environment for seamless integration.

## Prerequisites
- Ensure you have Python 3 installed on your system.
- Access to ESRF Jupyter-Slurm.

## Setup Instructions

### Step 1: Create a Virtual Environment
To create a virtual environment, use the following command:

```Terminal
python3 -m venv your_venv_name
```

Replace `your_venv_name` with a name of your choice for the virtual environment.

### Step 2: Activate the Virtual Environment
Activate your newly created virtual environment. The activation command varies depending on your operating system:

- **Linux:**
  ```Terminal
  source path_of_your_venv/your_venv_name/bin/activate
  ```


### Step 3: Install Required Libraries
Once the virtual environment is activated, you can install the required libraries using `pip`. For example:

```Terminal
pip3 install numpy pandas matplotlib
```

### Step 4: Connect the Virtual Environment to Jupyter-Slurm
After installing the necessary libraries, you need to connect your virtual environment to Jupyter-Slurm. This is done by installing the `ipykernel` package and creating a new kernel:

```Terminal
pip install ipykernel
python -m ipykernel install --user --name your_venv_name
```

Replace `your_venv_name` with the name you chose for your virtual environment.

### Step 5: Select the New Kernel in Jupyter
- Open Jupyter Notebook through Jupyter-Slurm.
- Go to the "Kernel" menu and select "Change kernel".
- Choose the kernel named "your_venv_name" that you created in the previous step.

## Conclusion
By following these steps, you can successfully create a virtual environment and connect it to Jupyter-Slurm, allowing you to install and use the required libraries without any restrictions. This setup ensures a flexible and efficient working environment for your projects at ESRF.

## Support
If you encounter any issues or need further assistance, please feel free to open an issue on this repository.
