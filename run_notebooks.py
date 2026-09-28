"""Execute project notebooks from the repository root.

Pass notebook paths relative to the repository root, or omit arguments to run
the modelling and evaluation notebooks in sequence.
"""
import sys
from pathlib import Path
import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parent
names = sys.argv[1:] or [
    'notebooks/02_task3_multimodal_fusion_modelling.ipynb',
    'notebooks/03_task4_evaluation_critical_discussion.ipynb',
]
for name in names:
    path = (ROOT / name).resolve()
    if ROOT not in path.parents:
        raise ValueError(f'Notebook must be inside the repository: {name}')
    notebook = nbformat.read(path, as_version=4)
    NotebookClient(notebook, timeout=1200, kernel_name='python3',
                   resources={'metadata': {'path': str(ROOT)}}).execute()
    nbformat.write(notebook, path)
    print(f'Completed {path.relative_to(ROOT)}')
