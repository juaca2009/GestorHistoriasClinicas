delimiter //
create function insertar_adminP(_nro_documento int, _tipo_documento varchar(30), _nombre varchar(40), _apellidos varchar(40), _correo varchar(50), _telefono varchar(10), _ciudad varchar(50), _contrasena varchar(10))
    returns int
begin  
    declare tip_documento int;
    declare _cod_postal int;
    declare id int;
    declare corre varchar(50);

    select nro_documento into id from administrador_general where nro_documento = _nro_documento;
    if id is Null then
        select correo into corre from administrador_general where correo = _correo;
        if corre is Null then
            select codigo_postal into _cod_postal from ciudad where nombre = _ciudad;
            select id into tip_documento from tipo_documento where nombre = _tipo_documento;
            insert into administrador_general (nro_documento, tipo_d, nombre, apellidos, correo, telefono, cod_postal, contrasena) values (_nro_documento, tip_documento, _nombre, _apellidos, _correo, _telefono, _cod_postal, _contrasena);
            return 1;
        else
            return 0;
        end if;
    else
        return 2;
    end if;
end; //
delimiter ;