#!/usr/bin/env python3
"""
Ex1 data_stream
"""

from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


def ft_len(data: Any) -> int:
    """
    Recreation of len() as do not appear as an allowed function
    """
    counter: int = 0
    for _ in data:
        counter += 1
    return counter


def ft_sum(data: List[Union[int, float]]) -> Union[int, float]:
    """
    Recreation of sum() as do not appear as an allowed function
    """
    total: Union[int, float] = 0
    for number in data:
        total += number
    return total


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        """Class initializer"""
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Processes batch"""
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Gets Stream info"""
        return {"stream_id": self.stream_id, "type": "Unknown type Data"}

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        """Filters data based on optional criteria"""
        return data_batch


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        """Class initializer"""
        super().__init__(stream_id)

    def validate_data(self, data_batch: List[Any]) -> bool:
        """Checks if data represents valid sensor readings (str, number)."""
        try:
            if not isinstance(data_batch, list):  # type: ignore
                return False
            for item in data_batch:
                if not isinstance(item, (tuple, list)):
                    return False
                if ft_len(item) < 2:
                    return False
                if not isinstance(item[0], str):
                    return False
                if not isinstance(item[1], (int, float)):
                    return False
            return True
        except Exception:
            return False

    def process_batch(self, data_batch: List[Any]) -> str:
        """Processes batch"""
        count: int = ft_len(data_batch)
        return f"Sensor data: {count} readings processed"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Gets Stream info"""
        return {"stream_id": self.stream_id, "type": "Environmental Data"}

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        """Filters data based on optional criteria"""
        if criteria == "high_priority":
            filtered: List[tuple[str, float]] = [
                x
                for x in data_batch
                if (x[0] == "temp" and x[1] > 50)
                or (x[0] == "humidity" and x[1] > 70)
                or (x[0] == "pressure" and x[1] > 1300)
            ]
            return filtered
        else:
            return data_batch

    def avg_temp(self, data_batch: List[Any]) -> float:
        """Calculates average temperature"""
        temps: List[float] = [
            x[1]
            for x in data_batch
            if isinstance(x, (tuple, list)) and
            ft_len(x) >= 2 and x[0] == "temp"
        ]
        if not temps:
            return 0.0
        return ft_sum(temps) / ft_len(temps)


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        """Class initializer"""
        super().__init__(stream_id)

    def validate_data(self, data_batch: List[Any]) -> bool:
        """Checks if data represents valid operations (buy/sell, int)."""
        try:
            if not isinstance(data_batch, list):  # type: ignore
                return False
            for item in data_batch:
                if not isinstance(item, (tuple, list)):
                    return False
                if ft_len(item) < 2:
                    return False
                if not isinstance(item[0], str):
                    return False
                if not isinstance(item[1], int):
                    return False
                if item[0] not in ['buy', 'sell']:
                    return False
            return True
        except Exception:
            return False

    def process_batch(self, data_batch: List[Any]) -> str:
        """Processes batch"""
        count: int = ft_len(data_batch)
        return f"Transaction data: {count} operations processed"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Gets Stream info"""
        return {"stream_id": self.stream_id, "type": "Financial Data"}

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        """Filters data based if a transaction is higher than 150"""
        if criteria == "high_priority":
            filtered: List[Any] = [
                x
                for x in data_batch
                if x[1] > 150
            ]
            return filtered
        else:
            return data_batch

    def net_flow(self, data_batch: List[Any]) -> int:
        """Calculates net flow considering buy to be positive"""
        values: List[Union[int, float]] = [
            x[1] if x[0] == 'buy' else -x[1]
            for x in data_batch
        ]
        flow: int = int(ft_sum(values))
        return flow


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        """Class initializer"""
        super().__init__(stream_id)

    def validate_data(self, data_batch: List[Any]) -> bool:
        """Checks if data represents valid events (strings)"""
        try:
            if not isinstance(data_batch, list):  # type: ignore
                return False

            for item in data_batch:
                if not isinstance(item, str):
                    return False
                if not item:
                    return False
            return True
        except Exception:
            return False

    def process_batch(self, data_batch: List[Any]) -> str:
        """Processes batch and counts errors"""
        count: int = ft_len(data_batch)

        return f"Event analysis: {count} events processed"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Gets Stream info"""
        return {"stream_id": self.stream_id, "type": "System Events"}

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        """Filters data based on criteria."""
        if criteria == "high_priority":
            filtered: List[Any] = [
                x for x in data_batch
                if x == 'error'
            ]
            return filtered
        else:
            return data_batch


class StreamProcessor:
    def __init__(self) -> None:
        """Class initializer"""
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream):
        """Adds stream to processor"""
        self.streams.append(stream)

    def process_streams(self, data_map: Dict[str, List[Any]]):
        """
        Process stream batch
        """
        print("Batch 1 Results:")
        for stream in self.streams:
            stats: Dict[str, Union[str, int, float]] = stream.get_stats()
            stream_id: str = str(stats['stream_id'])
            data: List[Any] = data_map.get(stream_id)  # type: ignore
            if data:
                result: str = stream.process_batch(data)
                print(f"- {result}")

    def report_filtered_results(self, data_map: Dict[str, List[Any]],
                                criteria: str):
        """Applies filter and gets requested report."""
        print()
        print("Stream filtering active: High-priority data only")

        report_parts: List[str] = []

        for stream in self.streams:
            stats: Dict[str, Union[str, int, float]] = stream.get_stats()
            stream_id: str = str(stats['stream_id'])
            data: List[Any] = data_map.get(stream_id)  # type: ignore

            if data:
                filtered_data: List[Any] = stream.filter_data(data, criteria)
                count: int = len(filtered_data)

                if count > 0:
                    if isinstance(stream, SensorStream):
                        report_parts.append(f"{count} critical sensor alerts")
                    elif isinstance(stream, TransactionStream):
                        report_parts.append(f"{count} large transaction")
                    elif isinstance(stream, EventStream):
                        report_parts.append(f"{count} critical events")

        print("Filtered results: ", end="")
        print(*report_parts, sep=", ")
        print("All streams processed successfully. Nexus throughput optimal")


def separate_streams():
    """Demonstrates separate stream processing"""
    print()
    stream_sensor: SensorStream = SensorStream("SENSOR_001")
    sensor_data: List[tuple[str, float]] = [
        ("temp", 22.5),
        ("humidity", 65),
        ("pressure", 1013),
        ("temp", 23.5),
    ]
    print("Initializing Sensor Stream...")
    if stream_sensor.validate_data(sensor_data) is False:
        print("Error while reading Sensor Stream Data... "
              "Shutting down the system")
        return
    stats: Dict[str, Union[str, int, float]] = stream_sensor.get_stats()
    print(f"Stream ID: {stats['stream_id']}, Type: {stats['type']}")
    print("Processing sensor batch: [", end="")
    i: int = 0
    for key, value in sensor_data:
        if i != ft_len(sensor_data) - 1:
            print(f"{key}:{value}, ", end="")
        else:
            print(f"{key}:{value}]")
        i += 1
    print(
        f"Sensor analysis: {ft_len(sensor_data)} readings processed, "
        f"avg temp: {stream_sensor.avg_temp(sensor_data)}"
    )

    print()
    stream_finance: TransactionStream = TransactionStream("TRANS_001")
    finance_data: List[tuple[str, int]] = [
        ("buy", 100),
        ("sell", 150),
        ("buy", 75)
    ]
    print("Initializing Transaction Stream...")
    if stream_finance.validate_data(finance_data) is False:
        print("Error while reading Transaction Data... "
              "Shutting down the system")
        return
    stats = stream_finance.get_stats()
    print(f"Stream ID: {stats['stream_id']}, Type: {stats['type']}")
    print("Processing transaction batch: [", end="")
    i = 0
    for key, value in finance_data:
        if i != ft_len(finance_data) - 1:
            print(f"{key}:{value}, ", end="")
        else:
            print(f"{key}:{value}]")
        i += 1

    net_flow: int = stream_finance.net_flow(finance_data)
    print(
        f"Transaction analysis: {ft_len(finance_data)} operations, ", end='')
    if net_flow >= 0:
        print(f"net flow: {net_flow}")
    else:
        print(f"net flow: -{net_flow}")

    print()
    stream_event: EventStream = EventStream("EVENT_001")
    event_data: List[str] = [
        "login",
        "error",
        "logout"
    ]
    print("Initializing Event Stream...")
    if stream_event.validate_data(event_data) is False:
        print("Error while reading Event Data... "
              "Shutting down the system")
        return
    stats = stream_event.get_stats()
    print(f"Stream ID: {stats['stream_id']}, Type: {stats['type']}")
    print("Processing event batch: [", end="")
    i = 0
    for item in event_data:
        if i != ft_len(event_data) - 1:
            print(f"{item}, ", end="")
        else:
            print(f"{item}]")
        i += 1
    error_count: int = 0
    for item in event_data:
        if item == 'error':
            error_count += 1
    print(f"Event analysis: {ft_len(event_data)} events, {error_count} "
          "error detected")


def polymorphic_stream():
    """Demonstrates polymorphic processing"""
    print("Processing mixed stream types through unified interface...")
    processor: StreamProcessor = StreamProcessor()
    sensor: SensorStream = SensorStream("SENSOR_001")
    trans: TransactionStream = TransactionStream("TRANS_001")
    event: EventStream = EventStream("EVENT_001")
    processor.add_stream(sensor)
    processor.add_stream(trans)
    processor.add_stream(event)
    sensor_data: List[tuple[str, float]] = [
        ('pressure', 1400),
        ('temp', 60)
    ]
    trans_data: List[tuple[str, int]] = [
        ('buy', 10),
        ('sell', 20),
        ('buy', 10),
        ('sell', 200)
    ]
    event_data: List[str] = [
        "login",
        "logout",
        "entry"
    ]

    data_map: Dict[str, Any] = {
        "SENSOR_001": sensor_data,
        "TRANS_001": trans_data,
        "EVENT_001": event_data
    }
    processor.process_streams(data_map)
    processor.report_filtered_results(data_map, "high_priority")


def main():
    """Main entry point"""
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    separate_streams()
    print()
    print('=== Polymorphic Stream Processing ===')
    polymorphic_stream()


if __name__ == "__main__":
    main()
