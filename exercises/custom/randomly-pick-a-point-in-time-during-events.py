Problem: Randomly Pick a Point in Time During Events
Given a list of events, each represented by an interval [start, end) where start is the start time and end is the end time of the event, write a function that randomly picks a point in time during which at least one event is happening. The point chosen should be uniformly distributed, meaning every point within the events should have the same probability of being selected.

You should use the predefined random() function, which returns a random number in the range [0, 1).

Function Signature:
```
def pick_event_time(events: List[List[float]]) -> float:
    pass
```

Input:
events is a list of events where each event is represented by a list of two floating point numbers [start, end) representing the time interval for the event. The list events contains between 1 and 10^4 events, and each interval [start, end) satisfies 0 <= start < end <= 10^9.
Output:
Return a randomly picked point in time that lies within one of the events. The point should be uniformly distributed, meaning every point within the event intervals should have the same probability of being picked.
Example 1:
Input: events = [[0.0, 0.5], [3.0, 5.5], [9.0, 10.2]]
Output: 4.75
Explanation:
The event [0.0, 0.5] has a duration of 0.5.
The event [3.0, 5.5] has a duration of 2.5.
The event [9.0, 10.2] has a duration of 1.2.
The total time during which any event is happening is 4.2 (0.5 + 2.5 + 1.2). The randomly picked point should be within any of these events, for example, 4.75.
