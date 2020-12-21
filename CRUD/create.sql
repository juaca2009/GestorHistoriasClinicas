--tabla departamentos
create table departamentos(
    id int primary key,
    nombre varchar(50) not null
);

--tabla ciudades
create table ciudad(
    codigo_postal int primary key,
    nombre varchar(50) not null,
    id_departamento int references departamentos(id)
);

--tabla tipo de documentos
create table tipo_documento(
    id int primary key,
    nombre varchar(50) not null
);

-- tabla tipo de especializaciones
create table tipo_especializacion(
    id int primary key,
    nombre varchar(100) not null
);

-- tabla solicitudes 
create table solicitudes(
    id int primary key,
    nombre varchar(60) not null,
    direccion varchar(30),
    cod_postal int references ciudad(codigo_postal),
    correo varchar(50) not null,
    cant_personas int
);

-- tabla clinicas 
create table clinicas(
    id int primary key,
    nombre varchar(50) not null,
    descripcion varchar(200),
    cod_postal int references ciudad(codigo_postal)
);

-- tabla administradores generales 
create table administrador_general(
    nro_documento int primary key,
    tipo_d int references tipo_documento(id),
    nombre varchar(40) not null,
    apellidos varchar(80) not null,
    correo varchar(50),
    telefono varchar(10) not null,
    cod_postal int references ciudad(codigo_postal),
    contrasena varchar(10) not null
);

--tabla medicos
create table medicos(
    nro_documento int primary key,
    tipo_d int references tipo_documento(id),
    nombre varchar(40) not null,
    apellidos varchar(80) not null,
    correo varchar(50),
    telefono varchar(10) not null,
    id_clinica int references clinicas(id),
    id_espc int references tipo_especializacion(id),
    contrasena varchar(10) not null
);

-- tabla administradores clinicos
create table administrador_clinica(
    nro_documento int primary key,
    tipo_d int references tipo_documento(id),
    nombre varchar(40) not null,
    apellidos varchar(80) not null,
    correo varchar(50),
    telefono varchar(10) not null,
    id_clinica int references clinicas(id),
    contrasena varchar(10) not null
);

-- tabla historias clinicas 
create table historias_clinicas(
    id int primary key,
    nro_documento int not null,
    nombre varchar(40) not null,
    apellidos varchar(40) not null,
    correo varchar(50),
    telefono varchar(10) not null,
    id_clinica int references clinicas(id)
);

-- tabla entradas a la historia clinica
create table entradas(
    id int primary key,
    sintomas varchar(500) not null,
    fecha date not null,
    operaciones_recientes varchar(500),
    diagnosticos varchar(500) not null,
    medicamentos varchar(500),
    examenes varchar(500),
    id_historias int references historias_clinicas(id)
);

-- tabla paciente 
create table paciente(
    nro_documento int primary key,
    tipo_d int references tipo_documento(id),
    nombre varchar(40) not null,
    apellidos varchar(80) not null,
    correo varchar(50),
    telefono varchar(10) not null,
    id_clinica int references clinicas(id),
    id_historias int references historias_clinicas(id),
    contrasena varchar(10) not null
);
