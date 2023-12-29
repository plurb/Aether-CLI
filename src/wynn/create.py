import click


@click.command
@click.option('-type', default="")
def create(ftype: str) -> None:

    if ftype == "spell":
        create_spell()
    elif ftype == "exploit":
        create_exploit()
    elif ftype == "feat":
        create_feat()


def create_spell() -> None:
    click.echo("Creating spell")


def create_exploit() -> None:
    click.echo("Creating exploit")
    pass


def create_feat() -> None:
    click.echo("Creating feat")
    pass
