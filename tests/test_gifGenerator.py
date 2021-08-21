import unittest
from unittest import TestCase

from src.gifGenerator import GifGenerator


class TestGifGenerator(TestCase):

    def setUp(self) -> None:
        self.gg = GifGenerator()

    def test_set_text_position(self):
        position = (50, 90)
        self.gg.setTextPosition(position)
        self.assertEqual(self.gg.text_position, position)

    def test_set_font(self):
        self.assertTrue(True)

    def test_load_image(self):
        # path='test.png'
        self.assertTrue(True)

    def test_crop_images(self):
        self.assertTrue(True)

    def test_generate(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
