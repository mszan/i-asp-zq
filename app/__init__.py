# -*- coding: utf-8 -*-
"""Top-level package for the CLI App"""

import click
from app import commands

@click.group()
def cli():
    pass

cli.add_command(commands.hello)