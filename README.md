# todotask
Creación de modelos, vistas y modificaciones para comprobar su funcionamiento en odoo 16.0. 

Se crea la imagen a través de un Dockerfile.
Se crea el docker compose con los datos y campos necesarios para la base de datos y los volumenes.

El módulo se llama "moduloprueba" y su modelo principal es "todo.task". A partir de esto, se crean menús, vistas y demás acciones de prueba para comprender su funcionamiento.
En algunos de los modelos que parten de "todo.task", se hace referencia a otros modelos que pertenecen a "crm_claim", por lo tanto es necesario adjuntar también sus carpetas.

Hay que tener en cuenta que en la creación de "controllers.py", es necesario el siguiente comando de sudo porque sino salta un error de permisos y no nos deja continuar.
" todotask = http.request.env['todo.task'].sudo().create(datos_recibidos) "

Cuando se crea una API en "controllers.py", se utiliza una extensión de postman para poder comprobar su correcto funcionamiento. En este caso, se hace una "New request" y  se escoge el método POST. En el apartado "Body" se escribe lo siguiente:
{
    "categ_id": "10",
    "name": "prueba2",
    "partner_id": "14",
    "team_id": "1",
    "user_id": "1"
}

De esta forma se añadiría este campo con esos datos a la lista de categorías. Si hubiese algún problema, debugeando se podría verificar dónde está el error para poder corregirlo.

*Para el correcto funcionamiento de este código es necesario instalar extensiones en VS Code para odoo, python, github, debug, postman, docker...*
