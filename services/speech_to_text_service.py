import torch
from transformers import pipeline


def speech_to_text(audio_file):
    pipe = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-tiny.en",
        chunk_length_s=30
    )

    prediction = pipe(audio_file, batch_size=8)["text"]
    
    return prediction
