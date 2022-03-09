from classes import Recipiente
from classes import Copo

if __name__ == "__main__":
    # Execute suas testagens manuais aqui
    r = Recipiente(100)
    print(r.tamanho)
    print(r)
    print(r.esta_limpo())
  
    print(r.estado())

    r.sujar()
    print(r.esta_limpo())

    r.lavar()
    print(r.esta_limpo())


    copo = Copo(100)

    print(copo.tamanho)
    print(copo)

    print(copo.estado())

    copo.encher("café")
    print(copo.bebida)
