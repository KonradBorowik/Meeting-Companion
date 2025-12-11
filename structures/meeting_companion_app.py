import gradio as gr

from services import speech_to_text


class MeetingCompanionApp:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port

        self.audio_input = gr.Audio(sources="upload", type="filepath")  # Audio input
        self.output_text = gr.Textbox()  # Text output

        self.iface = gr.Interface(
            fn=transcript_audio, 
            inputs=audio_input, outputs=output_text, 
            title="Audio Transcription App",
            description="Upload the audio file"
        )

    def launch_app(self) -> None:
        self.iface.launch(
            server_name=self.hhost,
            server_port=self.port
        )
