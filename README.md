# Sinesp-Python
Script de consulta ao SINESP em python


Para consultar basta executar o script e chamar a funcao consulta

usando cmd
python sinesp.py placa
usando idle deve-se comentar as ultimas linhas do script 
"
if __name__ == '__main__':
   consulta(*sys.argv[1:])
"
e utilizar chamando a função.
Consulta('PLACA A SER CONSULTADA')
