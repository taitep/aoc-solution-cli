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
from aoc_solution_cli import solution_pair

def solution_a(data):
    pass

def solution_b(data):
    pass

cli = solution_pair(solution_a, solution_b, day={day}, year={year})
''')
