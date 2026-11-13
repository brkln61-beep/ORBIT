class OrbitApp:
    def __init__(self):
        self.is_running = False

    def start(self):
        self.is_running = True
        print("ORBIT запущен!")

    def stop(self):
        self.is_running = False
        print("ORBIT остановлен!")