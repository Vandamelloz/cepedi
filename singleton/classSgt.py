class DataBaseSingleton(type):
    _instances= {} #variável privada em python

    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            instance= super().__call__(*args, **kwds)
            cls._instances[cls]= instance
        return cls._instances[cls]
   
class DataBaseCliente(metaclass= DataBaseSingleton):
  classmates= []
  connection =0
  def __init__(self, port) -> None:
     self.set_connection(port)
  def set_connection(self,port):
    if not isinstance(port, int): #isistance retorna se é true o tipo de valor informado
        raise TypeError("A porta informada não é válida!Digite um número: ")
    self.connection= port
  def get_connection(self):
     return self.connection
  def set_classmates(self, classmates):
     for classmates in classmates:
         self.classmates.append(classmates)
  def get_classmates(self):
     return self.classmates