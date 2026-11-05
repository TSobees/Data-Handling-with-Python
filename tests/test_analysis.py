import unittest
import pandas as pd
from student_scores.analysis import analyze

class ScoreTests(unittest.TestCase):
    def frame(self):
        return pd.DataFrame({'Name':['A','B','C'], 'Maths':[80,90,90], 'English':[100,90,70]})
    def test_ties_and_subject_summary(self):
        ranked, summary = analyze(self.frame(), ['Maths','English'], 90)
        self.assertEqual(ranked['Rank'].tolist(), [1,1,3])
        self.assertEqual(ranked['Name'].tolist(), ['A','B','C'])
        self.assertAlmostEqual(summary.iloc[0]['Pass Rate (%)'], 200/3)
    def test_invalid_scores_are_not_silently_averaged(self):
        for bad in [-1,101,'bad',None,float('inf')]:
            f=self.frame().astype({'Maths':'object'});f.loc[0,'Maths']=bad
            with self.subTest(bad=bad), self.assertRaises(ValueError): analyze(f,['Maths','English'])
    def test_invalid_structure_and_names(self):
        for f in [pd.DataFrame(), self.frame().assign(Name=['A','a','C']),self.frame().assign(Name=['A',' ','C'])]:
            with self.assertRaises(ValueError): analyze(f,['Maths'])
    def test_missing_subject_or_invalid_threshold(self):
        with self.assertRaises(ValueError): analyze(self.frame(),['Physics'])
        with self.assertRaises(ValueError): analyze(self.frame(),['Maths'],float('nan'))
    def test_input_is_not_modified(self):
        f=self.frame();copy=f.copy(deep=True);analyze(f,['Maths']);pd.testing.assert_frame_equal(f,copy)

if __name__ == '__main__': unittest.main()
