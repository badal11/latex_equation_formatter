# LaTeX Equation Formatter

This Python script is a versatile tool for converting LaTeX equations between different formats. It allows you to easily switch between the following LaTeX equation formats:

- `$...$` to `\( ... \)`
- `\( ... \)` to `$...$`
- `$$...$$` to `\[ ... \]`
- `\[ ... \]` to `$$...$$`

## Usage

### Command-Line Usage

You can use this tool from the command line by running `converter.py` with the following arguments:

```bash
python converter.py <mode> <path> <filetype>
```

- `<mode>`: The conversion mode, which can be either "dedollarify" or "dollarify" LaTeX format.
- `<path>`: The file or directory path to process.
- `<filetype>`: applies regex replacements to only files ending with this specified extension.  

Examples:

- To convert LaTeX equations in a single file from `$...$` and `$$...$$` to `\( ... \)` and `\[ ... \]` format:

```bash
python converter.py dedollorify input.tex tex
```

- To convert LaTeX equations in a single file from`\( ... \)` and `\[ ... \]` to `$...$` and `$$...$$` format:

```bash
python converter.py dollorify input.tex tex
```

- To convert LaTeX equations in all `.tex` files within a directory and its subdirectories:

```bash
python converter.py dedollorify /path/to/directory md
```

### Unit Tests

To ensure the correctness of the conversion functions, we have included unit tests. You can run them using the following command:

```bash
python -m unittest tests/basic_tests.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project was inspired by the need to simplify LaTeX equation conversion.
- Special thanks to the Python community for the `argparse` and `unittest` modules.

---

Feel free to contribute, report issues, or provide feedback to make this tool even better!


Make sure to customize the README by adding information specific to your project, such as installation instructions, additional features, and any other relevant details. Also, consider including a license file (e.g., `LICENSE`) in your repository if you haven't already.