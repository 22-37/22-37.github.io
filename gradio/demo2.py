import gradio as gr
import time


def echo(message, history):
    response = message + "李哲gg好帅李哲gg好帅李哲gg好帅李哲gg好帅李哲gg好帅李哲gg好帅."

    data_str = '\n'.join(str(item) for item in history)  # 保存对话
    with open('data.txt', 'w') as file:
        file.write(data_str)

    for i in range(len(response)):  # 延时显示
        time.sleep(0.1)
        yield response[: i + 1]


demo = gr.ChatInterface(fn=echo,
                        chatbot=gr.Chatbot(label="lizhe123", height=365, bubble_full_width=False, container=True,
                                           show_label=True,
                                           scale=2),

                        textbox=gr.Textbox(placeholder="请输入问题", container=True, scale=7),
                        title="lizhe123",
                        description="西北工业大学招生智能问答机器人",
                        theme="soft",
                        examples=["你好", "西工大？", "李哲帅不帅？"],
                        retry_btn="重试",
                        undo_btn="撤回",
                        clear_btn="清空",
                        autofocus=True,
                        )

if __name__ == "__main__":
    demo.queue().launch(share=True)
