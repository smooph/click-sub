import click

from ..imagepipe import cli, processor


@cli.command('display')
@processor
def display_cmd(images):
    """Opens all images in an image viewer."""
    for image in images:
        click.echo('Displaying "%s"' % image.filename)
        image.show()
        yield image


