import click
from PIL import Image, ImageFilter, ImageEnhance

from ..imagepipe import cli, processor, copy_filename

def convert_rotation(ctx, param, value):
    if value is None:
        return
    value = value.lower()
    if value in ('90', 'r', 'right'):
        return (Image.ROTATE_90, 90)
    if value in ('180', '-180'):
        return (Image.ROTATE_180, 180)
    if value in ('-90', '270', 'l', 'left'):
        return (Image.ROTATE_270, 270)
    raise click.BadParameter('invalid rotation "%s"' % value)


def convert_flip(ctx, param, value):
    if value is None:
        return
    value = value.lower()
    if value in ('lr', 'leftright'):
        return (Image.FLIP_LEFT_RIGHT, 'left to right')
    if value in ('tb', 'topbottom', 'upsidedown', 'ud'):
        return (Image.FLIP_LEFT_RIGHT, 'top to bottom')
    raise click.BadParameter('invalid flip "%s"' % value)


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