# -*- coding: utf-8 -*-
from __future__ import absolute_import
import sys, queue, random
from collections import namedtuple

try:
    pass
except ImportError:
    pass

DEFAULT_NUMBER_OF_TAXIS = 3
DEFAULT_END_TIME = 180
SEARCH_DURATION = 5
TRIP_DURATION = 20
DEPARTURE_INTERVAL = 5
# time是事件发生时的仿真时间，proc出租车实例编号，action活动描述
Event = namedtuple('Event', 'time proc action')


def taxi_process(ident, trips, start_time=0):
    """每次改变状态时创建事件，把控制权让给仿真器"""
    time = yield Event(start_time, ident, 'leave garage')
    for i in range(trips):
        time = yield Event(time, ident, 'pick up passenger')
        time = yield Event(time, ident, 'drop off passenger')

    yield Event(time, ident, 'going home')


def compute_duration(previous_action):
    if previous_action in ['leave garage', 'drop off passenger']:
        interval = SEARCH_DURATION
    elif previous_action == 'pick up passenger':
        interval = TRIP_DURATION
    elif previous_action == 'going home':
        interval = 1
    else:
        raise ValueError('Unknown previous_action: %s' % previous_action)
    return int(random.expovariate(1/interval)) + 1


class Simulator:

    def __init__(self, procs_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(procs_map)

    def run(self, end_time):
        """排定并吸纳时事件， 直到时间结束"""
        # 预激
        for _, proc in sorted(self.procs.items()):
            first_event = next(proc)
            self.events.put(first_event)

        sim_time = 0
        while sim_time < end_time:
            if self.events.empty():
                print('*** end of events ***')
                break

            current_event = self.events.get()
            sim_time, proc_id, previous_action = current_event
            print('taxi: ', proc_id, proc_id * '    ', current_event)
            active_proc = self.procs[proc_id]
            next_time = sim_time + compute_duration(previous_action)
            try:
                next_event = active_proc.send(next_time)
            except StopIteration:
                del self.procs[proc_id]
            else:
                self.events.put(next_event)
        else:
            msg = '*** end of simulation time: {} events pending ***'
            print(msg.format(self.events.qsize()))

# num_taxis = 3
# taxis = {i: taxi_process(i, (i + 1)*2, i * DEPARTURE_INTERVAL) for i in range(num_taxis)}
# sim = Simulator(taxis)
def main(end_time=DEFAULT_END_TIME, num_taxixs=DEFAULT_NUMBER_OF_TAXIS, seed=None):
    """Initialize random generator, build procs and run simulation"""
    if seed is not None:
        random.seed(seed)

    taxis = {i: taxi_process(i, (i + 1)*2, i * DEPARTURE_INTERVAL) for i in range(num_taxixs)}
    sim = Simulator(taxis)
    sim.run(end_time)


if __name__ == '__main__':
    main()