from dataclasses import dataclass


@dataclass
class Message:
    text: str
    fg: tuple[int,int,int] = (255,255,255)
    bg: tuple[int,int,int] = (0,0,0)


class MessageLog:
    def __init__(self):
        self.messages: list[Message] = []

    def log(self, text: str, fg: tuple[int,int,int] = (255,255,255), bg: tuple[int,int,int] = (0,0,0)):
        self.messages.append(Message(text, fg, bg))

    def get_messages(self, rows: int):
        n_messages = len(self.messages)
        return self.messages[n_messages-rows:] if rows < n_messages else self.messages