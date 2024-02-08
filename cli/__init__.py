# -*- coding: utf-8 -*-
"""Top-level package for the CLI App"""

import click
from cli import commands

@click.group(help="A CLI app that predicts the weather. Use [COMMAND] --help for more information.")
def cli():
    pass

cli.add_command(commands.predict)