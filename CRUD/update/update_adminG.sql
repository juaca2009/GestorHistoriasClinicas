--funcion encargada de actualizar la informacion personal de los administradores generales
--retorna 0 si la operacion fue exitosa, retorna 1 si no se proporciona un telefono
--retorna 2 si no se proporciona una contraseña
delimiter //
create function actualizar_adminG(_id int, _correo varchar(50), _telefono varchar(10), _ciudad varchar(50))
    returns int
begin
    declare _cod_postal int;
    declare corre varchar(50);
    declare corre2 varchar(50);

    select correo into corre from administrador_general where correo = _correo;
    select correo into corre2 from administrador_general where correo = _correo and nro_documento = _id;
    if corre is Null or corre2 = _correo then
        if _telefono is not null then
            select codigo_postal into _cod_postal from ciudad where nombre = _ciudad;
            update administrador_general set correo = _correo, telefono = _telefono, cod_postal = _cod_postal where nro_documento = _id;
            return 1;
        else 
            return 0;
        end if;
    else
        return 2;
    end if;
end; //
delimiter ;