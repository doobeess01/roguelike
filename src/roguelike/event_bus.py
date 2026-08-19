from collections import defaultdict, deque
from collections.abc import Callable
from dataclasses import dataclass
from typing import cast

from .event import Event


Listener = Callable[[Event], None]


@dataclass
class _Listener:
    priority: int
    callback: Listener


class EventBus:
    def __init__(self) -> None:
        self._listeners: defaultdict[type[Event], list[_Listener]] = defaultdict(list)
        self._queue: deque[Event] = deque()

    def subscribe[T: Event](
        self,
        event_type: type[T],
        callback: Callable[[T], None],
        *,
        priority: int = 0,
    ) -> None:
        """Register a listener for an event type."""
        listener = _Listener(priority, cast(Listener, callback))

        listeners = self._listeners[event_type]
        listeners.append(listener)
        listeners.sort(key=lambda listener: listener.priority)

    def emit(self, event: Event) -> None:
        """Add an event to the end of the queue."""
        self._queue.append(event)

    def process(self) -> None:
        """Process events until the queue is empty."""
        while self._queue:
            event = self._queue.popleft()

            for listener in self._listeners[type(event)]:
                listener.callback(event)
