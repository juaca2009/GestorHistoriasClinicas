--funcion encargada de actualizar la informacion de los pacientes 
--retorna 0 si la operacion fue exitosa, retorna 1 si no se proporciona un telefono
--retorna 2 si no se proporciona una contraseña
delimiter //
create function actualizar_pacientes(_id int, _correo varchar(50), _telefono varchar(10), _ciudad varchar(50), _contrasena varchar(10))
    returns int
begin
    declare _cod_postal int;

    select codigo_postal into _cod_postal from ciudad where nombre = _ciudad;
    if _telefono is not null then
        if _contrasena is not null then
            update paciente set correo = _correo, telefono = _telefono, cod_postal = _cod_postal, contrasena = _contrasena where id = _id;
            return 0;
        else 
            return 1;
        end if;
    else
        return 2;
    end if;
end; //
delimiter ;