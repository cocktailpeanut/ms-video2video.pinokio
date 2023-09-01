import gradio as gr

from modelscope.pipelines import pipeline
from modelscope.outputs import OutputKeys

pipe = pipeline(task='video-to-video', model='damo/Video-to-Video')#, model_revision='v1.1.0')

def infer (video_in, text):
    
    # IMG_PATH: your image path (url or local file)
    VIDEO_PATH = video_in
    print("video_in")
    print(video_in)
    input = {
        'video_path': VIDEO_PATH,
        'text': text
    }
    output_video_path = pipe(input, output_video='output.mp4')[OutputKeys.OUTPUT_VIDEO]
    print(output_video_path)
    
    return output_video_path

css="""

#col-container {
    max-width: 580px; 
    margin-left: auto; 
    margin-right: auto;
}
.animate-spin {
  animation: spin 1s linear infinite;
}
@keyframes spin {
  from {
      transform: rotate(0deg);
  }
  to {
      transform: rotate(360deg);
  }
}
#share-btn-container {
  display: flex; 
  padding-left: 0.5rem !important; 
  padding-right: 0.5rem !important; 
  background-color: #000000; 
  justify-content: center; 
  align-items: center; 
  border-radius: 9999px !important; 
  max-width: 13rem;
}
div#share-btn-container > div {
    flex-direction: row;
    background: black;
    align-items: center;
}
#share-btn-container:hover {
  background-color: #060606;
}
#share-btn {
  all: initial; 
  color: #ffffff;
  font-weight: 600; 
  cursor:pointer; 
  font-family: 'IBM Plex Sans', sans-serif; 
  margin-left: 0.5rem !important; 
  padding-top: 0.5rem !important; 
  padding-bottom: 0.5rem !important;
  right:0;
}
#share-btn * {
  all: unset;
}
#share-btn-container div:nth-child(-n+2){
  width: auto !important;
  min-height: 0px !important;
}
#share-btn-container .wrap {
  display: none !important;
}
#share-btn-container.hidden {
  display: none!important;
}
img[src*='#center'] { 
    display: block;
    margin: auto;
}
.footer {
    margin-bottom: 45px;
    margin-top: 10px;
    text-align: center;
    border-bottom: 1px solid #e5e5e5;
}
.footer > p {
    font-size: .8rem;
    display: inline-block;
    padding: 0 10px;
    transform: translateY(10px);
    background: white;
}
.dark .footer {
    border-color: #303030;
}
.dark .footer > p {
    background: #0b0f19;
}

"""

with gr.Blocks(css=css) as demo:
    with gr.Column(elem_id="col-container"):
        gr.Markdown("""
        
            <h1 style="text-align: center;">
                MS Video2Video
            </h1>

        
        """)

        video_in = gr.Video(
            label = "Source Video",
        )

        text_in = gr.Textbox()


        submit_btn = gr.Button(
            "Submit"
        )

        video_out = gr.Video(
            label = "Video Result",
            elem_id = "video-out"
        )



    submit_btn.click(
        fn = infer,
        inputs = [
            video_in, text_in
        ],
        outputs = [
            video_out
        ]
    )


demo.queue(max_size=20).launch()


