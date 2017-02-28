import click
from PIL import Image

from ..imagepipe import cli, generator


@cli.command('open')
@click.option('-i', '--image', 'images', type=click.Path(),
              multiple=True, help='The image file to open.')
@generator
def open_cmd(images):
    """Loads one or multiple images for processing.  The input parameter
    can be specified multiple times to load more than one image.
    """
    for image in images:
        try:
            click.echo('Opening "%s"' % image)
            if image == '-':
                img = Image.open(click.get_binary_stdin())
                img.filename = '-'
            else:
                img = Image.open(image)
            yield img
        except Exception as e:
            click.echo('Could not open image "%s": %s' % (image, e), err=True)