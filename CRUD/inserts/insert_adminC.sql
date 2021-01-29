delimiter //
create function insertar_adminC(_nro_documento int, _tipo_documento varchar(30), _nombre varchar(40), _apellidos varchar(40), _correo varchar(50), _telefono varchar(10), _clinica int, _contrasena varchar(90))
    returns int
begin
    declare tip_documento int;
    declare corre varchar(50);
    declare id int;

    select nro_documento into id from administrador_clinica where nro_documento = _nro_documento;
    if id is Null then
        select correo into corre from administrador_clinico where correo = _correo;
        if corre is Null then
            select id into tip_documento from tipo_documento where nombre = _tipo_documento;
            insert into administrador_general (nro_documento, tipo_d, nombre, apellidos, correo, telefono, id_clinica, contrasena) values (_nro_documento, tip_documento, _nombre, _apellidos, _correo, _telefono, _clinica, _contrasena);
            return 1;
        else
            return 0;
        end if;
    else
        return 2;
    end if;
end; //
delimiter ;