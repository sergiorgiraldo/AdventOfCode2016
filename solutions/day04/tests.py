import unittest

from solution import Solution

class Tests(unittest.TestCase):
    def test_real_rooms(self):
        solution = Solution()  
        rooms = [                
            "aaaaa-bbb-z-y-x-123[abxyz]",
            "a-b-c-d-e-f-g-h-987[abcde]",
            "not-a-real-room-404[oarel]",
            "totally-real-room-200[decoy]"
          ]

        self.assertEqual(solution.get_sector_real_rooms(rooms), 1_514, "Oops")

    def test_get_room_name(self):
        solution = Solution()  
        self.assertEqual(solution.decrypt("qzmt", 343), "very", "Oops")
        self.assertEqual(solution.decrypt("zixmtkozy", 343), "encrypted", "Oops")
        self.assertEqual(solution.decrypt("ivhz", 343), "name", "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")

if __name__ == '__main__':
    unittest.main()