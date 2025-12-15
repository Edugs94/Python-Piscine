#!/usr/bin/env python3
"""
Ex2 nexus_pipeline
"""
from typing import Any, List, Dict, Union, Optional, Protocol
from abc import ABC, abstractmethod


class ProcessingPipeline(ABC):
    pass


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str):
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        pass


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str):
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        pass


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str):
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        pass


class InputStage:
    """Stage responsible for initial data output."""

    def process(self, data: Any) -> Any:
        """Validate and prepare data."""
        return data


class TransformStage:
    """Stage responsible for data modification."""

    def process(self, data: Any) -> Any:
        return data


class OutputStage:
    """Stage responsible for data output."""

    def process(self, data: Any) -> Any:
        return data
