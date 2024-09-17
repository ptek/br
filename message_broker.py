from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, List, Callable
from datetime import datetime

class MessageType(Enum):
    INFO = auto()
    WARNING = auto()
    ERROR = auto()
    DEBUG = auto()

@dataclass
class Message:
    timestamp: datetime
    channel: str
    conversation_id: str
    message_type: MessageType
    content: str

class MessageBroker:
    def __init__(self):
        self.subscribers: Dict[str, List[Callable[[Message], None]]] = {}

    def publish(self, message: Message):
        if message.channel in self.subscribers:
            for subscriber in self.subscribers[message.channel]:
                subscriber(message)

    def subscribe(self, channel: str, callback: Callable[[Message], None]):
        if channel not in self.subscribers:
            self.subscribers[channel] = []
        self.subscribers[channel].append(callback)
