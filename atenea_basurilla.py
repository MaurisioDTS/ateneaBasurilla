#!/usr/bin/env python3
"""GUI simple: convierte un texto en flag Atenea vía MD5 (equivalente a echo -n '...' | md5sum)."""

import hashlib
import tkinter as tk
from tkinter import ttk, messagebox

## QUE MIRAS AQUIDENTRO PRIMO?¿
def md5_hex_no_trailing_newline(s: str) -> str:
    return hashlib.md5(s.encode("utf-8")).hexdigest()


def build_flag(s: str) -> str:
    return f"flag{{{md5_hex_no_trailing_newline(s)}}}"


def main() -> None:
    root = tk.Tk()
    root.title("atenea basurilla")
    root.minsize(420, 160)

    frm = ttk.Frame(root, padding=12)
    frm.grid(row=0, column=0, sticky="nsew")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    frm.columnconfigure(1, weight=1)

    ttk.Label(frm, text="texto a convertir en flag:").grid(
        row=0, column=0, columnspan=2, sticky="w"
    )
    entry = ttk.Entry(frm, width=48)
    entry.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(4, 8))
    entry.focus()

    out_var = tk.StringVar(value="flag{…}")

    def update_flag() -> None:
        s = entry.get()
        out_var.set(build_flag(s))

    def copy_flag() -> None:
        flag = out_var.get()
        if flag.startswith("flag{") and len(flag) > 10:
            root.clipboard_clear()
            root.clipboard_append(flag)
            root.update()

    def clear_input() -> None:
        entry.delete(0, tk.END)
        out_var.set("flag{…}")
        entry.focus()

    btn_row = ttk.Frame(frm)
    btn_row.grid(row=2, column=0, columnspan=2, sticky="w", pady=(0, 8))
    ttk.Button(btn_row, text="generar flag", command=update_flag).pack(side=tk.LEFT, padx=(0, 8))
    ttk.Button(btn_row, text="copiar flag", command=copy_flag).pack(side=tk.LEFT)
    ttk.Button(btn_row, text="limpiar", command=clear_input).pack(side=tk.LEFT, padx=(8, 0))

    ttk.Label(frm, text="flag para atenea:").grid(row=3, column=0, sticky="nw")
    out = ttk.Entry(frm, textvariable=out_var, state="readonly", width=48)
    out.grid(row=3, column=1, sticky="ew", pady=(0, 4))

    ttk.Label(
        frm,
        text="jvnfafdnscnswuf",
        font=("TkDefaultFont", 8),
        foreground="gray",
    ).grid(row=4, column=0, columnspan=2, sticky="w")

    def on_return(_event: tk.Event) -> str:
        update_flag()
        return "break"

    entry.bind("<Return>", on_return)

    def show_help() -> None:
        messagebox.showinfo(
            "ayuda",
            "lomismo que:\n  echo -n 'texto' | md5sum\n\n"
            "flag: flag{<hash_md5_32_hex_minúsculas>}",
        )

    ttk.Button(btn_row, text="ayuda", command=show_help).pack(side=tk.LEFT, padx=(8, 0))

    root.mainloop()


if __name__ == "__main__":
    main()
