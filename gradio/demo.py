import time
import gradio as gr


# 缓慢输出效果
def slow_echo(message, history):
    for i in range(len(message)):
        time.sleep(0.3)
        yield "You typed: " + message[: i + 1]


gr.ChatInterface(
    slow_echo,
    chatbot=gr.Chatbot(label="lizhe123", height=300),
    textbox=gr.Textbox(placeholder="请输入问题", container=False, scale=7),
    title="lizhe123",
    description="西北工业大学招生智能问答机器人",
    theme="soft",
    examples=["你好", "西工大？", "李哲帅不帅？"],
    cache_examples=True,
    retry_btn=None,
    undo_btn="撤回",
    clear_btn="清空",
).queue().launch()
