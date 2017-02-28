import click

from ..imagepipe import cli, processor


@cli.command('paste')
@click.option('-l', '--left', default=0, help='Offset from left.')
@click.option('-r', '--right', default=0, help='Offset from right.')
@processor
def paste_cmd(images, left, right):
    """Pastes the second image on the first image and leaves the rest
    unchanged.
    """
    imageiter = iter(images)
    image = next(imageiter, None)
    to_paste = next(imageiter, None)

    if to_paste is None:
        if image is not None:
            yield image
        return

    click.echo('Paste "%s" on "%s"' %
               (to_paste.filename, image.filename))
    mask = None
    if to_paste.mode == 'RGBA' or 'transparency' in to_paste.info:
        mask = to_paste
    image.paste(to_paste, (left, right), mask)
    image.filename += '+' + to_paste.filename
    yield image

    for image in imageiter:
        yield image
