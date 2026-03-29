# Ecommerce---Entrega-final-de-portafolio

Preguntas:
    ¿Es mejor para mi separar la app de inventario admin y acciones que realice el usuario?
    ¿Podria separar acciones según la app o el usuario?

Requerimientos y alcances del proyecto:
    1.Usuario(cliente): iniciar sesion, acceder al catalogo y operar el carrito
    1.1Administrador: Iniciar sesion, acceder al area de gestion del inventario
        Restriccion de acceso al cliente para la url de inventario
    2.Mostrar catalogo de productos mediante el ORM de django
    2.1 Productos CRUD por Adminisrtador
    3.Carrito de compra:
        -Agregar producto:
        -Quitar producto:
        -Actualizar cantidad:
        -Mostrar subtotal y total
    3.1Confirmacion de compra:
        -Registrar una orden con sus items
        -Asociar la orden al usuario autenticado
            El flujo catalogo-carrito-confirmacion funcione de forma estable
    4. Mantener front consistente uso de bootstrap
    4.1 Navegacion clara entre:
        -Catalogo
        -detalle producto
        -carrito
        -login/logout
        -administrador de productos
    5. Validacion y mensajes:
        -Validaciones basicas en formularios, precio, cantidades.
        -Mensajes de exito o error

