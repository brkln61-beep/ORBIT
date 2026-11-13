from config import APP_NAME, DEBUG, VERSION
from core.app import OrbitApp

app = OrbitApp()

def main():
    print(f"Запуск приложения: {APP_NAME}")
    print(f"Версия: {VERSION}")
    print(f"Режим отладки: {DEBUG}")
    app.start()

if __name__ == "__main__":
    main()