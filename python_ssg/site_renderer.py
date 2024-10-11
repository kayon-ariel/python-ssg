from jinja2 import Environment, FileSystemLoader
from python_ssg.storage import Storage


class SiteRenderer:
    """
    A class responsible for rendering HTML templates using Jinja2.

    Attributes:
        env (jinja2.Environment): The Jinja2 environment for loading templates.
        output_dir (str): The directory where rendered HTML files will be saved.
    """

    def __init__(self, template_dir='html'):
        """
        Initializes the SiteRenderer with the specified template directory.

        Args:
            template_dir (str): The directory containing the HTML templates. Defaults to 'html'.
        """
        self.env = Environment(loader=FileSystemLoader(
            template_dir))  # Load templates from the specified directory
        self.output_dir = 'dist'  # Set the output directory for rendered HTML files

    def render_template(self, template_name, variables, output_name):
        """
        Renders a specific template with the given variables and saves the output.

        Args:
            template_name (str): The name of the template file (must include .html).
            variables (dict): A dictionary of variables to pass to the template during rendering.
            output_name (str): The name of the output HTML file (including path if necessary).
        """
        # Load the specified template
        template = self.env.get_template(template_name)
        # Render the template with the provided variables
        html_result = template.render(variables)

        # Save the rendered HTML to the specified output file
        Storage.save_html(html_result, output_name)

    def render_site(self, page, variables):
        """
        Renders a site page using the corresponding HTML template.

        Args:
            page (str): The name of the page (without .html) to render.
            variables (dict): A dictionary of variables to pass to the template during rendering.
        """
        # Call render_template to render the page's HTML file
        self.render_template(page + '.html', variables, page + '.html')
