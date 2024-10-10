from python_ssr.storage import Storage
import unittest
import shutil
import os


class TestStorage(unittest.TestCase):

    def tearDown(self):
        # Remove the temporary directory after tests
        shutil.rmtree('dist', ignore_errors=True)
        shutil.rmtree('html', ignore_errors=True)

    def test_create_dist_folder(self):
        # Act
        Storage.create_dist_folder()

        # Assert
        self.assertTrue(os.path.exists('dist'))

    def test_copy_assets(self):
        # Ensure the dist folder is created
        Storage.create_dist_folder()

        # Setup: Create assets directory and a test file
        os.makedirs('html/assets', exist_ok=True)
        with open('html/assets/test_file.txt', 'w') as f:
            f.write('test')

        # Act
        Storage.copy_assets()

        # Assert
        self.assertTrue(os.path.exists('dist/assets/test_file.txt'))

    def test_save_html(self):
        # Ensure the dist folder is created
        Storage.create_dist_folder()

        # Act
        Storage.save_html('<html></html>', 'test_output.html')

        # Assert
        self.assertTrue(os.path.exists('dist/test_output.html'))


if __name__ == '__main__':
    unittest.main()
