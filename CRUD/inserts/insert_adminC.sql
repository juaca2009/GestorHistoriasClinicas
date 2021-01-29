delimiter //
create function insertar_adminC(_nro_documento int, _tipo_documento int, _nombre varchar(40), _apellidos varchar(40), _correo varchar(50), _telefono varchar(10), _clinica int, _contrasena varchar(90))
    returns int
begin
    declare corre varchar(50);
    declare id int;

    select nro_documento into id from administrador_clinica where nro_documento = _nro_documento;
    if id is Null then
        select correo into corre from administrador_clinica where correo = _correo;
        if corre is Null then
            insert into administrador_clinica (nro_documento, tipo_d, nombre, apellidos, correo, telefono, id_clinica, contrasena) values (_nro_documento, _tipo_documento, _nombre, _apellidos, _correo, _telefono, _clinica, _contrasena);
            return 1;
        else
            return 0;
        end if;
    else
        return 2;
    end if;
end; //
delimiter ;