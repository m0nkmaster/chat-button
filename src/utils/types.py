from typing import Protocol, List, Dict, Optional, Callable, Any
from dataclasses import dataclass
import pyaudio

class AudioConfig:
    def __init__(
        self,
        sample_rate: int = 48000,
        channels: int = 1,
        chunk_size: int = 1024,
        format: int = pyaudio.paInt16,
        input_device_index: int | None = None,
    ):
        self.sample_rate = sample_rate
        self.channels = channels
        self.chunk_size = chunk_size
        self.format = format
        self.input_device_index = input_device_index

@dataclass
class AudioFrame:
    data: bytes
    is_speech: bool

class AudioRecorder(Protocol):
    def start_recording(self) -> None:
        """Start recording audio."""
        ...
    
    def stop_recording(self, is_wake_word_mode: bool = False) -> bytes:
        """Stop recording and return the recorded audio data."""
        ...

class AudioAnalyzer(Protocol):
    def is_speech(self, audio_data: bytes, config: Any) -> bool:
        """Analyze audio data to determine if it contains speech."""
        ...

class AudioPlayer(Protocol):
    def play(self, audio_data: bytes) -> None:
        """Play audio data."""
        ...

class WordDetector(Protocol):
    def detect(self, audio_data: bytes) -> bool:
        """Detect if the wake word is present in the audio data."""
        ...

class ConversationManager(Protocol):
    def add_user_message(self, message: str) -> None:
        """Add a user message to the conversation history."""
        ...
    
    def add_assistant_message(self, message: str) -> None:
        """Add an assistant message to the conversation history."""
        ...
    
    def get_conversation_history(self) -> List[Dict[str, str]]:
        """Get the full conversation history."""
        ...
    
    def clear_history(self) -> None:
        """Clear the conversation history."""
        ...
    
    def get_last_user_message(self) -> Optional[str]:
        """Get the most recent user message."""
        ...
    
    def get_last_assistant_message(self) -> Optional[str]:
        """Get the most recent assistant message."""
        ...