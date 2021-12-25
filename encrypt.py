import click
from caesar import encrypt_cesar


@click.command()
@click.option('--text', prompt='Your text',
              help='The text you want to encrypt')
@click.option('--key', default=2, help='key for encryption')
@click.option('--ke', default=2, help='key for encryption')
@click.argument('algo')
def encrypt(text, key,algo,ke):
    cypher='no algorithm was chosen'
    if(algo=="caesar"):
        cypher=encrypt_cesar(text,key)
    click.echo(cypher)


if __name__ == '__main__':
    encrypt()