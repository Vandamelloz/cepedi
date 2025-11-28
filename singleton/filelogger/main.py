from file_logger import FileLogger
from auth_manager import AuthManager
import os

if os.path.exists(FileLogger._log_file):
    os.remove(FileLogger._log_file)


print("--- Teste 1: Logger Singleton ---")

logger_a = FileLogger()
print(f"ID Logger A: {id(logger_a)}")
logger_a.info("Módulo A: Inicializando o aplicativo.")

logger_b = FileLogger()
print(f"ID Logger B: {id(logger_b)}")


if id(logger_a) == id(logger_b):
    print("Sucesso: logger_a e logger_b são a mesma instância (Singleton).")
else:
    print("Falha: Mais de uma instância do logger foi criada.")

logger_b.warning("Módulo B: Atenção, recurso depreciado detectado.")


print("\n--- Teste 2: AuthManager (Módulo Externo) ---")

auth_service = AuthManager()


auth_service.login("user_teste", "senha_errada") 

auth_service.login("admin", "secret")

auth_service.get_current_user()


auth_service.logout()

logger_a.error("Processo principal encerrado com erros críticos.")


logger_a.close()

print(f"\n--- Conteúdo do Arquivo de Log ({FileLogger._log_file}) ---")
try:
    with open(FileLogger._log_file, 'r', encoding='utf-8') as f:
        print(f.read())
except FileNotFoundError:
    print("O arquivo de log não foi criado ou encontrado.")