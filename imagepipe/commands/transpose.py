import click

from ..imagepipe import cli, processor, copy_filename


@cli.command('transpose')
@click.option('-r', '--rotate', callback=convert_rotation,
              help='Rotates the image (in degrees)')
@click.option('-f', '--flip', callback=convert_flip,
              help='Flips the image  [LR / TB]')
@processor
def transpose_cmd(images, rotate, flip):
    """Transposes an image by either rotating or flipping it."""
    for image in images:
        if rotate is not None:
            mode, degrees = rotate
            click.echo('Rotate "%s" by %ddeg' % (image.filename, degrees))
            image = copy_filename(image.transpose(mode), image)
        if flip is not None:
            mode, direction = flip
            click.echo('Flip "%s" %s' % (image.filename, direction))
            image = copy_filename(image.transpose(mode), image)
        yield image