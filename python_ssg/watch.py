from python_ssg.site_renderer import SiteRenderer
from python_ssg.api_client import APIClient
from python_ssg.storage import Storage
import multiprocessing
import time
import json


def load_config(config_path):
    """
    Load the configuration from a JSON file.

    Args:
        config_path (str): The file path to the configuration JSON file.

    Returns:
        dict: The configuration data loaded from the JSON file.
    """
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
    return config


def render_page(page_name, page_info):
    while True:
        try:
            # Load API configuration and rendering variables
            api_config = page_info.get('api', {})
            page_variables = page_info.get('variables', {})
            render_interval = page_info.get('render_interval', 60)

            # Fetch data from the API
            # Change this line to use APIClient
            api_data = APIClient.fetch_data(api_config)

            # Combine API data and page variables
            combined_variables = {**api_data, **page_variables}

            # Create a SiteRenderer instance and render the page
            renderer = SiteRenderer()
            renderer.render_site(page_name, combined_variables)

            print(
                f"Waiting for {render_interval} seconds before the next render of {page_name}...")
            # Wait for the specified interval before re-rendering
            time.sleep(render_interval)
        except Exception as e:
            # Handle rendering errors
            print(f"Error rendering {page_name}: {e}")


def start_rendering(config_path):
    """
    Start the rendering process for all pages defined in the configuration.

    Args:
        config_path (str): The file path to the configuration JSON file.
    """
    # Create necessary directories and copy assets
    Storage.create_dist_folder()
    Storage.copy_assets()

    # Load the configuration
    config = load_config(config_path)
    pages = config.get('pages', {})  # Get page configurations

    processes = []  # List to keep track of processes

    # Start a separate process for each page to be rendered
    for page_name, page_info in pages.items():
        process = multiprocessing.Process(
            target=render_page, args=(page_name, page_info))
        processes.append(process)
        process.start()  # Start the rendering process for the page

    # Wait for all rendering processes to finish
    for process in processes:
        process.join()
