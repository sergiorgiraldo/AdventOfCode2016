import unittest

from solution import Solution

class Tests(unittest.TestCase):
    def test_get_corrected_message_common(self):
        solution = Solution()
        messages = [
            "eedadn",
            "drvtee",
            "eandsr",
            "raavrd",
            "atevrs",
            "tsrnev",
            "sdttsa",
            "rasrtv",
            "nssdts",
            "ntnada",
            "svetve",
            "tesnvt",
            "vntsnd",
            "vrdear",
            "dvrsen",
            "enarar"
        ]
        self.assertEqual(solution.get_corrected_message_common(messages), "easter", "Oops")

    def test_get_corrected_message_uncommon(self):
        solution = Solution()
        messages = [
            "eedadn",
            "drvtee",
            "eandsr",
            "raavrd",
            "atevrs",
            "tsrnev",
            "sdttsa",
            "rasrtv",
            "nssdts",
            "ntnada",
            "svetve",
            "tesnvt",
            "vntsnd",
            "vrdear",
            "dvrsen",
            "enarar"
        ]
        self.assertEqual(solution.get_corrected_message_uncommon(messages), "advent", "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")

if __name__ == '__main__':
    unittest.main()