import gradio as gr
import random
import time


def user(user_message, history):
    return "", history + [[user_message, None]]


def bot(history):
    bot_message = random.choice(["How are you?", "I love you", "I'm very hungry"])
    history[-1][1] = ""
    for character in bot_message:
        history[-1][1] += character
        time.sleep(0.05)
        yield history


def vote(data: gr.LikeData):
    if data.liked:
        print("You upvoted this response: " + data.value)
    else:
        print("You downvoted this response: " + data.value)


with gr.Blocks() as demo:
    chatbot = gr.Chatbot(bubble_full_width=False)
    msg = gr.Textbox(placeholder="请输入问题", scale=7)
    clear = gr.Button("Clear")
    chatbot.like(vote, None, None)  # Adding this line causes the like/dislike icons to appear in your chatbot

    submit = gr.Button("submit", size="sm", min_width=10, scale=3)
    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
        bot, chatbot, chatbot
    )
    clear.click(lambda: None, None, chatbot, queue=False)
    submit.click()
demo.queue()
demo.launch()
