dataset = read.csv(file = '/home/skull/workspace/workspaceML_AZ_DS/workspaceML_AZ_DS/data_sets/parte_1_preprocesodedatos/Data.csv')
#print(dataset)

#Tratamiento de los valores NAN
#Se llama el dataset concatenado con el nombre de columna
#Muy similar a un decode le uso del ifelse

dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x) mean(x,na.rm = TRUE)),
                     dataset$Age)

dataset$Salary = ifelse(is.na(dataset$Salary),
                     ave(dataset$Salary, FUN = function(x) mean(x,na.rm = TRUE)),
                     dataset$Salary)



round(dataset$Age)

round(dataset$Salary)
