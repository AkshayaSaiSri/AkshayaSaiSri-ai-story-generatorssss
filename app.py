import gradio as gr
from story_generator import generate_story
def main():
    interface = gr.Interface(
        fn=generate_story,
        inputs=gr.Textbox(label="Enter a story prompt"),
        outputs=gr.Textbox(label="Generated Story"),
        title="AI Story Generator"
    )
    interface.launch()

if __name__ == "__main__":
    main()
