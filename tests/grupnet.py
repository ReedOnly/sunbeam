import unittest
import sunbeam


class TestGrupnet(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        norne = '../../examples/data/norne/NORNE_ATW2013.DATA'
        cls.es = sunbeam.parse(norne, ('PARSE_RANDOM_SLASH', sunbeam.action.ignore))

    def test_vfp_table(self):
        self.assertEqual(0, self.es.schedule.group(timestep=0)['PROD'].vfp_table)
        self.assertEqual(9, self.es.schedule.group(timestep=0)['MANI-E2'].vfp_table)
        self.assertEqual(9, self.es.schedule.group(timestep=247)['MANI-E2'].vfp_table)
        self.assertEqual(9999, self.es.schedule.group(timestep=0)['MANI-K1'].vfp_table)
        self.assertEqual(0, self.es.schedule.group(timestep=0)['INJE'].vfp_table)


if __name__ == '__main__':
    unittest.main()
