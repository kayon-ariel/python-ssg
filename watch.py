import multiprocessing
import time
import json
from storage import Storage
from site_renderer import SiteRenderer
import requests


def load_config():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    return config


def fetch_data_from_api(api_config):
    api_url = api_config.get('url', '')
    api_method = api_config.get('method', 'GET')
    api_params = api_config.get('params', {})

    response = requests.request(api_method, api_url, params=api_params)

    if response.status_code == 200:
        return response.json()
    else:
        return {}


def render_page(page_name, page_info):
    while True:
        api_config = page_info.get('api', {})
        page_variables = page_info.get('variables', {})
        render_interval = page_info.get('render_interval', 60)

        api_data = fetch_data_from_api(api_config)

        combined_variables = {**api_data, **page_variables}

        renderer = SiteRenderer()
        renderer.render_site(page_name, combined_variables)

        print(
            f"Waiting for {render_interval} seconds before the next render of {page_name}...")
        time.sleep(render_interval)


if __name__ == "__main__":
    Storage.create_dist_folder()
    Storage.copy_assets()

    config = load_config()
    pages = config.get('pages', {})

    processes = []

    for page_name, page_info in pages.items():
        process = multiprocessing.Process(
            target=render_page, args=(page_name, page_info))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
