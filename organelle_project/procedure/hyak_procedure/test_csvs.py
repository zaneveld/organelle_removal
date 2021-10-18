import pandas as pd
import pandas.testing as pd_testing
import unittest
import csvs

load_tbp = csvs.load_tbp
get_proportions_and_counts = csvs.get_proportions_and_counts

class TestProportionsAndCounts(unittest.TestCase):

    def assert_df_equal(self, left, right, msg):
        try:
            pd_testing.assert_frame_equal(left, right, check_dtype = False, check_exact = True)
        except AssertionError as e:
            raise self.failureException(msg) from e
    
    def setUp(self):
        self.addTypeEqualityFunc(pd.DataFrame, self.assert_df_equal)
        self.df = pd.DataFrame(index = range(5),
                          columns = ['Unassigned',
                                     'd__Bacteria;p__Cyanobacteria;c__Cyanobacteriia;o__Chloroplast',
                                     'd__Bacteria;p__Proteobacteria;c__Alphaproteobacteria;o__Rickettsiales;f__Mitochondria',
                                     'k__Bacteria;p__Cyanobacteria;c__Chloroplast',
                                     'k__Bacteria;p__Proteobacteria;c__Alphaproteobacteria;o__Rickettsiales;f__mitochondria']).fillna(10)

    def test_math(self):
        """Test that the proportion math and the count return the correct result
        (0.2 and 10, respectively)"""
        unassigned_expected = pd.DataFrame({'proportion unassigned': [0.2,
                                                                         0.2,
                                                                         0.2,
                                                                         0.2,
                                                                         0.2],
                                               'absolute unassigned': [10, 10,
                                                                       10, 10,
                                                                       10]})
        unassigned_actual = get_proportions_and_counts(self.df, 'Unassigned',
                                                          'unassigned')

        chloroplasts_expected = pd.DataFrame({'proportion chloroplasts': [0.2,
                                                                            0.2,
                                                                            0.2,
                                                                            0.2,
                                                                            0.2],
                                               'absolute chloroplasts': [10, 10,
                                                                         10, 10,
                                                                         10]})
        silva_chloroplasts_actual = get_proportions_and_counts(self.df,
                                                               'd__Bacteria;p__Cyanobacteria;c__Cyanobacteriia;o__Chloroplast',
                                                               'chloroplasts')
        gg_chloroplasts_actual = get_proportions_and_counts(self.df,
                                                            'k__Bacteria;p__Cyanobacteria;c__Chloroplast',
                                                            'chloroplasts')

        mitochondria_expected = pd.DataFrame({'proportion mitochondria': [0.2,
                                                                             0.2,
                                                                             0.2,
                                                                             0.2,
                                                                             0.2],
                                               'absolute mitochondria': [10, 10,
                                                                         10, 10,
                                                                         10]})
        silva_mitochondria_actual = get_proportions_and_counts(self.df,
                                                               'd__Bacteria;p__Proteobacteria;c__Alphaproteobacteria;o__Rickettsiales;f__Mitochondria',
                                                               'mitochondria')
        gg_mitochondria_actual = get_proportions_and_counts(self.df,
                                                            'k__Bacteria;p__Proteobacteria;c__Alphaproteobacteria;o__Rickettsiales;f__mitochondria',
                                                            'mitochondria')

        self.assertEqual(unassigned_expected, unassigned_actual, 'unassigned')
        self.assertEqual(chloroplasts_expected, silva_chloroplasts_actual, 'silva chloroplasts')
        self.assertEqual(chloroplasts_expected, gg_chloroplasts_actual, 'gg chloroplasts')
        self.assertEqual(mitochondria_expected, silva_mitochondria_actual, 'silva mitochondria')
        self.assertEqual(mitochondria_expected, gg_mitochondria_actual, 'gg mitochondria')

    def test_missing_columns(self):
        """Test that when taxon columns are absent, counts and proportions appropriately
        return zeroes"""
        no_unassigned = self.df.drop('Unassigned', 1)
        no_chloroplasts = self.df.drop(['d__Bacteria;p__Cyanobacteria;c__Cyanobacteriia;o__Chloroplast',
                                      'k__Bacteria;p__Cyanobacteria;c__Chloroplast'],
                                      1)
        no_mitochondria = self.df.drop(['d__Bacteria;p__Proteobacteria;c__Alphaproteobacteria;o__Rickettsiales;f__Mitochondria',
                                      'k__Bacteria;p__Proteobacteria;c__Alphaproteobacteria;o__Rickettsiales;f__mitochondria'],
                                      1)
        
        unassigned_expected = pd.DataFrame({'proportion unassigned': [0, 0,
                                                                         0, 0,
                                                                         0],
                                               'absolute unassigned': [0, 0, 0,
                                                                       0, 0]})
        unassigned_actual = get_proportions_and_counts(no_unassigned,
                                                          'Unassigned',
                                                          'unassigned')

        chloroplasts_expected = pd.DataFrame({'proportion chloroplasts': [0,
                                                                             0,
                                                                             0,
                                                                             0,
                                                                             0],
                                               'absolute chloroplasts': [0, 0,
                                                                         0, 0,
                                                                         0]})
        silva_chloroplasts_actual = get_proportions_and_counts(no_chloroplasts,
                                                            'd__Bacteria;p__Cyanobacteria;c__Cyanobacteriia;o__Chloroplast',
                                                            'chloroplasts')
        gg_chloroplasts_actual = get_proportions_and_counts(no_chloroplasts,
                                                               'k__Bacteria;p__Cyanobacteria;c__Chloroplast',
                                                               'chloroplasts')
        
        mitochondria_expected = pd.DataFrame({'proportion mitochondria': [0,
                                                                             0,
                                                                             0,
                                                                             0,
                                                                             0],
                                               'absolute mitochondria': [0, 0,
                                                                         0, 0,
                                                                         0]})
        silva_mitochondria_actual = get_proportions_and_counts(no_mitochondria,
                                                                  'd__Bacteria;p__Proteobacteria;c__Alphaproteobacteria;o__Rickettsiales;f__Mitochondria',
                                                                  'mitochondria')
        gg_mitochondria_actual = get_proportions_and_counts(no_mitochondria,
                                                               'k__Bacteria;p__Proteobacteria;c__Alphaproteobacteria;o__Rickettsiales;f__mitochondria',
                                                               'mitochondria')

        self.assertEqual(unassigned_expected, unassigned_actual, 'unassigned')
        self.assertEqual(chloroplasts_expected, silva_chloroplasts_actual, 'silva chloroplasts')
        self.assertEqual(chloroplasts_expected, gg_chloroplasts_actual, 'gg chloroplasts')
        self.assertEqual(mitochondria_expected, silva_mitochondria_actual, 'silva mitochondria')
        self.assertEqual(mitochondria_expected, gg_mitochondria_actual, 'gg mitochondria')
        
    def test_zero_count(self):
        """Test whether samples with zero of the specified taxa appropriately
        return zero counts and proportions"""

        zero_unassigned = self.df.copy()
        zero_unassigned['Unassigned'] = 0

        zero_chloroplasts = self.df.copy()
        zero_chloroplasts['d__Bacteria;p__Cyanobacteria;c__Cyanobacteriia;o__Chloroplast'] = 0
        zero_chloroplasts['k__Bacteria;p__Cyanobacteria;c__Chloroplast'] = 0

        zero_mitochondria = self.df.copy()
        zero_mitochondria['d__Bacteria;p__Proteobacteria;c__Alphaproteobacteria;o__Rickettsiales;f__Mitochondria'] = 0
        zero_mitochondria['k__Bacteria;p__Proteobacteria;c__Alphaproteobacteria;o__Rickettsiales;f__mitochondria'] = 0

        unassigned_expected = pd.DataFrame({'proportion unassigned': [0, 0,
                                                                         0, 0,
                                                                         0],
                                               'absolute unassigned': [0, 0, 0,
                                                                       0, 0]})
        unassigned_actual = get_proportions_and_counts(zero_unassigned,
                                                          'Unassigned',
                                                          'unassigned')

        chloroplasts_expected = pd.DataFrame({'proportion chloroplasts': [0,
                                                                             0,
                                                                             0,
                                                                             0,
                                                                             0],
                                               'absolute chloroplasts': [0, 0,
                                                                         0, 0,
                                                                         0]})
        silva_chloroplasts_actual = get_proportions_and_counts(zero_chloroplasts,
                                                            'd__Bacteria;p__Cyanobacteria;c__Cyanobacteriia;o__Chloroplast',
                                                            'chloroplasts')
        gg_chloroplasts_actual = get_proportions_and_counts(zero_chloroplasts,
                                                               'k__Bacteria;p__Cyanobacteria;c__Chloroplast',
                                                               'chloroplasts')
        
        mitochondria_expected = pd.DataFrame({'proportion mitochondria': [0,
                                                                             0,
                                                                             0,
                                                                             0,
                                                                             0],
                                               'absolute mitochondria': [0, 0,
                                                                         0, 0,
                                                                         0]})
        silva_mitochondria_actual = get_proportions_and_counts(zero_mitochondria,
                                                                  'd__Bacteria;p__Proteobacteria;c__Alphaproteobacteria;o__Rickettsiales;f__Mitochondria',
                                                                  'mitochondria')
        gg_mitochondria_actual = get_proportions_and_counts(zero_mitochondria,
                                                               'k__Bacteria;p__Proteobacteria;c__Alphaproteobacteria;o__Rickettsiales;f__mitochondria',
                                                               'mitochondria')

        self.assertEqual(unassigned_expected, unassigned_actual, 'unassigned')
        self.assertEqual(chloroplasts_expected, silva_chloroplasts_actual, 'silva chloroplasts')
        self.assertEqual(chloroplasts_expected, gg_chloroplasts_actual, 'gg chloroplasts')
        self.assertEqual(mitochondria_expected, silva_mitochondria_actual, 'silva mitochondria')
        self.assertEqual(mitochondria_expected, gg_mitochondria_actual, 'gg mitochondria')

#needed? empty samples probably shouldn't be included in the data. but we're
#running this before filtering for things like that, right? so it might be worth?
#    def test_empty_sample:
#

#how do i want to deal with gg/silva nomenclature? should I role it into a parameter of the counting function?
#should the whole function be specific to unassigned, chloroplasts, and mitochondria? 
#should the whole function do all three?
#    def test_gg_format:
#
#    def test_silva_format:


if __name__ == '__main__':
    unittest.main()