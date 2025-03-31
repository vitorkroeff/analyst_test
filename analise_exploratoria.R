# Pacotes utilizados
require(dplyr)
require(ggplot2)

# Clientes
clientes <- read.csv('BASES/Clientes.csv', sep =';', colClasses = 'character')
View(clientes)
str(clientes)


#  Estoque
estoque <- read.csv('BASES/Estoque.csv', sep =';', colClasses = 'character')
View(estoque)

# Forecedores
forncedores <- read.csv('BASES/Fornecedores.csv', sep =';', colClasses = 'character',
                        fileEncoding = "latin1")
View(forncedores)

# Produtos
produtos <- read.csv('BASES/Produtos.csv', sep =';', colClasses = 'character',
                     fileEncoding = "latin1")
View(produtos)

# Vendas
vendas <- read.csv('BASES/Vendas.csv', sep =';', colClasses = 'character',
                               fileEncoding = "latin1")
View(vendas)


# Média de compras por cliente
compras_cliente <- vendas %>% group_by(client_id) %>% summarise(vendas = n(),
                                                                tkm = mean(as.numeric(total_value)))

mean(compras_cliente$vendas) # Média de compras

mean(compras_cliente$tkm) # Média do tkm.
