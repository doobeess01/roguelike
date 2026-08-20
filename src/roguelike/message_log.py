from .text import Text


class Message:
    def __init__(self, text: Text):
        self.text = text
        self.count = 1
    def __eq__(self, other: object):
        if isinstance(other, Message):
            return self.text == other.text
        return False
    @property
    def text_with_count(self):
        if self.count > 1:
            return Text(self.text.text + f' (x{self.count})', self.text.fg, self.text.bg)
        return self.text


class MessageLog:
    def __init__(self):
        self.messages: list[Message] = []

    def log(self, text: str, fg: tuple[int,int,int] = (255,255,255), bg: tuple[int,int,int] = (0,0,0)):
        message = Message(Text(text, fg=fg, bg=bg))
        if self.messages:
            if message == self.messages[-1]:
                self.messages[-1].count += 1
                return
        self.messages.append(message)

    def get_messages(self, rows: int):
        n_messages = len(self.messages)
        return self.messages[n_messages-rows:] if rows < n_messages else self.messages