from collections import namedtuple

AoCDay = namedtuple('AoCDay', ['day', 'year'])

def get_recent(day=None, year=None, file='.recent_problem'):
    try:
        with open(file, 'r') as f:
                savedyear, savedday = tuple([int(i) for i in f.read().strip().split(' ')])
                if len(pair) != 2:
                    print(f"File '{file}' is not formatted correctly")
    except FileNotFoundError:
        savedday, savedyear = None, None
    
    if not day or not year:
        if not day: day = savedday
        if not year: year = savedyear

    if (day, year) != (savedday, savedyear):
        with open(file, 'w') as f:
            f.write(f"{day, year}")
    
    return AoCDay(day, year)


day_to_module = lambda day, year: f'aoc_{year}_{day}'
