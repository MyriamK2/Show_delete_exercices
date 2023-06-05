import django
django.setup()

from members.seed import run
from cars.seed import run

if __name__ == '__main__':
    run()