# 🕒 Kaiten Time Logger

Приложение для автоматизации учета рабочего времени в Kaiten на основе git-коммитов.

## ✨ Возможности

- 🔄 Автоматический сбор коммитов за текущий день
- 📊 Группировка коммитов по веткам
- 🔔 Уведомления в настраиваемое время
- 📅 Работа только в рабочие дни с учетом праздников

## 🚀 Быстрый старт

### Установка

```bash
# Клонируем репозиторий
git clone https://github.com/PavelDemin/kaiten_time_logger
cd kaiten_time_logger
pip install uv
uv venv
uv pip install -e .
```

### Настройка

1. Запустите приложение:
   ```bash
   uv run python src/main.py
   ```
2. Откройте настройки через иконку в трее
3. Укажите:
   - **URL Kaiten**
   - **API-токен** Kaiten
   - **Время уведомлений** (формат HH:MM, например 18:00)
   - **Путь к git-репозиторию**
   - **Идентификатор роли в Kaiten** (role_id)

## 💡 Использование

1. Приложение работает в фоновом режиме
2. В указанное время появится окно с:
   - Списком коммитов по веткам
   - Полями для ввода времени
   - Редактируемыми описаниями
3. Введите время в формате `ЧЧ.ММ`
4. Нажмите "Сохранить"

## 🛠️ Технологии

- Python 3.12+
- tkinter + ttk
- [GitPython](https://gitpython.readthedocs.io/)
- [pystray](https://github.com/moses-palmer/pystray)
- [holidays](https://pypi.org/project/holidays/)
- [keyring](https://pypi.org/project/keyring/)
- [Pillow](https://python-pillow.org/)
- [schedule](https://schedule.readthedocs.io/)

## Сборка

Для сборки exe-файла используется GitHub Actions. При каждом push в main:
1. Запускаются тесты и проверка кода
2. Если тесты прошли успешно, собирается exe-файл через PyInstaller
3. Собранный файл доступен в артефактах сборки

## Лицензия

MIT

