# Sensor Fusion for Human Activity Recognition

This repository contains a completed study of multimodal human activity recognition using the MHEALTH dataset. It evaluates whether combining wearable accelerometer and gyroscope measurements improves participant-independent classification.

The adapted input contained 343,195 observations from ten participants performing 12 activities. After controlled short-gap interpolation and segmentation into overlapping 128-sample windows, 4,581 windows were retained. Random Forest models were evaluated with leave-one-subject-out cross-validation so that every test fold represented an unseen participant.

## Main findings

The combined three-location accelerometer model was the strongest evaluated system:

| Model | Accuracy | Macro F1 |
|---|---:|---:|
| Accelerometers, all locations | 96.81% | 96.91% |
| Feature fusion | 96.44% | 96.51% |
| Decision fusion | 96.44% | 96.45% |
| Ankle accelerometer | 85.96% | 87.09% |
| Chest accelerometer | 82.71% | 83.40% |
| Gyroscopes, ankle and wrist | 78.63% | 75.28% |
| Wrist accelerometer | 73.96% | 73.74% |

Adding gyroscope features did not improve pooled macro F1 under this design. Participant-level effects were mixed, and the main residual confusions included running versus jogging and sitting versus standing. These findings apply to this small, structured dataset and are not evidence for clinical, employment, insurance, or safety-critical use.

The final written report is [`report/MHEALTH_Report_v2_preview.pdf`](report/MHEALTH_Report_v2_preview.pdf). Its nine publication figures are preserved unchanged in [`figures/`](figures/).

## Repository layout

```text
.
├── notebooks/       Executed notebooks for exploration, modelling, and evaluation
├── src/             Shared evaluation, statistical, and plotting helpers
├── data/            Dataset acquisition and local-placement instructions only
├── results/         Derived features, predictions, metrics, audits, and manifests
├── figures/         Final report figures; protected and not regenerated in place
├── report/          Final report PDF; protected and unchanged
├── docs/            Historical project-progress record
├── run_notebooks.py Reproducible notebook runner
└── requirements.txt Pinned Python dependencies
```

`results/final_figure_selection.csv` is the current manifest for all nine final figures. Generated diagnostic figures and report notes are written beneath `results/`, never over the protected final deliverables.

## Data

The raw dataset is intentionally excluded because of size and redistribution considerations. Obtain MHEALTH from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/319/mhealth+dataset), then follow [`data/README.md`](data/README.md). The original project used an adapted archive named `MHEALTHDATASET_MISSING.zip`; reproducing Tasks 1–2 exactly requires that supplied archive, whose expected SHA-256 is recorded in `results/preprocessing_config.json`.

## Reproduction

Python 3.12 was used for the recorded analysis.

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

To reproduce feature extraction from the adapted raw archive, place it at `data/MHEALTHDATASET_MISSING.zip`, then run:

```powershell
python run_notebooks.py notebooks/01_tasks_1_2_exploration_preprocessing.ipynb
```

Tasks 3 and 4 can be reproduced from the included derived feature tables without the raw archive:

```powershell
python run_notebooks.py
```

The runner always executes with the repository root as the working directory. The notebooks also detect whether they were launched from the root or from `notebooks/`. Regenerated plots are saved to `results/generated_figures/`, and regenerated narrative notes to `results/generated_notes/`.

Random Forest settings are fixed at 200 trees, square-root feature sampling, minimum leaf size two, balanced training weights, and seed 42. No hyperparameter search was conducted. Exact model, preprocessing, feature, and split specifications are retained as JSON and CSV manifests in `results/`.

### Timing note

The final report records combined-accelerometer and decision-fusion totals of 36.403 s and 67.165 s. The currently retained notebook artifacts record 25.494 s and 49.418 s. These are expected wall-clock differences between executions or environments, not a discrepancy in predictions or performance results: model metrics and saved out-of-fold predictions remain consistent. Timing excludes data acquisition, feature extraction, memory, energy, and model-size costs.

The final report and its nine figures were treated as immutable deliverables during repository preparation. They were not edited, renamed, regenerated, re-cropped, or re-exported.

## Reproducibility boundaries

- Raw-data adaptation and the mechanism that introduced missingness were not independently verified.
- There are only ten participant clusters and no external validation dataset.
- Activity boundaries are known during preprocessing, unlike a continuous deployment stream.
- Overlapping windows are not independent observations.
- Bootstrap intervals condition on saved out-of-fold predictions and do not include retraining variability.

## Citation and license

Repository citation metadata is provided in [`CITATION.cff`](CITATION.cff). Please confirm the author spelling, repository URL, and release metadata before publication.

Code and repository-authored documentation are released under the MIT License; see [`LICENSE`](LICENSE). The MHEALTH dataset remains subject to its source terms, and the final report and figures should be cited as research outputs rather than assumed to inherit dataset licensing.
