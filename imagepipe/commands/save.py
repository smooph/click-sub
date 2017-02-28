import click

from ..imagepipe import cli, processor


@cli.command('save')
@click.option('--filename', default='processed-%04d.png', type=click.Path(),
              help='The format for the filename.',
              show_default=True)
@processor
def save_cmd(images, filename):
    """Saves all processed images to a series of files."""
    for idx, image in enumerate(images):
        try:
            fn = filename % (idx + 1)
            click.echo('Saving "%s" as "%s"' % (image.filename, fn))
            yield image.save(fn)
        except Exception as e:
            click.echo('Could not save image "%s": %s' %
                       (image.filename, e), err=True)


