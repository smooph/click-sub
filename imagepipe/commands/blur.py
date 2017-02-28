import click
from PIL import ImageFilter

from ..imagepipe import cli, processor, copy_filename


@cli.command('blur')
@click.option('-r', '--radius', default=2, show_default=True,
              help='The blur radius.')
@processor
def blur_cmd(images, radius):
    """Applies gaussian blur."""
    blur = ImageFilter.GaussianBlur(radius)
    for image in images:
        click.echo('Blurring "%s" by %dpx' % (image.filename, radius))
        yield copy_filename(image.filter(blur), image)


