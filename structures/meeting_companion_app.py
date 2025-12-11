import gradio as gr

from services import speech_to_text


class MeetingCompanionApp:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port

        self.audio_input = gr.Audio(
            value="assets/sample.mp3"
            sources="upload",
            type="filepath",
            autoplay=False,
            interactive=True
        )
        self.output_text = gr.Textbox()

        self.app_interface = gr.Interface(
            fn=speech_to_text, 
            inputs=self.audio_input, outputs=self.output_text, 
            title="Audio Transcription App",
            description="Upload the audio file"
        )

    def launch_app(self) -> None:
        self.app_interface.launch(
            server_name=self.host,
            server_port=self.port
        )
