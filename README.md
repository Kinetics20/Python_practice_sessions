# Python Practice Sessions

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Notebook-7.3.1-orange?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![mypy](https://img.shields.io/badge/mypy-1.14.0-blueviolet?logo=mypy&logoColor=white)](http://mypy-lang.org/)
[![pytest](https://img.shields.io/badge/pytest-8.3.4-yellow?logo=pytest&logoColor=white)](https://pytest.org/)
[![Poetry](https://img.shields.io/badge/Poetry-1.x-65C2CB?logo=poetry&logoColor=white)](https://python-poetry.org/)
[![PyCharm](https://img.shields.io/badge/PyCharm-2024.3.1-blue?logo=jetbrains&logoColor=white)](https://www.jetbrains.com/pycharm/)

## About the Repository

This repository is dedicated to my Python programming practice. It contains programs written in both functional and object-oriented paradigms. I explore various techniques, including:  

- Static typing (`mypy`)  
- Unit testing (`pytest`)  
- Working with notebooks (`Jupyter Notebook`)  
- Managing dependencies using `Poetry`  

## Tools and Technologies

Below are the tools and technologies used in this repository along with their versions:  

| Tool               | Version | Link                                  |
|--------------------|---------|---------------------------------------|
| **Python**         | ^3.12   | [Python](https://www.python.org/)     |
| **Jupyter Notebook** | 7.3.1 | [Jupyter](https://jupyter.org/)       |
| **mypy**           | 1.14.0  | [mypy](https://mypy-lang.org/)        |
| **pytest**         | 8.3.4   | [pytest](https://pytest.org/)         |
| **Poetry**         | 1.x     | [Poetry](https://python-poetry.org/)  |

## Repository Structure

- **Functional Programming**  
  Programs written following the principles of functional programming.  
- **Object-Oriented Programming**  
  Projects based on object-oriented programming using classes and methods.  
- **Tests and Typing**  
  Contains unit tests and code with static typing.  
- **Jupyter Notebooks**  
  Interactive notebooks with experiments and analyses.  

## How to Run?

1. Install `pipx` (a recommended way to manage Python tools):  
   ```bash
   sudo apt install pipx
   pipx ensurepath

2. Install Poetry using pipx:
    ```bash
    pipx install poetry
    ```

3. Install Mypy using Poetry:
    ```bash
    poetry add mypy
    ```

4. Install Jupyter Notebook using Poetry:
    ```bash
    poetry add 'pytest==8.3.4'
    ```
5Install Pytest using Poetry:
    ```bash
    poetry add 'notebook==7.3.1'
    ```   

## Update all dependencies:
```bash
poetry update
```

## Using `pytest` and `mypy`

- **`pytest`** is a framework for writing and running tests to ensure your code works as expected. Run tests with:
- **`pytest`** is a testing framework for Python that allows you to write simple and scalable tests to ensure your code behaves as expected.
  ```bash
  poetry run pytest
  ```
  ```bash
  poetry run mypy script_name.py
  ```


## 🧑‍💻 Author

Piotr Lipiński

Feel free to contribute, submit issues, or ask questions! 😊

