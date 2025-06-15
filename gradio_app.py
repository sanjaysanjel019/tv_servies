import gradio as gr

def get_themes(theme_list,subtitles_path,save_path):
    theme_list = theme_list.split(",")
    theme_classifier = ThemeClassifier(theme_list)
    
def main():
    with gr.Blocks() as iface:
        with gr.Row():
            with gr.Column():
                gr.HTML("<h1>Theme Classification9Zero Shor Classifier)</h1>")
                with gr.Row():
                    with gr.Column():
                        plot = gr.BarPlot()
                    with gr.Column():
                        theme_list = gr.Textbox(label="Themes")
                        subtitles_path = gr.Textbox(label="Subtitles or Script Path")
                        save_path = gr.Textbox(label="Save Path")
                        get_theses_button = gr.Button("Get Themes")
                        get_theses_button.click(
                            fn=get_themes,
                            inputs=[subtitles_path,theme_list],
                            outputs=[plot,theme_list]
                        )
                        save_button = gr.Button("Save")
                    


if __name__ == "__main__":
    main()