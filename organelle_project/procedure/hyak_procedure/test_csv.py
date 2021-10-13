import numpy as np
import pandas as pd
import unittest

csv = __import__('csv.py')
load_tbp = csv.load_tbp
get_proportions_and_counts = csv.get_proportions_and_counts

class TestProportionsAndCounts(unittest.TestCase):

    def setUp(self):
        rng = np.random.default_rng()
        df = pd.DataFrame(rng.integers(0, 100, size = (5, 5)),
                          columns = ['Unassigned', 'd__Bacteria;p__Cyanobacteria;c__Cyanobacteriia;o__Chloroplast',
                                     'd__Bacteria;p__Proteobacteria;c__Alphaproteobacteria;o__Rickettsiales;f__Mitochondria',
                                     'k__Bacteria;p__Cyanobacteria;c__Chloroplast',
                                     'k__Bacteria;p__Proteobacteria;c__Alphaproteobacteria;o__Rickettsiales;f__mitochondria'])

    def test_missing_columns:
        """Test that when taxon columns are absent, counts and proportions appropriately
        return zeroes"""
        df_no_unassigned = df.drop('Unassigned', 1)
        # df_no_chloroplasts = df.drop(['d__Bacteria;p__Cyanobacteria;c__Cyanobacteriia;o__Chloroplast',
        #                               'k__Bacteria;p__Cyanobacteria;c__Chloroplast'],
        #                               1)
        # df_no_mitochondria = df.drop(['d__Bacteria;p__Proteobacteria;c__Alphaproteobacteria;o__Rickettsiales;f__Mitochondria',
        #                               'k__Bacteria;p__Proteobacteria;c__Alphaproteobacteria;o__Rickettsiales;f__mitochondria'],
        #                               1)
        
        unassigned_expected_df = pd.DataFrame({'proportion unassigned': [0, 0,
                                                                         0, 0,
                                                                         0],
                                               'absolute unassigned': [0, 0, 0,
                                                                       0, 0]})
        unassigned_actual_df = get_proportions_and_counts(df_no_unassigned, 'Unassigned',
                                                          'unassigned')

        # chloroplasts_expected_df = pd.DataFrame({'proportion chloroplasts': [0,
        #                                                                      0,
        #                                                                      0,
        #                                                                      0,
        #                                                                      0],
        #                                        'absolute chloroplasts': [0, 0,
        #                                                                  0, 0,
        #                                                                  0]})
        # silva_chloroplasts_actual_df = get_proportions_and_counts(df_no_chloroplasts,
        #                                                     'd__Bacteria;p__Cyanobacteria;c__Cyanobacteriia;o__Chloroplast',
        #                                                     'chloroplasts')
        # gg_chloroplasts_actual_df = get_proportions_and_counts(df_no_chloroplasts,
        #                                                        'k__Bacteria;p__Cyanobacteria;c__Chloroplast',
        #                                                        'chloroplasts')
        
        # mitochondria_expected_df = pd.DataFrame({'proportion mitochondria': [0,
        #                                                                      0,
        #                                                                      0,
        #                                                                      0,
        #                                                                      0],
        #                                        'absolute mitochondria': [0, 0,
        #                                                                  0, 0,
        #                                                                  0]})
        # silva_mitochondria_actual_df = get_proportions_and_counts(df_no_mitochondria,
        #                                                           'd__Bacteria;p__Proteobacteria;c__Alphaproteobacteria;o__Rickettsiales;f__Mitochondria',
        #                                                           'mitochondria')
        # gg_mitochondria_actual_df = get_proportions_and_counts(df_no_mitochondria,
        #                                                        'k__Bacteria;p__Proteobacteria;c__Alphaproteobacteria;o__Rickettsiales;f__mitochondria')

        self.assertTrue(unassigned_expected_df.equals(unassigned_actual_df))#, 'unassigned')
        # self.assertTrue(chloroplasts_expected_df.equals(silva_chloroplasts_actual_df), 'chloroplasts')
        # self.assertTrue(chloroplasts_expected_df.equals(gg_chloroplasts_actual_df), 'chloroplasts')
        # self.assertTrue(mitochondria_expected_df.equals(silva_mitochondria_actual_df), 'mitochondria')
        # self.assertTrue(mitochondria_expected_df.equals(gg_mitochondria_actual_df), 'mitochondria')
        
    def test_zero_count:
        """Test whether samples with zero of the specified taxa appropriately
        return zero counts and proportions"""

#needed? empty samples probably shouldn't be included in the data. but we're
#running this before filtering for things like that, right? so it might be worth?
#    def test_empty_sample:
#

#how do i want to deal with gg/silva nomenclature? should I role it into a parameter of the counting function?
#should the whole function be specific to unassigned, chloroplasts, and mitochondria? 
#should the whole function do all three?
    def test_gg_format:

    def test_silva_format:


if __name__ == '__main__':
    unittest.main()