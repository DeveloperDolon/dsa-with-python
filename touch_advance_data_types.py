import arrow;

brewing_time = arrow.utcnow();
brewing_time.to('Europe/Rome');
print(brewing_time.datetime);

from collections import namedtuple;

chaiProfile = namedtuple('chaiProfile', ['flavor', 'aroma']);

print(f'Chai profile: {chaiProfile.__doc__}');

