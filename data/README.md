# MHEALTH data

Raw sensor recordings are not committed to this repository.

The public MHEALTH dataset is available from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/319/mhealth+dataset). Review the source documentation, citation guidance, and terms before use.

This project was completed with a supplied, adapted archive containing missing sensor values. To reproduce Tasks 1–2 exactly, place that archive here as:

```text
data/MHEALTHDATASET_MISSING.zip
```

The expected SHA-256 digest is recorded in `../results/preprocessing_config.json`. The first notebook validates the archive structure and records its digest without modifying the archive.

The original public UCI archive may not reproduce the missingness analysis because it is not necessarily identical to the adapted coursework input. Tasks 3–4 can run without raw data by using the committed derived feature and metadata tables in `results/`.
