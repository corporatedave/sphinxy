from dataclasses import dataclass
from typing import Iterator


@dataclass(frozen=True)
class Riddle:
    question: str
    answer: str
    """_summary_
    """
    def check_answer(self, answer: str) -> bool:
        return answer.lower() == self.answer.lower()
        """_summary_
        """
    def get_hint(self) -> Iterator[str]:
        yield from iter(self.answer)
        """_summary_
        """