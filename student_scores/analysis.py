"""Validate score tables and produce reproducible descriptive summaries."""
import math
import pandas as pd

DEFAULT_SUBJECTS = ['English', 'Maths', 'Physics', 'Chemistry', 'Biology',
    'Geography', 'Further Maths', 'Computer Science', 'Technical Drawing',
    'Fisheries', 'Civic Education']

def analyze(frame, subjects=None, pass_mark=50):
    subjects = list(subjects or DEFAULT_SUBJECTS)
    if not subjects or len(set(subjects)) != len(subjects) or 'Name' in subjects:
        raise ValueError('Choose distinct subject columns, excluding Name.')
    if not math.isfinite(pass_mark) or not 0 <= pass_mark <= 100:
        raise ValueError('Pass mark must be between 0 and 100.')
    missing = [c for c in ['Name', *subjects] if c not in frame]
    if missing:
        raise ValueError('Missing columns: ' + ', '.join(missing))
    if frame.empty:
        raise ValueError('The CSV contains no student records.')
    result = frame[['Name', *subjects]].copy()
    if result['Name'].isna().any() or result['Name'].astype(str).str.strip().eq('').any():
        raise ValueError('Every student needs a name.')
    result['Name'] = result['Name'].astype(str).str.strip()
    if result['Name'].str.casefold().duplicated().any():
        raise ValueError('Student names must be unique; use a name with a unique ID if needed.')
    scores = result[subjects].apply(pd.to_numeric, errors='coerce')
    if scores.isna().any().any() or not scores.ge(0).all().all() or not scores.le(100).all().all():
        raise ValueError('All selected scores must be numbers between 0 and 100; missing scores are rejected.')
    result[subjects] = scores
    result['Average'] = scores.mean(axis=1)
    result['Rank'] = result['Average'].rank(method='min', ascending=False).astype(int)
    result = result.sort_values(['Rank', 'Name'], kind='stable').reset_index(drop=True)
    summary = pd.DataFrame({'Subject': subjects, 'Mean': scores.mean().values,
        'Highest': scores.max().values, 'Lowest': scores.min().values,
        'Pass Rate (%)': scores.ge(pass_mark).mean().mul(100).values})
    return result, summary
