import click
from wynn.create import create


@click.group(help="")
def aether():
    pass


if __name__ == '__main__':
    aether.add_command(create.create)

    aether()

