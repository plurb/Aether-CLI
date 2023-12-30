import click


@click.command
@click.argument('kind', default="")
def create(kind: str) -> None:

    if kind == "spell":
        create_spell()
    elif kind == "exploit":
        create_exploit()
    elif kind == "feat":
        create_feat()


def create_spell() -> None:
    spell_name = input("Spell name: ")
    spell_level = int(input("Spell level: "))

    while spell_level not in range(1, 10):
        spell_level = int(input("Spell level: "))

    spell_school = input("Spell school: ")
    spell_casting_time = input("Casting time: ")
    spell_range = input("Spell range: ")
    spell_components = input("Spell components: ")
    spell_duration = input("Spell duration: ")

    click.echo("Creating spell")

    click.echo(f"""
### {spell_name}
*{spell_level}{"st" if spell_level == 1 else "th"}-Level Spell ({spell_school})*  
**Casting Time:** {spell_casting_time}  
**Range:** {spell_range}  
**Components:** {spell_components}  
**Duration:** {spell_duration}  
    """)


def create_exploit() -> None:
    click.echo("Creating exploit")


def create_feat() -> None:
    click.echo("Creating feat")
