"""
JPMC Virtual SEP - InsideSherpa - Module 1
Pedro Teixeira - O734271

Unit tests for the alerts module
"""

import unittest
from alerts import AlertService

class TestAlertService(unittest.TestCase):
    """
    Provides Unit Tests for AlertService

    * Uses both positive and negative test cases
    * Focus on testing the parsing separated from the validation to benefit 
    from the granularity since the exercise is small enough that we can afford 
    it.
    """

    def setUp(self):
        self.alert_service = AlertService()

    # Positive test cases for the parsing function ============================

    def test_parsing_ints(self):
        """Test a regular integer-only input"""
        result = self.alert_service._parse("(1234,0,0,0)")
        self.assertEqual(('1234',0,0,0), result)

    def test_parsing_negative_ints(self):
        """Test negative integer inputs"""
        result = self.alert_service._parse("(1234,-1,-1,-1)")
        self.assertEqual(('1234',-1,-1,-1), result)

    def test_parsing_floats(self):
        """Test floating-point utilization values"""
        result = self.alert_service._parse("(1234,0.5,0.5,0.5)")
        self.assertEqual(('1234',0,0,0), result)

    def test_parsing_spaces(self):
        """Test multiple spaces in multiple locations within tuple"""
        result = self.alert_service._parse("( 1234   , 2, 3  , 5.5)")
        self.assertEqual(('1234',2,3,6), result)

    def test_parsing_alphanum_server_id(self):
        """Test alphabetical chars in the server id"""
        result = self.alert_service._parse("(ABC123,4,5,6)")
        self.assertEqual(('ABC123',4,5,6), result)

    # Negative test cases for the parsing function ============================

    def test_parsing_fails_alpha_utilization(self):
        """Test that alphabetic chars in utilization raises a ValueError"""
        with self.assertRaises(ValueError):
            self.alert_service._parse("(1234,a,1,1)")

    def test_parsing_fails_not_enough_vlaues(self):
        """Test that not enough utilization values raises a ValueError"""
        with self.assertRaises(ValueError):
            self.alert_service._parse("(1234,1,1)")

    def test_parsing_too_many_values(self):
        """Test that too many utilization values raises a ValueError"""
        with self.assertRaises(ValueError):
            self.alert_service._parse("(1,1,1,1,1)")

    def test_parsing_fails_empty_string(self):
        """Test that empty string raises a ValueError"""
        with self.assertRaises(ValueError):
            self.alert_service._parse("")

    # Positive test cases for the validation function =========================

    def test_validation_no_utilization(self):
        out = self.alert_service._validate("1234",0,0,0)
        self.assertEqual(f"({AlertService.NO_ALERT}, 1234)", out)

    def test_validation_full_utilization(self):
        out = self.alert_service._validate("1234",100,100,100)
        self.assertEqual(f"({AlertService.ALERT}, 1234, " \
            f"{AlertService.RULE_CPU}, {AlertService.RULE_MEM}, {AlertService.RULE_DSK})", out)

    def test_validation_cpu_utilization(self):
        out = self.alert_service._validate("1234",100,0,0)
        self.assertEqual(f"({AlertService.ALERT}, 1234, " \
            f"{AlertService.RULE_CPU})", out)

    def test_validation_mem_utilization(self):
        out = self.alert_service._validate("1234",0,100,0)
        self.assertEqual(f"({AlertService.ALERT}, 1234, " \
            f"{AlertService.RULE_MEM})", out)

    def test_validation_disk_utilization(self):
        out = self.alert_service._validate("1234",0,0,100)
        self.assertEqual(f"({AlertService.ALERT}, 1234, " \
            f"{AlertService.RULE_DSK})", out)

    def test_validation_limit_utilization(self):
        out = self.alert_service._validate("1234",85,75,60)
        self.assertEqual(f"({AlertService.NO_ALERT}, 1234)", out)

    def test_validation_over_limit_utilization(self):
        out = self.alert_service._validate("1234",86,76,61)
        self.assertEqual(f"({AlertService.ALERT}, 1234, " \
            f"{AlertService.RULE_CPU}, {AlertService.RULE_MEM}, {AlertService.RULE_DSK})", out)

    def test_validation_negative_values(self):
        out = self.alert_service._validate("1234",-1,-1,-1)
        self.assertEqual(f"({AlertService.NO_ALERT}, 1234)", out)

    # No negative testcases for the validation function


