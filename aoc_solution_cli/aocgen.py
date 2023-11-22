import click
from recent_problem_saver import get_recent, day_to_module

@click.command
@click.option('--day', type=int)
@click.option('--year', type=int)
def generate(day, year):
    day, year = get_recent(day, year)
    file = f"{day_to_module(day, year)}.py"
    with open(file, 'w') as f:
        f.write(f'''\
def solution_a(data):
    pass

def solution_b(data):
    pass
''')
