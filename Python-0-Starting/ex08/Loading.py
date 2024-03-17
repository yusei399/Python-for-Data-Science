import sys
import time
from time import sleep

def ft_tqdm(lst):
    start_time = time.time()
    total = len(lst)
    def print_progress_bar(iteration):
        elapsed_time = time.time() - start_time
        percent = ("{0:.1f}").format(100 * (iteration / float(total)))
        filled_length = int(50 * iteration // total)
        bar = "=" * filled_length + '>' + '-' * (50 - filled_length)
        sys.stdout.write(f'\r{percent}% |{bar}| {iteration}/{total} ')
        sys.stdout.flush()
    for i, item in enumerate(lst):
        yield item
        print_progress_bar(i + 1)
    print()

for elem in ft_tqdm(range(333)):
    sleep(0.005)
