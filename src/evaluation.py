"""Small evaluation helpers shared by the two notebooks."""
import numpy as np
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

CLASSES = np.arange(1, 13)
ACTIVITIES = ['Standing', 'Sitting', 'Lying down', 'Walking', 'Climbing stairs',
              'Waist bends', 'Arm elevation', 'Knees bending', 'Cycling',
              'Jogging', 'Running', 'Jump front/back']

def scores(y_true, y_pred):
    precision, recall, f1, _ = precision_recall_fscore_support(
        y_true, y_pred, labels=CLASSES, average='macro', zero_division=0)
    return {'accuracy': accuracy_score(y_true, y_pred), 'macro_precision': precision,
            'macro_recall': recall, 'macro_f1': f1}

def metrics_from_counts(counts):
    """Calculate pooled accuracy and macro F1 from confusion-matrix counts."""
    tp = np.diagonal(counts, axis1=-2, axis2=-1)
    true_count = counts.sum(axis=-1)
    predicted_count = counts.sum(axis=-2)
    denominator = true_count + predicted_count
    f1 = np.divide(2 * tp, denominator, out=np.zeros_like(tp, dtype=float), where=denominator != 0)
    accuracy = tp.sum(axis=-1) / counts.sum(axis=(-2, -1))
    return accuracy, f1.mean(axis=-1)
