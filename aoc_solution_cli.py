import click
from typing import Callable
from aocd import get_data, submit

def solution_pair(solution_a: Callable[[list[str]], int], solution_b: Callable[[list[str]], int], year=None, day=None):
    @click.group
    def solution_cli():
        pass

    @solution_cli.command
    @click.option('--submit/--no-submit', 'submit_attempt', default=False, help='Submit the answer')
    @click.option('--data', default='', help='If provided, uses this data instead of fetching from servers')
    @click.option('--show-output/--hide-output', default=True, help='Print result to stdout')
    def a(submit_attempt, data, show_output):
        answer = solution_a((data or get_data(day=day, year=year)).strip().splitlines())
        if submit_attempt:
            if not data: submit(answer, day=day, year=year, part='a')
            else:
                print("Can not upload answer based on custom data.")
                exit(1)
        if show_output: print(f'Result: {answer}')
        return answer
    
    @solution_cli.command
    @click.option('--submit/--no-submit', 'submit_attempt', default=False, help='Submit the answer')
    @click.option('--data', default='', help='If provided, uses this data instead of fetching from servers')
    @click.option('--show-output/--hide-output', default=True, help='Print result to stdout')
    def b(submit_attempt, data, show_output):
        answer = solution_b((data or get_data(day=day, year=year)).strip().splitlines())
        if submit_attempt:
            if not data: submit(answer, day=day, year=year, part='b')
            else:
                print("Can not upload answer based on custom data.")
                exit(1)
        if show_output: print(f'Result: {answer}')
        return answer
    
    return solution_cli
