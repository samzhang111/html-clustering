import click
from bs4 import BeautifulSoup
from suffix_tree import generate


@click.group()
def cli():
    pass

@cli.command()
@click.argument('html_file')
def score(html_file):
    with open(html_file) as f:
        soup = BeautifulSoup(f, 'html.parser')

    tags = [tag.name for tag in soup.find_all()]

    print(generate(tags))



@cli.command()
@click.argument('file1')
@click.argument('file2')
def compare(file1, file2):
    print(file1, file2)

@cli.command()
@click.argument('string')
def suffix_string(string):
    print(generate(list(string)))


if __name__ == '__main__':
    cli()
