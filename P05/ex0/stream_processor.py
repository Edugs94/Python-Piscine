#!/usr/bin/env python3
"""
Ex0 stream_processor
"""

from typing import Any, List
from abc import ABC, abstractmethod


def ft_len(data: Any) -> int:
    """
    Recreation of len() as do not appear as an allowed function
    """
    counter = 0
    for _ in data:
        counter += 1
    return counter


def ft_sum(data: List[int]) -> int:
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


def validate_data(data: Any, datatype: Any) -> None:
    if not isinstance(data, datatype):
        raise ValueError("Incorrect data type")


class DataProcessor(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: List[int]) -> str:
        result = (
            f"Processed {ft_len(data)} numeric values, "
            f"sum={ft_sum(data)}, avg={ft_sum(data)/ft_len(data):.1f}"
        )
        return result

    def validate(self, data: Any | list[int]) -> bool:
        try:
            if not isinstance(data, list):
                raise ValueError("Data is not a list")
            for i in data:  # type: ignore
                validate_data(i, int)
        except ValueError:
            print()
            print(
                "Validation: Data is not a List of int values."
                " Skipping numeric processor..."
            )
            return False
        return True


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: str) -> str:
        result = (
            f"Processed text: {ft_len(data)} "
            f"characters, {ft_word_count(data)} words"
        )
        return result

    def validate(self, data: str) -> bool:
        try:
            validate_data(data, str)
        except ValueError:
            print()
            print("Validation: Data is not a string. "
                  "Skipping text processor...")
            return False
        return True


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: str) -> str:
        if 'ERROR' in data:
            result = "ERROR level detected: Connection timeout"
        else:
            result = "INFO level detected: System ready"
        return result

    def validate(self, data: str) -> bool:
        try:
            validate_data(data, str)
        except ValueError:
            print()
            print("Validation: Data is not a string. "
                  "Skipping log processor...")
            return False
        return True

    def format_output(self, result: str) -> str:
        if "ERROR" in result:
            return f"[ALERT] {result}"
        else:
            return f"[INFO] {result}"


def test_proc_library() -> None:

    processor_1 = NumericProcessor()
    data: List[int] = [1, 2, 3, 4, 5]
    print()
    print("Initializing Numeric Processor...")
    print(f"Processing data: {data}")
    if processor_1.validate(data) is True:
        print("Validation: Numeric data verified")
        result = processor_1.process(data)
        print(processor_1.format_output(result))

    processor_2 = TextProcessor()
    text: str = "Hello Nexus World"
    print()
    print("Initializing Text Processor...")
    print(f'Processing data: "{text}"')
    if processor_2.validate(text) is True:
        print("Validation: Text data verified")
        result = processor_2.process(text)
        print(processor_2.format_output(result))

    processor_3 = LogProcessor()
    error: str = "ERROR: Connection timeout"
    print()
    print("Initializing Log Processor...")
    print(f'Processing data: "{error}"')
    if processor_3.validate(error) is True:
        print("Validation: Log entry verified")
        result = processor_3.process(error)
        print(processor_3.format_output(result))


def polymorphic_processing() -> None:
    print('=== Polymorphic Processing Demo ===')
    print('Processing multiple data types through same interface...')

    proc_library: List[DataProcessor] = [NumericProcessor(),
                                         TextProcessor(), LogProcessor()]
    data: List[Any] = [
        [2, 2, 2],
        "Hello Nexus ",
        "INFO: System ready"
    ]
    i = 0
    for processor in proc_library:
        if processor.validate(data[i]):
            raw_result: str = processor.process(data[i])
            formatted_result = processor.format_output(raw_result)
            clean_result: str = formatted_result.replace("Output: ", "")
            print(f"Result {i + 1}: {clean_result}")
        i += 1


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    test_proc_library()
    print()
    polymorphic_processing()
    print()
    print('Foundation systems online. Nexus ready for advanced streams.')


if __name__ == "__main__":
    main()
