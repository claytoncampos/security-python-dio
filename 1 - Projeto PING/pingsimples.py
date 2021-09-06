import os #importa módulo ou  biblioteca (os) integra os programas e recursos do S.O


print("="* 60)#imprimindo = 60 *
ip_ou_host = input("Digite o IP ou Host a ser verificado: ") # atribuindo a variavel o valor digitado
print("="* 60)#imprimindo = 60 *
os.system('ping -n 6 {}'.format(ip_ou_host))#chamando system da biblioteca (os) comando ping -n numero de pacotes