import os
from pathlib import Path

import jupytext


def main():
    """
    Convert Jupyter notebooks in /notebooks to Markdown format in /markdown.
    """

    notebooks_dir = "./notebooks"
    markdown_dir = "./markdown"

    for root, _, files in os.walk(notebooks_dir):
        for file in files:
            if file.endswith(".ipynb"):
                notebook_path = Path(root) / file
                relative_path = notebook_path.relative_to(notebooks_dir)
                markdown_path = Path(markdown_dir) / relative_path.with_suffix(".md")

                # Create the directory structure in markdown_dir
                markdown_path.parent.mkdir(parents=True, exist_ok=True)

                # Read the notebook
                with open(notebook_path, "r", encoding="utf-8") as nb_file:
                    notebook = jupytext.read(nb_file)

                # Write the notebook as markdown
                with open(markdown_path, "w", encoding="utf-8") as md_file:
                    jupytext.write(notebook, md_file, fmt="md")

                print(f"Converted {notebook_path} to {markdown_path}")


if __name__ == "__main__":
    main()
