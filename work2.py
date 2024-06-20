import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑


def button_action1():  # 関数の定義 ※ボタンが押されたときの動き
    seireki = int(num.get())
    if seireki < 1912:
        gengo = "明治"
        wareki = seireki - 1868 + 1
    elif seireki < 1926:
        gengo = "大正"
        wareki = seireki - 1912 + 1
    elif seireki < 1989:
        gengo = "昭和"
        wareki = seireki - 1926 + 1
    elif seireki < 2019:
        gengo = "平成"
        wareki = seireki - 1989 + 1
    else:
        seireki > 2019
        gengo = "令和"
        wareki = seireki - 2019 + 1

    if wareki == 1:
        label1.config(text=f"西暦{seireki}年は{gengo}元年です")
    else:
        label1.config(text=f"西暦{seireki}年は{gengo}{wareki}年です")


# 入力フィールドの作成
num = tk.Entry(window, bg=fg_color, fg=bg_color)
num.pack(pady=10)

# ボタンの作成
button1 = tk.Button(window, text="変換", command=button_action1)
button1.pack(pady=10)

# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
