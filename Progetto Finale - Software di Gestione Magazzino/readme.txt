This is a software to manage a vegan product shop.
Provided functionalities are:
1. add a new product in warehouse
2. list all products in warehouse
3. record all sales
4. display gross and net earnings from sales

PS the program language is italian.

To execute the program, follow these steps:
Inside project directory, create a python virtual environment with venv module:
  python -m venv myenv
Activate the virtual environment (it depends on which OS you're working on).
Download and install all required packages and modules with
  pip install -r requirements.txt
Create a kernel inside virtual env with
  python -m ipykernel install --user --name=myenv_kernel
Open "main.ipynb" with Jupyter notebook, with new kernel.
Run the two code blocks below and follow terminal instructions.

During execution two csv files will be created in the main project directory (warehouse.csv and sales.csv). Don't delete them in order to keep operations' persistence.