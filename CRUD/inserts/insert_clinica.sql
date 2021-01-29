delimiter //
create function clinica_maximo()
    returns int
begin
    declare id_cli int;
    select max(id) into id_cli from clinicas;
    if id_cli is Null then
        return 1;
    else 
        set id_cli = id_cli + 1;
        return id_cli;
    end if;
end; //
delimiter ;

delimiter //
create function insertar_clinica(_nombre varchar(50), _ciudad varchar(50))
    returns int
begin
    declare _cod_postal int;
    declare _id int;

    select codigo_postal into _cod_postal from ciudad where nombre = _ciudad;
    select clinica_maximo() into _id;
    insert into clinicas (id, nombre, cod_postal) values(_id, _nombre, _cod_postal);
    return _id;
end; //
delimiter ;