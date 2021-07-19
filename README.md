Rodando a algorítmo no Windows, utilizando PyCharm, numpy e PIP:

1. Com o "Terminal" do PyCharm, fazer uso do "pip" para instalar o "Numpy" (PIP constumar ser instalado junto do PyCharm):
    
    "pip install numpy" 
  
  ![image](https://user-images.githubusercontent.com/52551449/126098884-9d955082-1382-48bd-b544-42df0d7992bf.png)
  
 2. O diretório do projeto deve necessáriamente conter dois arquivos ".txt":
    
  2.1 "mapa.txt": O caractere "0" representa um espaço disponível para que o agente possa percorrer, e "1" um obstáculo. 
    Obs.: Os caracteres do mapa podem ser alterados.
    
![image](https://user-images.githubusercontent.com/52551449/126230156-a206626a-a986-4442-ae66-6370b0a5752b.png)

   2.2 "path.txt": Inicialmente pode estar em branco, o importante aqui é que o arquivo exista no root da aplicação.
    Obs.: A cada vez que o algoritmo rodar, um novo percurso com base no "mapa.txt", será gerado neste no "path.txt". 
    
![image](https://user-images.githubusercontent.com/52551449/126230418-32ca914a-c2ba-42df-a5f5-c20054b46321.png)


Após estes dois passos, seu projeto será capaz de rodar o algoritmo em questão.
Caso esteja com dificuldades de rodar o algoritmo, sugiro que crie um novo projeto no "PyCharm", copie o código daqui "main.py" e cole no "main.py" do seu novo projeto. Feito isso, mova o "mapa.txt" daqui para onde se encontra o novo "main.py" do seu novo projeto, e crie um "path.txt" em branco no mesmo local.
Pronto, feito isto, basta rodar a aplicação novamente.
