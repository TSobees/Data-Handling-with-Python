import argparse
from pathlib import Path
import pandas as pd
from .analysis import analyze

def main(argv=None):
    parser = argparse.ArgumentParser(description='Analyze student scores without editing source paths.')
    parser.add_argument('csv', nargs='?', type=Path, default=Path(__file__).resolve().parents[1]/'data/sample_scores.csv')
    parser.add_argument('--subjects', help='Comma-separated subject names; defaults to the eleven sample subjects.')
    parser.add_argument('--pass-mark', type=float, default=50)
    parser.add_argument('--output-dir', type=Path, default=Path('outputs'))
    args = parser.parse_args(argv)
    try:
        ranked, summary = analyze(pd.read_csv(args.csv), args.subjects.split(',') if args.subjects else None, args.pass_mark)
    except (OSError, ValueError, pd.errors.ParserError) as error:
        parser.error(str(error))
    args.output_dir.mkdir(parents=True, exist_ok=True)
    # Protect names from spreadsheet formula evaluation in exported CSVs.
    exported = ranked.copy()
    exported['Name'] = exported['Name'].map(lambda s: "'"+s if s.lstrip().startswith(('=', '+', '-', '@')) else s)
    exported.to_csv(args.output_dir/'student_rankings.csv', index=False, float_format='%.2f')
    summary.to_csv(args.output_dir/'subject_summary.csv', index=False, float_format='%.2f')
    print(ranked.to_string(index=False))
    print('\nSubject summary\n' + summary.round(2).to_string(index=False))
    print('\nTop students: ' + ', '.join(ranked.loc[ranked['Rank'].eq(1), 'Name']))
    print('Reports saved in ' + str(args.output_dir.resolve()))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
