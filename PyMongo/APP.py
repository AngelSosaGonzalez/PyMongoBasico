"""Pero... ¿Que es PyMongo? 
Este es una libreria o modulo creado para el lenguaje de programacion de Python
con el objetivo de podernos conectar a nuestras bases de datos en MongoDB,
tampoco voy a contar historia solamente que es, no me pidan mucho"""

#Importamos PyMongo
import pymongo

#Importamos DNS
import dns


#Especificar la ruta de nuestra base de datos
#El enlace de mongodb es en base al cluster creado en atlas (mongodb pero en cloud, la nube pues)
Cliente = pymongo.MongoClient("*Enlace de conexion*")
BaseDatos = Cliente.perfil
#El .perfil es en referencia al nombre de la base de datos, como ya dice anteriormente lo llamaremos .perfil

"""NOTA A DESARROLLADOR NOVATO (Osea yo), en momento de realizar la conexion a la base de datos
(que lo haces en la opcion de conection del cluster), te lo pido, no te lo ruego el nombre
va en minusculas completamente, ahora cuando hagas la conexion (lo que esta en el codigo da arriba)
al momento de realizar la autenticacion debes de crear un usuario con contraseña, para mas seguro
que no se te olvide, de nuevo, te lo ruego, te lo imploro, es con minusculas, todo es con minusculas
o si no te pasaras 2 horas buscando el error, de antemano muchas gracias"""

#Comprobamos, solamente compruebo si hay una conexion
"""try:
    print("MongoDB version is %s" %
            my_client.server_info()['version'])
except pymongo.errors.OperationFailure as error:
    print(error)
    quit(1)"""
#Lo pondre como comentario ya que no quiero que cada vez que se ejecute me imprima eso
#Lo puedes quitar y probar tus conexiones con la base...

#Insertar documentos, esto porque la BD esta orientada a documentos
#Comenzaremos invocando a la coleccion
Coleccion = BaseDatos.usuarios
#El .usuarios es la referencia a la coleccion de nuestra BD (en este caso se llama perfil)


#Inserar un documento, como es una coleccion de ususarios pues pondremos datos personales 
Coleccion.insert_one({

    'Nombre': 'Angel',
    'Edad': 21,
    'Ciudad': 'Nezahualcoyotl'
})

"""Pero tu me puedes preguntar ¿Oye, y como hago si no quiero comenzar con un solo documento?
tu tranquilo te lo voy a poner, para agregar mas documentos usaremos _many, aqui te va un ejemplo"""

Coleccion.insert_many([
   {
    'Nombre': 'Alberto',
    'Edad': 24,
    'Ciudad': 'Nezahualcoyotl' 
   },
   {
    'Nombre': 'Rodrigo',
    'Edad': 25,
    'Ciudad': 'Ecatepec' 
   }
])

"""Ahora vamos a las consultas :), para este caso usaremos la funcion .find()
pues en español find es encontrar, te lo juro buscalo en google"""
BuscarUsu = Coleccion.find()
print('Los Usarios registrados son: \n')
for nombre in BuscarUsu:
    print('- ', nombre['Nombre'])

#Y para buscar uno es especifico
BuscarUsu = Coleccion.find({
    'Nombre': 'Angel'
})

#Actualizacion de los datos
Coleccion.update_one(
    {'Nombre': 'Alberto'}, #Sera la busqueda o el dato de referencia
    #Ahora los datos a actualizar
    {
        '$set':{
            'Nombre': 'Juan',
            'Edad': 26
        }
    }
)
#Nota se puede realizar una actualizacion de mas de un registro con el metodo _many

#Eliminar datos
Coleccion.delete_one({
    'Nombre':'Rodrigo'
})     

#Antes de esto te recomiendo una cosa en las busquedas para verificar usa un print
#Solo para asegurar...
"""Ahora para terminar, este pequeño tutorial sobre MongoDB y Phyton es algo sencillo
el verdadero objetivo de este proyecto es para realizar una API pero ya dejando de lado
un documento estatico o una BD relacional, ya entrando al terreno de la API en BD no relacional"""