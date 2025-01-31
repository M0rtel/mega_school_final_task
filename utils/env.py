import environs

from pathlib import Path

env = environs.Env()
BASE_DIR = Path(__file__).resolve().parent.parent


if Path(Path(BASE_DIR) / '.env').exists():
    env.read_env(Path(BASE_DIR) / '.env')
else:
    raise FileNotFoundError('.env file not found')
