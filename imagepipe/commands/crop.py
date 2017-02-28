import click
from PIL import Image

from ..imagepipe import cli, processor, copy_filename


@cli.command('crop')
@click.option('-b', '--border', type=int, help='Crop the image from all '
              'sides by this amount.')
@processor
def crop_cmd(images, border):
    """Crops an image from all edges."""
    for image in images:
        box = [0, 0, image.size[0], image.size[1]]

        if border is not None:
            for idx, val in enumerate(box):
                box[idx] = max(0, val - border)
            click.echo('Cropping "%s" by %dpx' % (image.filename, border))
            yield copy_filename(image.crop(box), image)
        else:
            yield image


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