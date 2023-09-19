# Python Project Structure: PyCharm & GitHub Checklist

## Identifying the Root Folder

1. **Root Folder**: The root folder contains your entire project. It's the parent folder of all other folders and files.
2. **PyCharm Display**: In PyCharm, the root folder typically appears at the top of your "Project" tool window.

## Folder Relationship

1. **`src/`**: Houses the main Python code.

- **Role**: Contains modules, packages, and scripts.
- **PyCharm**: Mark as "Sources Root" by right-clicking -> "Mark Directory as" -> "Sources Root".
  
2. **`tests/`**: Contains test scripts.

- **Role**: Unit tests, integration tests, etc.
- **PyCharm**: Can be marked as "Excluded" if you don't want PyCharm to index these files.

3. **`.idea/`**: PyCharm configuration folder.

- **Role**: Stores PyCharm-specific settings.
- **Git**: Add to `.gitignore` as this is IDE-specific.

4. **`.venv/`**: Virtual environment folder.

- **Role**: Isolates project dependencies.
- **Git**: Add to `.gitignore`.

5. **`.git/`**: Git metadata and object database.

- **Role**: Version control.
- **PyCharm**: Automatically recognized.

## Marking Folders

- **Sources Root**: Mark `src/` as the Sources Root for PyCharm to recognize it as the main codebase.
- **Excluded Folders**: Folders like `tests/` can be excluded to prevent indexing, although not necessary.

## File Naming in Python

1. **LowerCase**: Use lowercase with underscores for file names (`my_module.py`).
2. **Clarity**: Choose clear, descriptive names.
3. **Extensions**: Always use `.py` extension for Python files.

## Test Case Naming in Python

1. **Prefix**: Use the `test_` prefix for test files (`test_module.py`) and test methods (`test_method_name`).
2. **TestCase Class**: Use camel case when naming test case classes (`MyTestCase`).
3. **Underscores**: Use underscores to separate words for better readability (`test_this_function_works`).

## Summary

- Identify your root folder as the top-level container of your project.
- Understand folder roles (`src/`, `tests/`, `.idea/`, `.venv/`, `.git/`) and how to mark them in PyCharm.
- Follow naming conventions for both Python files and test cases.
