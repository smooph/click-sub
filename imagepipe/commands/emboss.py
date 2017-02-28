import click
from PIL import ImageFilter

from ..imagepipe import cli, processor, copy_filename


@cli.command('emboss')
@processor
def emboss_cmd(images):
    """Embosses an image."""
    for image in images:
        click.echo('Embossing "%s"' % image.filename)
        yield copy_filename(image.filter(ImageFilter.EMBOSS), image)
