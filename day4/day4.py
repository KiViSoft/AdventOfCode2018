"""
guard - { id: int
          work_days: int
          minutes_asleep: []
        }
"""
import re

class Guard(object):
    def __init__(self, guard_id):
        self.id = guard_id
        self.workdays = 1
        self.minutes_asleep = []

    def __repr__(self):
        return str(self.id)

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return len(self.minutes_asleep) < len(other.minutes_asleep)

guards = []
regex_id = re.compile('[0-9]+')

# part 1

with open('input.txt', 'r') as f:
    input_lines = f.readlines()
    input_lines.sort()
    list_iter = iter(input_lines)

    while True:
        try:
            line = next(list_iter)
            if 'Guard' in line:
                tmp = Guard(regex_id.findall(line)[-1])
                if tmp not in guards:
                    guards.append(tmp)
                    latest_guard = guards[-1]
                else:
                    latest_guard = guards[guards.index(tmp)]
                    latest_guard.workdays += 1
                pass
            elif 'falls' in line:
                    start = regex_id.findall(line)[-1]
            elif 'wakes' in line:
                    end = regex_id.findall(line)[-1]
                    for minute in range(int(start), int(end)):
                        latest_guard.minutes_asleep.append(minute)
        except StopIteration:
            break

guards.sort(reverse=True)
worst_guard = guards[0]
print(int(worst_guard.id) * max(worst_guard.minutes_asleep, key=worst_guard.minutes_asleep.count))

# part 2
freq_max = 0
most_freq = 0
guard_id = 0

for guard in guards:
    try:
        most_frequently_asleep = max(guard.minutes_asleep, key=guard.minutes_asleep.count)
        frequency = guard.minutes_asleep.count(most_frequently_asleep)
        if frequency > freq_max:
            freq_max = frequency
            most_freq = most_frequently_asleep
            guard_id = int(guard.id)
    except ValueError:
        pass

print(guard_id * most_freq)

