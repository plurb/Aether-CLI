import click
from colorama import Fore


@click.command
@click.argument('kind', default="")
def create(kind: str) -> None:
    """
    Create a new item.

    :param kind: the type of item to create
    :return:
    """

    match kind:
        case "spell":
            create_spell()
        case "exploit":
            create_exploit()
        case "feat":
            create_feat()


def create_spell() -> None:
    """
    Create a new spell.

    :return:
    """

    spell_name = input("Spell name: ")
    spell_level = int(input("Spell level: "))

    while spell_level not in range(1, 10):
        spell_level = int(input("Spell level: "))

    spell_school = input("Spell school: ")
    spell_casting_time = input("Casting time: ")
    spell_range = input("Spell range: ")
    spell_components = input("Spell components: ")
    spell_duration = input("Spell duration: ")

    click.echo(Fore.GREEN + "Creating spell")

    click.echo(f"""
### {spell_name}
*{spell_level}{"st" if spell_level == 1 else "th"}-Level Spell ({spell_school})*  
**Casting Time:** {spell_casting_time}  
**Range:** {spell_range}  
**Components:** {spell_components}  
**Duration:** {spell_duration}  
    """)


def create_exploit() -> None:
    """
    Create a new exploit.

    :return:
    """

    click.echo("Creating exploit")


def create_feat() -> None:
    """
    Create a new feat.

    :return:
    """

    click.echo("Creating feat")
