import click
from PIL import ImageEnhance

from ..imagepipe import cli, processor, copy_filename


@cli.command('sharpen')
@click.option('-f', '--factor', default=2.0,
              help='Sharpens the image.', show_default=True)
@processor
def sharpen_cmd(images, factor):
    """Sharpens an image."""
    for image in images:
        click.echo('Sharpen "%s" by %f' % (image.filename, factor))
        enhancer = ImageEnhance.Sharpness(image)
        yield copy_filename(enhancer.enhance(max(1.0, factor)), image)
