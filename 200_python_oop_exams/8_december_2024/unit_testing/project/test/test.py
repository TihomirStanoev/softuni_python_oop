from project.gallery import Gallery
from unittest import TestCase, main

class TestsGallery(TestCase):
    VALID_NAME = 'Test'
    VALID_CITY = 'Sofia'
    VALID_AREA = 15.5
    def setUp(self):
        self.gallery = Gallery(self.VALID_NAME, self.VALID_CITY,self.VALID_AREA)

    def test_init(self):
        self.assertEqual(self.gallery.gallery_name, self.VALID_NAME)
        self.assertEqual(self.gallery.city, self.VALID_CITY)
        self.assertEqual(self.gallery.area_sq_m, self.VALID_AREA)
        self.assertIsInstance(self.gallery.exhibitions, dict)
        self.assertTrue(self.gallery.open_to_public)

    def test_gallery_name_assert_error(self):
        invalid_names = ['a a', 'z_', ' ','Gallery Name', 'Gallery#']
        for gallery_name in invalid_names:
            with self.subTest(gallery_name=gallery_name):
                with self.assertRaises(ValueError) as e:
                    self.gallery.gallery_name = gallery_name
                self.assertEqual(str(e.exception), 'Gallery name can contain letters and digits only!')

    def test_gallery_name_with_valid_names(self):
        valid_names = ['Gallery', 'Gallery2025', '2025']
        for gallery_name in valid_names:
            with self.subTest(gallery_name=gallery_name):
                self.gallery.gallery_name = gallery_name
                self.assertEqual(self.gallery.gallery_name, gallery_name)

    def test_city_setter_with_invalid_name_raises_value_error(self):
        invalid_cities = ['5ofia', '#ofia', ' ofia']
        for city in invalid_cities:
            with self.subTest(city = city):
                with self.assertRaises(ValueError) as e:
                    self.gallery.city = city
                self.assertEqual(str(e.exception), 'City name must start with a letter!')

    def test_city_setter_with_valid_name(self):
        valid_names = ['Sofia', 'sofia']
        for city in valid_names:
            with self.subTest(city = city):
                self.gallery.city = city
                self.assertEqual(self.gallery.city, city)

    def test_area_sq_with_less_or_eques_value(self):
        for area_sq_m in [-1.5, 0]:
            with self.subTest(area_sq_m=area_sq_m):
                with self.assertRaises(ValueError) as e:
                    self.gallery.area_sq_m = area_sq_m
                self.assertEqual(str(e.exception), 'Gallery area must be a positive number!')

    def test_area_sq_m_with_valid_value(self):
        valid_value = 55.1
        self.gallery.area_sq_m = valid_value
        self.assertEqual(self.gallery.area_sq_m, valid_value)

    def test_add_exhibition_with_non_existed_data(self):
        exhibition_name = 'Test'
        year = 2000
        test_exhibition = {exhibition_name: year}
        expected_result = f'Exhibition "{exhibition_name}" added for the year {year}.'
        result = self.gallery.add_exhibition(exhibition_name, year)

        self.assertEqual(result, expected_result)
        self.assertEqual(self.gallery.exhibitions, test_exhibition)
        self.assertIn(exhibition_name, self.gallery.exhibitions)

    def test_add_exhibition_with_existed_exhibition(self):
        exhibition_name = 'Test'
        year = 2000
        self.gallery.add_exhibition(exhibition_name, year)

        result = self.gallery.add_exhibition(exhibition_name, year)
        expected_result = f'Exhibition "{exhibition_name}" already exists.'

        self.assertEqual(result, expected_result)

    def test_remove_exhibition_if_exhibition_exist(self):
        exhibition_name = 'Test'
        year = 2000
        self.gallery.add_exhibition(exhibition_name, year)

        expected_result = f'Exhibition "{exhibition_name}" removed.'
        result = self.gallery.remove_exhibition(exhibition_name)

        self.assertEqual(expected_result, result)
        self.assertNotIn(exhibition_name, self.gallery.exhibitions)
        self.assertEqual(self.gallery.exhibitions, {})

    def test_remove_exhibition_if_exhibition_not_found(self):
        exhibition_name = 'Test'
        year = 2000

        expected_result = f'Exhibition "{exhibition_name}" not found.'
        result = self.gallery.remove_exhibition(exhibition_name)

        self.assertEqual(expected_result, result)

    def test_list_exhibitions_when_gallery_is_open(self):
        names = ['test1', 'test2']
        years = [2000, 2001]
        self.gallery.open_to_public = True

        for i in range(len(names)):
            self.gallery.add_exhibition(names[i], years[i])

        expected_result = '\n'.join(f"{name}: {year}" for name, year in dict(zip(names, years)).items())
        result = self.gallery.list_exhibitions()

        self.assertEqual(expected_result, result)

    def test_list_exhibitions_when_gallery_is_closed(self):
        self.gallery.open_to_public = False

        expected_result = f'Gallery {self.gallery.gallery_name} is currently closed for public! Check for updates later on.'
        result = self.gallery.list_exhibitions()

        self.assertFalse(self.gallery.open_to_public)
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()