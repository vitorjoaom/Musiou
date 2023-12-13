class Cliente:
    __nome: str
    __nascimento: int
    __email: str
    __conta: float


    def __init__(self,nome,nascimento,email,conta):
        self.__nome = nome
        self.__nascimento = nascimento
        self.__email = email
        self.__conta = conta
    
    @property
    def _nome(self):
        self.__nome  
    @property
    def _nascimento(self):
        self.__nascimento
    @property
    def _email(self):
        self.__email
    @property
    def _conta(self):
        self.__conta

    @__nome.setter
    def nome(self) -> str:
        return self.__nome 
    @__nascimento.setter
    def nascimento(self) -> int:
        return self.__nascimento 
    @__email.setter
    def email(self) -> str:
        return self.__email 
    @__conta.setter
    def conta(self) -> float:
        return self.__conta 

                
    def cadastrar(self, novonome,novonasc,novoemail,novaconta):
        self.__nome = novonome
        self.__nascimento = novonasc
        self.__email = novoemail
        self.__conta = novaconta
    def mudarnome(self, novonome):
        self.__nome = novonome


