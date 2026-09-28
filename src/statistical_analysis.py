"""Paired participant-cluster bootstrap of saved out-of-fold predictions."""
import numpy as np
from src.evaluation import metrics_from_counts

def cluster_bootstrap(confusion_by_participant, repeats=2000, seed=42):
    # Shape: models x participants x true classes x predicted classes.
    n_people = confusion_by_participant.shape[1]
    rng = np.random.default_rng(seed)
    weights = rng.multinomial(n_people, np.full(n_people, 1 / n_people), size=repeats)
    # The same resampled participants are used for every model.
    counts = np.einsum('bp,mpij->bmij', weights, confusion_by_participant)
    accuracy, f1 = metrics_from_counts(counts)
    return {'accuracy': accuracy, 'macro_f1': f1}
