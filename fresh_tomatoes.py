import webbrowser
import os

import re
from jinja2 import Environment
from jinja2 import FileSystemLoader
from jinja2 import select_autoescape


def get_youtube_id(youtube_url):
    """
    Returns the youtube id from the youtube url
    :param youtube_url: Youtube URL
    :return: Youtube ID
    """
    youtube_id_match = re.search(
        r'(?<=v=)[^&#]+', youtube_url)
    youtube_id_match = youtube_id_match or re.search(
        r'(?<=be/)[^&#]+', youtube_url)
    youtube_id = (youtube_id_match.group(0) if youtube_id_match
                  else None)
    return youtube_id


def get_template(template_name='movies.html'):
    """
    Returns the jinja template identified by the
    template name. By convention, all templates
    should be placed in the ./templates directory.
    :param template_name: Template file name.
    :return: Jinja2 template
    """

    # Define the Jinja2 environment. Templates from the ./templates folder
    # will be available after this.
    env = Environment(
        loader=FileSystemLoader('./templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    # Add the get_youtube_id function as a Jinja2 filter.
    env.filters['youtube_id'] = get_youtube_id
    return env.get_template(template_name)


def create_movie_tiles_content(movies):
    """
    Generates HTML content by rendering movies.html template
    :param movies: List of movies to be rendered
    :return: String containing the rendered HTML
    """
    content = get_template('movies.html').render({
        'movies': movies})
    return content


def open_movies_page(movies):
    """
    Takes a list of movies and renders HTML content in the webbrowser.
    :param movies:
    :return:
    """
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Create html using the movies template.
    rendered_content = create_movie_tiles_content(movies)

    # Write the generated html to the output file
    output_file.write(rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
