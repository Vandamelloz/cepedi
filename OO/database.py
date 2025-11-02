import sqlite3
class database:
    def __init__(self, dbPath: str= "exemplo2.db"):
       self.dbPath= dbPath
       self.conn= None
    def conectar(self):
        self.conn= sqlite3.connect(self.dbPath, isolation_level= None) #AUTO COMMIT 
        self.conn.row_factory=sqlite3.Row
        self.conn.execute("PRAGMA foreign_keys =ON")
        return self.conn
    def desconectar(self):
       self.close()
    def cursor(self):
     return self.conn.cursor()
    def criarTabelas(self):
     cur= self.cursor()
     cur.execute="""
criação de tabelas 
"""
    def limparTabelas(self):
     cur=self.cursor()
     cur.execute="""
comando de deletar tabelas """
