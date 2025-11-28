# file_logger.py
import datetime
import os

class FileLogger:
    _instance = None
    _log_file = "app_log.txt"
    _is_initialized = False

    def __new__(cls, *args, **kwargs):
       
       
        if cls._instance is None:
            cls._instance = super(FileLogger, cls).__new__(cls)
        return cls._instance

    def __init__(self):
       
        if not self._is_initialized:
            try:
    
                self._file_handle = open(self._log_file, 'a', encoding='utf-8')
                self._is_initialized = True
                self.info("Logger inicializado com sucesso.")
            except IOError as e:
                print(f"ERRO: Não foi possível abrir o arquivo de log '{self._log_file}'. {e}")
                self._is_initialized = True 

    def _format_message(self, level: str, message: str) -> str:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"[{timestamp}][{level.upper()}]: {message}\n"

    def log(self, level: str, message: str):
        if self._is_initialized and hasattr(self, '_file_handle'):
            formatted_message = self._format_message(level, message)
            self._file_handle.write(formatted_message)
            self._file_handle.flush() 
        elif not hasattr(self, '_file_handle'):
             print(f"LOG FALHOU: Arquivo não está acessível. Mensagem: {message}")


    def info(self, message: str):
        self.log("INFO", message)

    def warning(self, message: str):
        self.log("WARNING", message)

    def error(self, message: str):
        self.log("ERROR", message)

    def close(self): 
        if hasattr(self, '_file_handle') and not self._file_handle.closed:
            self._file_handle.close()
            self._is_initialized = False
            print(f"Logger: Arquivo '{self._log_file}' fechado.")