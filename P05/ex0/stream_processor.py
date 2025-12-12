"""
Ex0.stream_processor
"""

from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def process_data(self, data) -> None:
        pass


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def process_data(self, data: Any):
        print()
        print("Initializing Numeric Processor...")
        print(f"Processing data: {data}")
        try:
            validate_data(data, 'int')
        except ValueError:
            print("Validation: Data contains non numeric values. Skipping numeric processor...")
            return
        print("Validation: Numeric data verified")
        print(
            f"Output: Processed {ft_len(data)} numeric values, "
            f"sum={ft_sum(data)}, avg={ft_sum(data)/ft_len(data):.1f}"
        )


class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def process_data(self, data: Any):
        print()
        print("Initializing Text Processor...")
        print(f"Processing data: {data}")
        try:
            s = str(data)
        except ValueError:
            print("Validation: Data cannot be convertet to string. Skipping text processor...")
            return
        print("Validation: Text data verified")
        print(
            f"Output: Processed text: {ft_len(data)} "
            f"characters, {ft_word_count(data)} words"
        )


class LogProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def process_data(data: Any):
        print()
        print("Initializing Log Processor...")
        print(f"Processing data: {str(data)}")
        print("Validation: Log entry verified")
        print("Output: [ALERT] ERROR level detected: Connection timeout")


def validate_data(data: Any, datatype: str):
    if not isinstance(data, datatype):
        raise ValueError("Incorrect data type")




def ft_len(data: Any) -> int:
    """
    Recreation of len() as do not appear as an allowed function
    """
    counter = 0
    for _ in data:
        counter += 1
    return counter


def ft_sum(data: List[Union[int, float]]) -> Union[int, float]:
    """
    Recreation of sum() as do not appear as an allowed function
    """
    total = 0
    for number in data:
        total += number
    return total


def ft_word_count(text: str) -> int:
    """
    Words counter in a string
    """
    count = 0
    in_word = False

    for char in text:
        if char != " ":
            if not in_word:
                count += 1
                in_word = True
        else:
            in_word = False

    return count


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    a = NumericProcessor()
    a.process_data(1, a)

    """number = NumericProcessor()
    number.process_data([5, 7, 8])

    text = TextProcessor('Hello Nexus World')
    text.process_data()

    log = LogProcessor('ERROR: Connection timeout')
    log.process_data()"""


if __name__ == "__main__":
    main()


"""
=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===

Initializing Numeric Processor...
Processing data: [1, 2, 3, 4, 5]
Validation: Numeric data verified
Output: Processed 5 numeric values, sum=15, avg=3.0

Initializing Text Processor...
Processing data: "Hello Nexus World"
Validation: Text data verified
Output: Processed text: 17 characters, 3 words

Initializing Log Processor...
Processing data: "ERROR: Connection timeout"
Validation: Log entry verified
Output: [ALERT] ERROR level detected: Connection timeout

=== Polymorphic Processing Demo ===

Processing multiple data types through same interface...
Result 1: Processed 3 numeric values, sum=6, avg=2.0
Result 2: Processed text: 12 characters, 2 words
Result 3: [INFO] INFO level detected: System ready

Foundation systems online. Nexus ready for advanced streams.
"""
