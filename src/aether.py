import click
from wynn import create


@click.group(help="")
def aether():
    pass


if __name__ == '__main__':
    aether.add_command(create.create)

    aether()

