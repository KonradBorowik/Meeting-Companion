import gradio as gradio

from structures import MeetingCompanionApp


def main():
    mc_app = MeetingCompanionApp(
        host="0.0.0.0",
        port=7860
    )

    mc_app.launch_app()


if __name__ == "__main__":
    main()
