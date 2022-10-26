import unittest
from shared.asteroids import Asteroids
from shared.file_reader import read_chars_multiple_lines as file_read

class TestAsteroids(unittest.TestCase):
   def test_visibility_map(self):  
      self.assertEqual(
         int(max(Asteroids(file_read('shared/test_asteroids1.txt')).get_visibility_map())), 8
      )
      self.assertEqual(
         int(max(Asteroids(file_read('shared/test_asteroids2.txt')).get_visibility_map())), 33
      )
      self.assertEqual(
         int(max(Asteroids(file_read('shared/test_asteroids3.txt')).get_visibility_map())), 35
      )
      self.assertEqual(
         int(max(Asteroids(file_read('shared/test_asteroids4.txt')).get_visibility_map())), 41
      )
      self.assertEqual(
         int(max(Asteroids(file_read('shared/test_asteroids5.txt')).get_visibility_map())), 210
      )

   def test_fire_laser(self):
      asteroids = Asteroids(file_read('shared/test_asteroids5.txt'))
      visibility = asteroids.get_visibility_map()
      asteroids_destroyed = asteroids.fire_laser(visibility.index(max(visibility)))
      self.assertEqual(len(asteroids_destroyed), 299)
      self.assertEqual(asteroids_destroyed[0], (11,12))
      self.assertEqual(asteroids_destroyed[199], (8,2))
      self.assertEqual(asteroids_destroyed[len(asteroids_destroyed) - 1], (11,1))


if __name__ == '__main__':
    unittest.main()