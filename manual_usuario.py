import tkinter as tk

def crear_ventana(root):
    ventana = tk.Toplevel(root)
    ventana.title("Ventana con Barra de Desplazamiento")
    ventana.configure(bg="#000000")
    ventana.focus_force()
    scrollbar = tk.Scrollbar(ventana)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    texto = tk.Text(ventana, yscrollcommand=scrollbar.set,bg="#000000")
    texto.pack()

    scrollbar.config(command=texto.yview)

    # Agregar texto con diferentes estilos y colores usando tags
    texto.tag_configure("en", foreground="white",font=("Arial", 10))
    texto.tag_configure("estilo_azul", foreground="blue", font=("Arial", 10, "bold"))
    texto.tag_configure("estilo_rojo", foreground="red", font=("Arial", 10, "bold"))
    texto.tag_configure("estilo_btn", foreground="yellow", font=("Arial", 10, "bold"))
    texto.tag_configure("e_rec", foreground="lightblue", font=("Arial", 10, "bold"))

    texto.insert(tk.END, '''BIENVENIDO AL SOFTWARE DE CREACION DE MÉTODOS ESTANDAR PETRA METHOD GEN software desarrollado por Fernando López V.\n\n''',"estilo_azul")
    texto.insert(tk.END, '''¿Cómo hacer un metodo de fabricación?\n\n''',"estilo_rojo")
    texto.insert(tk.END, '''Para crear un nuevo metodo de fabricacion para un producto
se presiona el boton "Crear un metodo de Fabricación"

Se abrira una ventana azul con diversos campos

Se recomienda tener informacion sobre el producto como

-Nombre
-Numero de Inventario
-Pictogramas (en caso de haber)
-Envase para venta
-Envase para control de calidad
_Equipo Utilizado
-¿Se  filtra el producto?

Si se tiene toda esta información, se vacia en los campos
y se da click en el boton que dice ''',"en")
                
    texto.insert(tk.END, '''"Iniciar metodo"''',"estilo_btn")             
    texto.insert(tk.END, '''

En este punto si por error se equivoca en ingresar alguna información previa
puede cambiar la información y volver a dar ''',"en")
    texto.insert(tk.END, '''"Iniciar metodo"''',"estilo_btn")
    texto.insert(tk.END, '''
Advertencia: Si despues de dar ''',"en")
    texto.insert(tk.END, '''"Iniciar metodo"''',"estilo_btn")
    texto.insert(tk.END, ''' y hubo un error
en la información agregada y se da click 
en cualquiera de los botones ''',"en")
    texto.insert(tk.END, '''"reactivo", "paso" y "banner" ''',"estilo_btn")
    texto.insert(tk.END, '''ya no se puede modificar ya que el programa bloquea el ingreso
de datos en la informacion basica. Si requiere modificar 
algun campo de la información previa, continue el metodo
con normalidad, guardelo y de click en el boton ''',"en")
    texto.insert(tk.END, "actualizar","estilo_btn")
    texto.insert(tk.END, ''' una vez que aparezca su nuevo producto añadido en el menu de 
la derecha en la ventana principal, de click en ''',"en")
    texto.insert(tk.END, "Editar Metodo","estilo_btn")
    texto.insert(tk.END, ''' para modificar el campo donde hubo un error

Una vez se añadio correctamente la información basica del producto
y se dio click en ''',"en")
    texto.insert(tk.END, "Iniciar metodo","estilo_btn")
    texto.insert(tk.END, ''' verá que en el recuadro del 
lado derecho se añadio su información.

Debajo del boton ''',"en")
    texto.insert(tk.END, "Iniciar metodo","estilo_btn")
    texto.insert(tk.END, ''', hay tres botones que dicen ''',"en")
    texto.insert(tk.END, '''"reactivo", "paso" y "banner"\n''',"estilo_btn")
    texto.insert(tk.END, ''' que son los campos que actualmente 
se pueden añadir al metodo''',"en")
    texto.insert(tk.END, '''\n\nRecomendación: Para iniciar su metodo se le recomienda agregar 
banners de precaucion y de Equipo de Protección Personal
antes de  agregar''',"e_rec")
    texto.insert(tk.END, '''"reactivo" y "paso"''',"estilo_btn")
    texto.insert(tk.END, '\n\nBoton "Reativo\n"',"estilo_rojo")
    texto.insert(tk.END, '''El boton reactivo permite añadir materias primas al metodo
la información que el programa le pedirá sobre su reactivo es:

-Numero de Inventario
-Descripcion fisica del reactivo
-Pictogramas (en caso de haber)
-Indicacion
-Revisión

Indicación se refiere a que debe hacer el operador con ese material
Ejemplo 1: "Agregue el 15-101 a su tina de proceso, sin agitacion"
Ejemplo 2: "Adicione bajo agitacion el 25-501, 15 minutos 
	antes de finalizar su proceso
Ejemplo 3: DIvida la cantidad de 15-515 en 10 partes  y adicionelos 
	en intervalos de 5 minutos

Revisión se refiere a que debe revisar el operador sobre el material
Ejemplo 1: "revise que el material no tenga particulas"
Ejemplo 2: "El material debe ser claro y sin particulas"
Boton "Libreria de Reactivos"
este boton despliega un mini menu de los reactivos existente
facilita el ingreso de datos al metodo de fabricación

una vez terminado de escribir su reactivo, de click en el boton ''',"en")
    texto.insert(tk.END, "agregar","estilo_btn")
    texto.insert(tk.END, ''' para agregar este reactivo al metodo''',"en")
    texto.insert(tk.END, '\n\nBoton "Paso"\n',"estilo_rojo")
    texto.insert(tk.END, '''
"Paso" Se refiere a una instrucción larga, una nota, una advertencia
o una precaución, es un texto de una longitud considerable y que no
necesariamente tiene que ver con algun material, puede ser lo que se
necesite comunicar al operador

una vez terminado de escribir su instrucción, de click en el boton
"agregar" para agregar este paso al metodo''',"en")

    texto.insert(tk.END, '\n\nBoton "Banner\n"',"estilo_rojo")
    texto.insert(tk.END, '''"Banner" Es una imagen ancha de dimensiones de 60 de alto x 600 de ancho 
pixeles (px) y es un recurso visual utilizado para indicar 
alguna instruccion que normalmente se repite en muchos productos

Hay un menu que se despliega hacia abajo con los banners predeterminados
por el programa de los cuales puede elegir a libertad, si desea 
visualizar alguna de estas imagenes puede dar click en el boton ''',"en")
    texto.insert(tk.END, '"visualizar" ',"estilo_btn")
    texto.insert(tk.END, '''para obtener una vista previa del banner y si desea añadirlo se da click
en el boton agregar.''',"en")
    texto.insert(tk.END, '''Si desea añadir un nuevo banner
de click en el boton "Seleccionar imagen" y le pedirá el programa que 
le indique la ruta de donde se encuentra su imagen en el computador y se
añadira automaticamente sin tener que presionar el boton''',"en")
    texto.insert(tk.END, ' "agregar" ',"estilo_btn")
    texto.insert(tk.END, '''
Con estos 3 botones usted puede ir armando el metodo dando click sobre ellos

Si agrego un ''',"en")
    texto.insert(tk.END, '''"reactivo", "paso" o "banner" ''',"estilo_btn")
    texto.insert(tk.END, '''incorrecto y necesita quitarlo,
seleccionelo del recuadro de la derecha hasta que se ponga azul y una vez 
seleccionado, oprima el boton "Quitar ultimo elemento", este boton elimina''',"en")
    texto.insert(tk.END, ''' "reactivo" y "paso" ''',"estilo_btn")
    texto.insert(tk.END, '''al seleccionarlos
Si ha completado su metodo de  fabricación, guardelo presionando el boton''',"en")
    texto.insert(tk.END, ' "Guardar Información" ',"estilo_btn")
    texto.insert(tk.END, '''y verá que la pantalla se cerrará, despues de guardarlo
presone el boton actualizar que se encontrará en amarillo, una vez presionado
aparecerá el producto en el recuadro del ladi izquierdo del menu principal
hasta abajo, en ese momento ya puede modificarlo, excelizarlo o eliminarlo.\n''',"en")
    texto.insert(tk.END, '''\nComo editar un Metodo de fabricacion?''',"estilo_rojo")
    texto.insert(tk.END, '''\n\nPresione el boton ''',"en")
    texto.insert(tk.END, ''' "Editar un metodo existente" ''',"estilo_btn")
    texto.insert(tk.END, '''en la ventana principal y 
se abrira una ventana nueva. En la parte superior izquierda verá un menu de 
texto que se despliega hacia abajo indicando los nombres de los productos.
seleccione el producto que desea editar y vera que los campos vacios
se llenan con la información del producto que añadió

Para editar algo sobre la información basica, solo modifique el campo donde 
tuvo el error, si desea modificar algun campo del metodo (''',"en")
    
    texto.insert(tk.END, '''"reactivo", "paso" y "banner"''',"estilo_btn")
    texto.insert(tk.END, '''), seleccione el campo que usted crea y una
vez selecionado, clickee el boton que dice ''',"en")
    texto.insert(tk.END, '''"Editar bloque"''',"estilo_btn")
    texto.insert(tk.END, ''', inmediatamente
se abrira una ventana con campos en donde se encuentra la información del 
bloque, usted puede modificar la informacion del bloque y para guardar el
cambio realizado de click en ''',"en")
    texto.insert(tk.END, "guardar","estilo_btn")
    texto.insert(tk.END, '''Si desea eliminar un pedazo de informacion, (''',"en")
    texto.insert(tk.END, '''"reactivo", "paso" y "banner"''',"estilo_btn")
    texto.insert(tk.END, ''')
seleccionelo hasta que se ponga en azul y de click en el boton''',"en") 
    texto.insert(tk.END, '''"Eliminar bloque"''',"estilo_btn")
    texto.insert(tk.END, '''
Si desea añadir mas información al mismo metodo, seleccione el bloque
anterior a la posicion que usted desea

EJemplo:
Si yo quiero añadir un paso entre estos 2 reactivos
selecciono el superior de donde yo lo quiero adjuntar
selecciono el 15-443

//////////////x15-443///////////////////////
	x15-540
	
	["añadir bloque"]''',"en")
    texto.insert(tk.END, '''
y le doy click en ''',"en")
    texto.insert(tk.END, '''"añadir bloque"''',"estilo_btn")
    texto.insert(tk.END, '''
Inmediatamente se abrira una nueva ventana con un menu de texto
desplegable con los 3 tipos de información que maneja el programa.
Seleccione que información necesita, rellene los campos que el programa le 
pide y de click en ''',"en")
    texto.insert(tk.END, '"guardar"',"estilo_btn")
    texto.insert(tk.END, ''' le avisará el programa que se ha añadido 
la informacion.

Una vez que usted ha realizado los cambios pertinentes, proceda a
clickear ''',"en")
    texto.insert(tk.END, "Guardar metodo","en")
    texto.insert(tk.END, ''' y se cerrará la ventana, y de click en el boton''',"en")
    texto.insert(tk.END, "actualizar", "estilo_btn")
    texto.insert(tk.END, "¿Como volver a Excel un metodo de fabricación?","estilo_rojo")
    texto.insert(tk.END, '''\n\nPara crear un archivo excel, selecciona en la ventana principal 
el producto que usted desee y una vez seleccionado, de click en 
el boton que dice ''',"en")
    texto.insert(tk.END, '"excelizar"',"estilo_btn")
    texto.insert(tk.END, ''' y revise en la carpeta donde este
el programa de los metodos de fabricación\n\n''',"en")
    texto.insert(tk.END, "¿Cómo eliminar un producto?", "estilo_rojo")
    texto.insert(tk.END, '''\n\nPara eliminar un archivo excel, selecciona en la ventana principal 
el producto que usted desee y una vez seleccionado, de click en 
el boton que dice ''',"en")
    texto.insert(tk.END, '"eliminar"',"estilo_rojo")
    texto.insert(tk.END, ''' y revise si el producto desaparece''',"en")

    ventana.mainloop()

