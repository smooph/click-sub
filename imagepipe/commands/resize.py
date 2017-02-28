import click

from ..imagepipe import cli, processor


@cli.command('resize')
@click.option('-w', '--width', type=int, help='The new width of the image.')
@click.option('-h', '--height', type=int, help='The new height of the image.')
@processor
def resize_cmd(images, width, height):
    """Resizes an image by fitting it into the box without changing
    the aspect ratio.
    """
    for image in images:
        w, h = (width or image.size[0], height or image.size[1])
        click.echo('Resizing "%s" to %dx%d' % (image.filename, w, h))
        image.thumbnail((w, h))
        yield image
