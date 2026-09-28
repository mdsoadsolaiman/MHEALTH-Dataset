# Historical project progress

> **Status:** This file is a preserved working record from before the final report was assembled. It is superseded by the repository `README.md`, the final PDF in `report/`, and the current nine-figure manifest in `results/final_figure_selection.csv`. Statements below describing the report as unfinished or listing earlier runtime measurements reflect that earlier project state.

Tasks 1–4 are complete within the agreed scope; final report assembly has not started. The official assignment brief/rubric remains unavailable.

## Task 3
- Sources: chest, left ankle and right wrist/lower arm.
- Modalities: acceleration and angular velocity (gyroscopes).
- Classifier: Random Forest, 200 trees, minimum leaf size 2, square-root feature subsampling, balanced training weights, seed 42, one worker.
- Tuning: none; settings fixed before evaluation. Inner grouped tuning is not claimed.
- Experiments: three individual accelerometer baselines, combined acceleration, combined gyroscopes, feature fusion and decision fusion.
- Completion: all 10 outer folds; 60 trained forests and 70 model/fold evaluations. No incomplete model experiments.
- Data controls: unchanged 4,581 windows, matched IDs/labels, participant-disjoint splits, no metadata predictors, no learned preprocessing fitted outside training folds, probability alignment and fixed fusion weights.
- Saved metrics: task3_overall_metrics.csv and task3_fold_metrics.csv. Runtime: task3_runtime_summary.csv.

## Task 4 verified metrics (proportions)
model,accuracy,macro_precision,macro_recall,macro_f1
Chest accelerometer,0.8271119842829077,0.8432087821751391,0.8355047488277831,0.8339939487169611
Ankle accelerometer,0.8596376337044314,0.8781437220303387,0.8691406641410451,0.8709489442860078
Wrist accelerometer,0.7395765116786728,0.752898863088876,0.733902197411505,0.7373640986289215
Accelerometers (all locations),0.9681292294258896,0.9721929699549936,0.9679081397253084,0.969133217558614
Gyroscopes (ankle + wrist),0.7862912027941498,0.7842418322848118,0.7485552066476081,0.7527881025968401
Feature fusion,0.964418249290548,0.968464117420304,0.9633590956339227,0.9651367312612248
Decision fusion,0.964418249290548,0.9687322330496352,0.9620718996967526,0.9644633859696612

## Actual main findings
All-location acceleration is the strongest unimodal baseline. Feature and decision fusion slightly reduce pooled macro F1; participant-level effects are mixed, with intervals spanning improvement and decline. Both fusions outperform individual-source acceleration and the gyroscope baseline in pooled macro F1. Running/jogging and sitting/standing are important confusions; decision fusion also confuses knees bending with climbing stairs. Detailed numerical interpretation is in report/task4_evaluation_critical_discussion.md.

## Computational results (seconds across ten folds)
model,features,sources,modalities,component_models,train_seconds,prediction_seconds,total_seconds
Chest accelerometer,18,1,1,1,19.07093490900036,0.1082457819999258,19.179180691000283
Ankle accelerometer,18,1,1,1,18.58748532200013,0.1094596919994041,18.69694501399954
Wrist accelerometer,18,1,1,1,19.43789692500025,0.1170273719999381,19.554924297000184
Accelerometers (all locations),54,3,1,1,25.40264799599936,0.0911275200004406,25.4937755159998
Gyroscopes (ankle + wrist),36,2,1,1,23.817783223000102,0.1068136479999559,23.924596871000062
Feature fusion,90,3,2,1,31.22418638099998,0.1004356859998545,31.32462206699984
Decision fusion,90,3,2,2,49.220431218999465,0.1980616610003374,49.4184928799998

Decision cost includes both modality components plus averaging, reusing measured component costs. No memory, model-size or energy measurement is claimed.

## Ethics and limitations
Movement/ECG privacy, consent, secondary use, surveillance, security and consequences of errors are discussed. Demographic fairness is untested. Limits include ten participants, adapted data with unknown missingness, assumed 50 Hz timing, known activity boundaries, offline interpolation, overlapping windows, all-channel eligibility despite selected-channel models, fixed parameters, no external/continuous-stream validation and no sensor-dropout test.

Priority improvements: external and continuous-stream evaluation; clarify missingness; training-only calibration or weighting; explicit sensor-dropout experiments. These are unperformed future work.

## Figures and validation
Seven figures are proposed in results/final_figure_selection.csv. Figures 5–7 add model performance, participant variation and multi-panel confusion matrices. All were visually inspected. Metrics reproduce, fusion probabilities equal the declared average, and bootstrap calculations respect participant clustering. See report/validation_checks.md.

## Execution and repository
No model reruns for better results. Initial runner import issue was resolved before fitting. Notebooks ran in fresh-process IPython because kernel sockets are unavailable. A native Jupyter restart/run-all on the user's computer remains unverified here. No repository existed locally, and no remote privacy status was inspected. Nothing was pushed or published.

## Exact next step
Obtain the official brief/rubric and compare report/rubric_audit.md with it. Then assemble Tasks 1–4 using the verified tables and seven figure candidates, respecting the official page-limit rules. Do not modify the experimental design in response to test results.
