#!/usr/bin/python

class Clock:
    def __init__(self, clock_type):
        if clock_type == "NCAA Regular":
            self._game_clock = 20*60
        elif clock_type == "NCAA Overtime":
            self._game_clock = 5*60
        else:
            print "We only support NCAA clocks for now"
            assert 0
        self._status = "prepare"
        
    def start(self):
        assert self._status == "prepare"
        self._status = "in progress"
        
    def consume(self, clock):
        assert self._status == "in progress"
        self._game_clock -= clock
        if self._game_clock < 0:
            self._status = "finished"

    def getClock(self):
        if self._game_clock < 0:
            self._game_clock = 0
        return "["+str(self._game_clock / 60)+":"+str(self._game_clock % 60)+"]"

    def isFinished(self):
        return self._status == "finished"
