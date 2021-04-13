import click


@click.command()
@click.argument("globs", nargs=-1)
def minimize(globs):
    globs = globs or "./**"
    print(f"Minimizing {globs}")


if __name__ == "__main__":
    minimize()
