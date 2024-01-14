from jinja2 import Environment, FileSystemLoader
from storage import Storage


class SiteRenderer:
    def __init__(self, template_dir='html'):
        self.env = Environment(loader=FileSystemLoader(template_dir))
        self.output_dir = 'dist'

    def render_template(self, template_name, variables, output_name):
        template = self.env.get_template(template_name)
        html_result = template.render(variables)

        Storage.save_html(html_result, output_name)

    def render_site(self, page, variables):    
        self.render_template(page + '.html', variables, page + '.html')
