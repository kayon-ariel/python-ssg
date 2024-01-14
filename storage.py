import shutil
import os


class Storage:
    def create_dist_folder():
        if not os.path.exists('dist'):
            os.makedirs('dist')


    def copy_assets():
        shutil.copytree(os.path.join('html', 'assets'), os.path.join('dist', 'assets'), dirs_exist_ok=True)


    def save_html(html_content, output_name):
        output_path = os.path.join('dist', output_name)
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(html_content)