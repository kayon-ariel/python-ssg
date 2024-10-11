from python_ssg.site_renderer import SiteRenderer
from unittest.mock import patch, MagicMock
import unittest


class TestSiteRenderer(unittest.TestCase):

    @patch('python_ssg.site_renderer.Storage.save_html')
    @patch('python_ssg.site_renderer.Environment.get_template')
    def test_render_site(self, mock_get_template, mock_save_html):
        # Arrange
        renderer = SiteRenderer()
        mock_template = MagicMock()
        mock_get_template.return_value = mock_template
        variables = {'key': 'value'}
        page_name = 'test_page'

        # Set the mock to return the expected rendered content
        mock_template.render.return_value = '<html><body>value</body></html>'

        # Act
        renderer.render_site(page_name, variables)

        # Assert
        mock_get_template.assert_called_once_with('test_page.html')
        mock_template.render.assert_called_once_with(variables)
        mock_save_html.assert_called_once_with(
            '<html><body>value</body></html>', 'test_page.html')


if __name__ == '__main__':
    unittest.main()
