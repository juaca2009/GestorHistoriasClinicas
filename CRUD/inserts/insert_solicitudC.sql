--funcion encargada de obtener el maximo id de la tabla de solicitudes, retorna el maximo id+1  
delimiter //
create function solicitud_maximo()
    returns int
begin
    declare id_sol int;
    select max(id) into id_sol from solicitudes;
    if id_sol is Null then
        return 1;
    else 
        set id_sol = id_sol + 1;
        return id_sol;
    end if;
end; //
delimiter ;

--funcion encargada de insertar una nueva solicitud clinica 
--retorna 1 si se realizo la insercion
--retorna 0 si ya esa clinica posee una solicitud 
delimiter //
create function insertar_solicitudC(_nombre varchar(60), _direccion varchar(40), _ciudad varchar(50), _correo varchar(50))
    returns int
begin
    declare _cod_postal int;
    declare _id int;
    declare _nomb varchar(60);

    select codigo_postal into _cod_postal from ciudad where nombre = _ciudad;
    select solicitud_maximo() into _id;
    select nombre into _nomb from solicitudes where nombre = _nombre;
    if _nomb is Null then 
        insert into solicitudes (id, nombre, direccion, cod_postal, correo) values (_id, _nombre, _direccion, _cod_postal, _correo);
        return 1;
    else
        return 0;
    end if;
end; //
delimiter ;

