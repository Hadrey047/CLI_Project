import click


@click.command()
def cli():
    first_name = click.prompt("Enter an integer", type=click.STRING, default=0)
    last_name= click.prompt("Enter another integer", type=click.STRING, default=0)
    email = click.prompt("Enter another integer", type=click.STRING, default=0)
    phone_number = click.prompt("Enter another integer", type=click.INT, default=0)
    click.echo(f"{first_name} + {last_name} + {email} + {phone_number}")


if __name__ == "__main__":
    cli()


