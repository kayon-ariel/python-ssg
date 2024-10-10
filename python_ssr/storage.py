import shutil
import os


class Storage:
    """
    A class responsible for managing storage operations for the rendered site.
    This includes creating directories, copying assets, and saving HTML content.

    Methods:
        create_dist_folder: Creates the output directory for rendered HTML files if it doesn't exist.
        copy_assets: Copies static assets from the template directory to the output directory.
        save_html: Saves the rendered HTML content to a specified file.
    """

    @staticmethod
    def create_dist_folder():
        """
        Creates the 'dist' directory if it does not already exist.

        This directory is intended to store the rendered HTML files and other assets.
        """
        if not os.path.exists('dist'):
            os.makedirs('dist')  # Create the directory if it does not exist

    @staticmethod
    def copy_assets():
        """
        Copies the static assets from the 'html/assets' directory to the 'dist/assets' directory.

        This function uses shutil.copytree to copy all files and directories from the source to the destination.
        If the destination directory already exists, it will merge the directories.
        """
        shutil.copytree(
            # Source directory containing assets
            os.path.join('html', 'assets'),
            # Destination directory for assets
            os.path.join('dist', 'assets'),
            dirs_exist_ok=True  # Allows merging with existing directories
        )

    @staticmethod
    def save_html(html_content, output_name):
        """
        Saves the rendered HTML content to a specified file in the 'dist' directory.

        Args:
            html_content (str): The HTML content to be saved.
            output_name (str): The name of the output HTML file (including path if necessary).
        """
        output_path = os.path.join(
            'dist', output_name)  # Full path for the output file
        with open(output_path, 'w', encoding='utf-8') as output_file:
            # Write the HTML content to the file
            output_file.write(html_content)
