import click
from typing import Callable
from aocd import get_data, submit

def solution_pair(solution_a: Callable[[list[str]], int], solution_b: Callable[[list[str]], int], year=None, day=None):
    @click.group
    def solution_cli():
        pass

    @solution_cli.command
    @click.option('--submit/--no-submit', 'submit_attempt', default=False, help='Submit the answer')
    def a(submit_attempt):
        answer = solution_a(get_data(day=day, year=year))
        if submit_attempt: submit(answer, day=day, year=year, part='a')
    
    @solution_cli.command
    @click.option('--submit/--no-submit', 'submit_attempt', default=False, help='Submit the answer')
    def b(submit_attempt):
        answer = solution_b(get_data(day=day, year=year))
        if submit_attempt: submit(answer, day=day, year=year, part='b')
    
    return solution_cli
