import environs

from pathlib import Path

# Инициализация объекта окружения
env = environs.Env()
BASE_DIR = Path(__file__).resolve().parent.parent

# Проверяем существование файла .env и загружаем переменные окружения
if Path(BASE_DIR / '.env').exists():
    env.read_env(Path(BASE_DIR) / '.env')
else:
    raise FileNotFoundError('.env file not found')
