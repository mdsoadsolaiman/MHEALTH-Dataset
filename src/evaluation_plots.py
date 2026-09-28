"""Shared figure style and saving."""
from io import BytesIO
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

COLORS = ['#0072B2', '#E69F00', '#009E73', '#56B4E9', '#CC79A7', '#D55E00', '#444444']
REPO_ROOT = Path(__file__).resolve().parents[1]
GENERATED_FIGURES = REPO_ROOT / 'results' / 'generated_figures'

def set_style():
    sns.set_theme(style='whitegrid', context='notebook')
    plt.rcParams.update({'figure.dpi': 110, 'savefig.dpi': 300,
                         'font.family': 'DejaVu Sans', 'axes.spines.top': False,
                         'axes.spines.right': False, 'axes.titleweight': 'bold'})

def save_plot(fig, name):
    GENERATED_FIGURES.mkdir(parents=True, exist_ok=True)
    buffer = BytesIO()
    fig.savefig(buffer, format='png', bbox_inches='tight')
    (GENERATED_FIGURES / f'{name}.png').write_bytes(buffer.getvalue())
    fig.savefig(GENERATED_FIGURES / f'{name}.svg', bbox_inches='tight')
    plt.show()
    plt.close(fig)
