#!/usr/bin/env python
# coding: utf-8

# In[ ]:


nomedoativo = str(input("Inserir nome do ativo: "))


# In[ ]:


analiseanos = int(input("Quantidade de anos que deseja analisar: "))
anoinicio = int(input("Inserir ano da primeira analise (exemplo: 2014): "))
ano = anoinicio
analiseinicio = 1
rl = []
c = []
ll = []
db = []


# In[ ]:


while analiseinicio <= analiseanos:
    rl_ano = ano
    rl_valor = float(input("\nInserir valor da Receita Líquida, no ano de {}, em milhões: ".format(ano)))
    c_ano = ano
    c_valor = float(input("Inserir valor dos Custos, no ano de {}, em milhões: ".format(ano)))
    ll_ano = ano
    ll_valor = float(input("Inserir valor do Lucro Líquido, no ano de {}, em milhões: ".format(ano)))
    db_ano = ano
    db_valor = float(input("Inserir valor da Dívida Bruta, no ano de {}, em milhões: ".format(ano)))
    rl.append ([rl_ano,rl_valor])
    c.append ([c_ano,c_valor])
    ll.append ([ll_ano,ll_valor])
    db.append ([db_ano,db_valor])
    analiseinicio += 1
    ano += 1


# In[ ]:


print (rl)


# In[ ]:


ano = anoinicio
print (ano)


# In[ ]:


rl.sort(reverse=True)
anofinal = rl [0][0]
rl.sort()
print (anoinicio)
print (anofinal)


# In[ ]:


contagem = 0
cresc_ano = []
print (contagem)


# In[ ]:


print ("\nAnalisar o crescimento, ou não, da empresa de acordo com a relação entre Receita Líquida e Custos.")
print ("\nQuando o resultado der POSITIVO, quer dizer que a empresa obteve melhores resultados na relação entre Receita Líquida e Custos, seja: ")
print ("1. Aumentando mais a Receita Líquida do que os Custos;")
print ("Ou até mesmo 2. A queda da Receita Líquida foi menor do que a dos Custos;")
print ("E na melhor das hipóteses, 3. Aumento da Receita Líquida e queda dos Custos.")
print ("\nQuando NEGATIVO, quer dizer o contrário, então: ")
print ("1. Custos aumetaram mais do que a Receita Líquida;")
print ("2. A queda da Receita Líquida foi maior que a dos Custos;")
print ("No pior cenário, 3. Houve aumento dos Custos e diminuição da Receita Líquida.")


# In[ ]:


while anoinicio < anofinal:
    if rl[0+contagem][0] == c[0+contagem][0]:
        print ("\nNo período {}/{}, segue considerações: ".format(anoinicio, anoinicio+1))
        crescimento_rl = round (rl[1+contagem][1] - rl[0+contagem][1], 2)
        print ("Crescimento da Receita Líquida foi de {} milhões".format(crescimento_rl))
        crescimento_c = round (c[1+contagem][1] - c[0+contagem][1], 2)
        print ("Crescimento de Custo foi de {} milhões".format(crescimento_c))
        coeficiente_crescimento = round (crescimento_rl - crescimento_c, 2)
        print ("Relação do crescimento da empresa, com base na Receita Líquida e nos Custos foi de: {} milhões".format(coeficiente_crescimento))
        cresc_ano.append (coeficiente_crescimento)
        anoinicio += 1
        contagem += 1
    else:
        print ("erro")
        

                                                                        
        


# In[ ]:


anoinicio = rl [0][0]
cresc_ano1 = []
contagem = 0


# In[ ]:


while anoinicio < anofinal:
    if ll[0+contagem][0] == db[0+contagem][0]:
        crescimento_ll = ll[1+contagem][1] / ll[0+contagem][1]
        crescimento_llpor100 = crescimento_ll - 1
        print ("\nCrescimento do Lucro Líquido, respectivo ao período {}/{} foi de {}".format(anoinicio, anoinicio+1, crescimento_llpor100))
        crescimento_db = db[1+contagem][1] / db[0+contagem][1]
        crescimento_dbpor100 = crescimento_db - 1
        print ("Crescimento da Dívida Bruta, respectivo ao período {}/{} foi de {}".format(anoinicio, anoinicio+1, crescimento_dbpor100))
        coeficiente_crescimentopor100 = crescimento_llpor100 - crescimento_dbpor100
        print ("Relação do crescimento da empresa, respectivo ao período {}/{} foi de {}".format(anoinicio, anoinicio+1, coeficiente_crescimentopor100))
        cresc_ano1.append (coeficiente_crescimentopor100)
        anoinicio += 1
        contagem += 1
contagem = 0


# In[ ]:


while contagem < len (cresc_ano):
    print (cresc_ano [0+contagem])
    contagem += 1
contagem = 0


# In[ ]:


while contagem < len (cresc_ano1):
    print (cresc_ano1 [0+contagem])
    contagem += 1


# In[ ]:




