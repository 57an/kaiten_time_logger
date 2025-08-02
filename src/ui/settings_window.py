import tkinter as tk
from tkinter import ttk
from typing import Callable

from src.core.config import Config, config


class SettingsWindow(tk.Toplevel):
    def __init__(self, parent, on_init_app: Callable, user_roles: list[dict[int, str]]):
        super().__init__(parent)
        self.on_init_app = on_init_app
        self.user_roles = user_roles
        self.title('Настройки')

        window_width = 400
        window_height = 550

        self.geometry(f'{window_width}x{window_height}')

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.geometry(f'{window_width}x{window_height}+{x}+{y}')

        style = ttk.Style()
        style.configure('Settings.TLabel', padding=5)
        style.configure('Settings.TEntry', padding=5)
        style.configure('Settings.TButton', padding=5)

        token_label = ttk.Label(self, text='Kaiten API токен:', style='Settings.TLabel')
        token_label.pack(padx=5, pady=5)
        self.token_var = tk.StringVar(value=config.kaiten_token)
        token_entry = ttk.Entry(
            self,
            textvariable=self.token_var,
            width=40,
            show='*',
            style='Settings.TEntry',
        )
        token_entry.pack(padx=5, pady=5)

        url_label = ttk.Label(self, text='URL Kaiten:', style='Settings.TLabel')
        url_label.pack(padx=5, pady=5)
        self.url_var = tk.StringVar(value=config.kaiten_url)
        url_entry = ttk.Entry(
            self,
            textvariable=self.url_var,
            width=40,
            style='Settings.TEntry',
        )
        url_entry.pack(padx=5, pady=5)

        repo_label = ttk.Label(self, text='Путь до git репозитория:', style='Settings.TLabel')
        repo_label.pack(padx=5, pady=5)
        self.repo_var = tk.StringVar(value=config.git_repo_path)
        repo_entry = ttk.Entry(
            self,
            textvariable=self.repo_var,
            width=40,
            style='Settings.TEntry',
        )
        repo_entry.pack(padx=5, pady=5)

        time_label = ttk.Label(self, text='Время уведомления (HH:MM):', style='Settings.TLabel')
        time_label.pack(padx=5, pady=5)
        self.time_var = tk.StringVar(value=config.notification_time)
        time_entry = ttk.Entry(
            self,
            textvariable=self.time_var,
            width=10,
            style='Settings.TEntry',
        )
        time_entry.pack(padx=5, pady=5)

        # Add combobox for user roles
        role_label = ttk.Label(self, text='Выберите роль пользователя:', style='Settings.TLabel')
        role_label.pack(padx=5, pady=5)
        self.role_var = tk.StringVar()
        role_combobox = ttk.Combobox(
            self,
            textvariable=self.role_var,
            values=sorted(role for role in user_roles.values()),
        )
        role_combobox.pack(padx=5, pady=5)
        self.role_var.set(user_roles[config.role_id])

        author_label = ttk.Label(self, text='Автор коммита в git:', style='Settings.TLabel')
        author_label.pack(padx=5, pady=5)
        self.author = tk.StringVar(value=config.author)
        author_entry = ttk.Entry(
            self,
            textvariable=self.author,
            width=15,
            style='Settings.TEntry',
        )
        author_entry.pack(padx=5, pady=5)

        save_button = ttk.Button(
            self,
            text='Сохранить',
            command=self.save_settings,
            style='Settings.TButton',
        )
        save_button.pack(padx=5, pady=10)

    def save_settings(self):
        Config.save_config(
            self.token_var.get(),
            self.time_var.get(),
            self.repo_var.get(),
            self.url_var.get(),
            next(k for k, v in self.user_roles.items() if v == self.role_var.get()),
            self.author.get(),
        )
        self.on_init_app()
        self.destroy()
