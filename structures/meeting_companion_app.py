import gradio as gr
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from services import (
    speech_to_text,
    summarize_transcription
)


class MeetingCompanionApp:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port

        self.llm_chain = self._initiate_llm_chain()

        self.audio_input = gr.Audio(
            value="assets/sample.mp3",
            sources="upload",
            type="filepath",
            autoplay=False,
            interactive=True
        )
        self.output_text = gr.Textbox()

        self.app_interface = gr.Interface(
            fn=summarize_voice_message, 
            outputs=self.output_text, 
            title="Audio Transcription App",
            description="Upload the audio file"
        )

    def _initiate_llm_chain(self):
        MSG_TEMPLATE = """
        <s><<SYS>>
        List the key points with details from the context: 
        [INST] The context : {context} [/INST] 
        <</SYS>>
        """

        llm = LLMChain(
            model_path="~/Models/llama-2-7b-chat.Q4_0.gguf",
            streaming=False
        )
        prompt_template = PromptTemplate(
            input_variables=["context"],
            template=MSG_TEMPLATE
        )
        prompt_to_LLAMA2 = LLMChain(llm=llm, prompt=prompt_template)

        return prompt_to_LLAMA2

    def launch_app(self) -> None:
        self.app_interface.launch(
            server_name=self.host,
            server_port=self.port
        )

    def summarize_voice_message(self):
        transcript = speech_to_text(audio_file=self.audio_input)
        summary = summarize_transcription(transcript=transcript, llm_chain=self.llm_chain)
        
        return summary
