import tkinter as tk
from pynput import keyboard as pynput_keyboard
import keyboard

# capitalize_next为0：正常运行，1：输入了符号，2：出现符号和空格，将下一个字母大写,3:mode_switch 1中的正常状态，4:mode_switch 1中的首字母大写状态
capitalize_next = 0
# init_status为0会将程序启动后的输入的第一个字母大写，1：正常运行状态
init_status = 0
# mode_switch 0：仅每句首字母大写，1：每次空格后都会大写首字母
mode_switch = 0
if mode_switch == 1:
    capitalize_next = 3

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Keyboard App")

        self.root.geometry("250x100")
        self.start_button = tk.Button(root, text="Start", command=self.start_program)
        self.start_button.pack()

        self.pause_button = tk.Button(root, text="Pause", command=self.pause_program)
        self.pause_button.pack()

        self.switch_button = tk.Button(root, text="Switch Mode", command=self.switch_mode)
        self.switch_button.pack()

        # 创建一个 Text 组件，设置为只读
        # self.read_only_text = tk.Text(root, wrap=tk.WORD, height=5, state=tk.DISABLED, fg="black")
        # self.read_only_text.insert(tk.END, "这是一个自动首字母大写辅助工具，点击start，可以自动帮助你将每段话的首字母大写，点击pause可以暂停使用;拥有两种模式，一种是检测到每句话的首字母大写；另一种是检测到空格就会将下一个字母大写")
        # self.read_only_text.pack(padx=10, pady=10)

        # 添加键盘监听器
        self.listener = pynput_keyboard.Listener(on_press=self.on_press)
        self.program_running = False

    def start_program(self):
        if not self.program_running:
            self.listener.start()
            self.program_running = True

    def pause_program(self):
        if self.program_running:
            self.listener.stop()
            self.program_running = False

    def switch_mode(self):
        # 在这里添加切换模式的逻辑
        global capitalize_next, init_status, mode_switch
        if mode_switch==0:
            mode_switch=1
        elif mode_switch==1:
            mode_switch = 0

    def on_press(self, key):
        # 在这里添加按下键的逻辑
        global capitalize_next, init_status, mode_switch
        if init_status == 0:
            uppercase_key = key.char.upper() if hasattr(key, 'char') else str(key).upper()
            print(uppercase_key)
            keyboard.press_and_release('backspace')
            keyboard.write(uppercase_key)  # 使用keyboard库的write方法
            init_status = 1
        try:
            if mode_switch == 0:
                if key.char == ',':
                    print('符号键： {} 被按下'.format(key.char))
                    capitalize_next = 1
                if key.char == '.':
                    print('符号键： {} 被按下'.format(key.char))
                    capitalize_next = 1
                if key.char == '!':
                    print('符号键： {} 被按下'.format(key.char))
                    capitalize_next = 1
                if key.char == ':':
                    print('符号键： {} 被按下'.format(key.char))
                    capitalize_next = 1

                # 如果不是特殊按键，就是普通字符键
                if capitalize_next == 2:
                    # 如果Shift键被按下或标志为True，将字符转为大写
                    uppercase_key = key.char.upper() if hasattr(key, 'char') else str(key).upper()
                    print(uppercase_key)
                    keyboard.press_and_release('backspace')
                    keyboard.write(uppercase_key)  # 使用keyboard库的write方法
                    capitalize_next = 0
                else:
                    print('字母键： {} 被按下'.format(key.char))
                print('状态：', capitalize_next)
            if mode_switch == 1:
                if key == pynput_keyboard.Key.space:
                    # 如果输入空格，设置标志以便下一个字母大写
                    capitalize_next = 4
                else:
                    # 如果不是特殊按键，就是普通字符键
                    if capitalize_next == 4:
                        # 如果Shift键被按下或标志为True，将字符转为大写
                        uppercase_key = key.char.upper() if hasattr(key, 'char') else str(key).upper()
                        print(uppercase_key)
                        keyboard.press_and_release('backspace')
                        keyboard.write(uppercase_key)  # 使用keyboard库的write方法
                        capitalize_next = 3
                    else:
                        print(key)
        except AttributeError:
            if key == pynput_keyboard.Key.space and capitalize_next == 1:
                print('空格键： {} 被按下'.format(key))
                capitalize_next = 2
            else:
                print('特殊键： {} 被按下'.format(key))


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()




# if mode_switch == 1:
#     capitalize_next = 3
# def on_press(key):
#     global capitalize_next, init_status, mode_switch
#     if init_status == 0:
#         uppercase_key = key.char.upper() if hasattr(key, 'char') else str(key).upper()
#         print(uppercase_key)
#         keyboard.press_and_release('backspace')
#         keyboard.write(uppercase_key)  # 使用keyboard库的write方法
#         init_status=1
#     try:
#         if mode_switch == 0:
#             if key.char == ',':
#                 print('符号键： {} 被按下'.format(key.char))
#                 capitalize_next = 1
#             if key.char == '.':
#                 print('符号键： {} 被按下'.format(key.char))
#                 capitalize_next = 1
#             if key.char == '!':
#                 print('符号键： {} 被按下'.format(key.char))
#                 capitalize_next = 1
#             if key.char == ':':
#                 print('符号键： {} 被按下'.format(key.char))
#                 capitalize_next = 1
#
#             # 如果不是特殊按键，就是普通字符键
#             if capitalize_next == 2:
#                 # 如果Shift键被按下或标志为True，将字符转为大写
#                 uppercase_key = key.char.upper() if hasattr(key, 'char') else str(key).upper()
#                 print(uppercase_key)
#                 keyboard.press_and_release('backspace')
#                 keyboard.write(uppercase_key)  # 使用keyboard库的write方法
#                 capitalize_next = 0
#             else:
#                 print('字母键： {} 被按下'.format(key.char))
#             print('状态：', capitalize_next)
#         if mode_switch == 1:
#             if key == pynput_keyboard.Key.space:
#                 # 如果输入空格，设置标志以便下一个字母大写
#                 capitalize_next = 4
#             else:
#                 # 如果不是特殊按键，就是普通字符键
#                 if capitalize_next == 4:
#                     # 如果Shift键被按下或标志为True，将字符转为大写
#                     uppercase_key = key.char.upper() if hasattr(key, 'char') else str(key).upper()
#                     print(uppercase_key)
#                     keyboard.press_and_release('backspace')
#                     keyboard.write(uppercase_key)  # 使用keyboard库的write方法
#                     capitalize_next = 3
#                 else:
#                     print(key)
#     except AttributeError:
#         if key == pynput_keyboard.Key.space and capitalize_next == 1:
#             print('空格键： {} 被按下'.format(key))
#             capitalize_next = 2
#         else:
#             print('特殊键： {} 被按下'.format(key))
#
# # 设置监听器
# with pynput_keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()
