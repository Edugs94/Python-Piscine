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
    counter = 0
    for _ in data:
        counter += 1
    return counter

class DataStream(ABC):
    def __init__(self, stream_id: str):
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]= None) -> List[Any]:

            return data_batch


    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            'stream_id': self.stream_id,
            'type': 'Unkown type Data'
            }


class SensorStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            'stream_id': self.stream_id,
            'type': 'Environmental Data'
            }

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]= None) -> List[Any]:
        if criteria is 'high_value':
            return [x for x in data_batch if x > 40]
        else:
            return data_batch


class TransactionStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            'stream_id': self.stream_id,
            'type': 'Financial Data'
            }

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]= None) -> List[Any]:
        if criteria is 'high_temp':
            if data_batch[0]
            return [x for x in data_batch if x[0] > 40]
        else:
            return data_batch


class EventStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass


class StreamProcessor:
    def __init__(self) -> None:
        pass
    def process_stream():
    pass


def main():
    print('=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===')
    print()
    stream_sensor = SensorStream('001')
    print('Initializing Sensor Stream...')
    stats = stream_sensor.get_stats()
    print(f'Stream ID: {stats['stream_id']}, Type: {stats['type']}')
    print('Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]')
    print('Sensor analysis: 3 readings processed, avg temp: 22.5°C')


if __name__ == "__main__":
    main()

'''
$> python3 data_stream.py
=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===

Initializing Sensor Stream...
Stream ID: SENSOR_001, Type: Environmental Data
Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]
Sensor analysis: 3 readings processed, avg temp: 22.5°C

Initializing Transaction Stream...
Stream ID: TRANS_001, Type: Financial Data
Processing transaction batch: [buy:100, sell:150, buy:75]
Transaction analysis: 3 operations, net flow: +25 units

Initializing Event Stream...
Stream ID: EVENT_001, Type: System Events
Processing event batch: [login, error, logout]
Event analysis: 3 events, 1 error detected

=== Polymorphic Stream Processing ===
Processing mixed stream types through unified interface...

Batch 1 Results:
- Sensor data: 2 readings processed
- Transaction data: 4 operations processed
- Event data: 3 events processed

Stream filtering active: High-priority data only
Filtered results: 2 critical sensor alerts, 1 large transaction
All streams processed successfully. Nexus throughput optimal
'''
