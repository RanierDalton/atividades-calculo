CREATE DATABASE PlcVision;
USE PlcVision;

CREATE TABLE funcionarios (
    idFuncionario INT PRIMARY KEY AUTO_INCREMENT,   
    nomeFuncionario VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    senha VARCHAR(100) NOT NULL,
    cargo VARCHAR(100)
);

CREATE TABLE plc (
    idPlc INT PRIMARY KEY AUTO_INCREMENT,   
    modeloPlc VARCHAR(100) NOT NULL,
    ano INT NOT NULL,
    fkEmpresa INT NOT NULL,
    ADD CONSTRAINT fkEmpresa FOREIGN KEY (fkEmpresa) REFERENCES empresas(idEmpresa)
)

CREATE TABLE empresas (
    idEmpresa INT PRIMARY KEY AUTO_INCREMENT,   
    nomeEmpresa VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    cnpj VARCHAR(100) NOT NULL
);

CREATE TABLE dadosCorriqueiros (
    idDado INT PRIMARY KEY AUTO_INCREMENT,  
    dataHora DATETIME NOT NULL DEFAULT now(),
    temperaturaCpu FLOAT,
    usoCpu FLOAT,
    atividadeCpu FLOAT,
    usoMemoriaRam FLOAT,
    memoriaRamLivre FLOAT,
    velcidadeGiroVentuinha FLOAT,
    fkPlc INT NOT NULL DEFAULT 1,
    ADD CONSTRAINT fkPlc FOREIGN KEY (fkPlc) REFERENCES plc(idPlc)
);

CREATE TABLE alertas (
    idAlerta INT PRIMARY KEY AUTO_INCREMENT,
    fkDado INT NOT NULL,
    nivelAlerta SMALLINT NOT NULL,
    ADD CONSTRAINT fkDado FOREIGN KEY (fkDado) REFERENCES dadosCorriqueiros(idDado),
    ADD CONSTRAINT chkNivelAlerta CHECK IN (0, 1) -- 0 = Atenção, 1 = Crítico
);

INSERT INTO empresas (nomeEmpresa, email, cnpj) VALUES
('Volkswagen', 'contato@volkswagen.com', '12345678000101'),
('Petrobras', 'contato@petrobras.com,br', '98765432000102');

INSERT INTO plc (modeloPlc, ano, fkEmpresa) VALUES
('SIMATIC S7-1200', 2022, 1),
('SIMATIC S7-1500', 2023, 1),
('SIMATIC S7-1200', 2021, 2),
('SIMATIC S7-300', 2020, 2);

INSERT INTO funcionarios (nomeFuncionario, email, senha, cargo) VALUES
('Carlos Eduardo', 'carlos.eduardo@siemens.com', 'senha123', 'Gerente de Manutenção'),
('João Neto', 'joao.neto@siemens.com', 'senha456', 'Técnico de Manutenção');

INSERT INTO dadosCorriqueiros (temperaturaCpu, usoCpu, atividadeCpu, usoMemoriaRam, memoriaRamLivre, velcidadeGiroVentuinha, fkPlc) VALUES
(45.5, 75.3, 80.1, 60.2, 3.5, 2000, 1),
(50.2, 82.7, 85.5, 70.8, 2.1, 2200, 2),
(42.0, 60.4, 70.2, 50.3, 4.2, 1800, 3),
(48.3, 78.1, 79.0, 65.5, 3.0, 2100, 4);