CREATE DATABASE IF NOT EXISTS escola_db;
USE escola_db;

CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) UNIQUE NOT NULL,
    senha VARCHAR(100) NOT NULL,
    tipo ENUM('admin','professor','aluno') NOT NULL
);

CREATE TABLE IF NOT EXISTS alunos (
    id_aluno INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INT NOT NULL,
    turma VARCHAR(50) NOT NULL,
    id_usuario INT,
    FOREIGN KEY (id_usuario)
        REFERENCES usuarios(id_usuario)
);

CREATE TABLE IF NOT EXISTS professores (
    id_professor INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    disciplina VARCHAR(100),
    id_usuario INT,
    FOREIGN KEY (id_usuario)
        REFERENCES usuarios(id_usuario)
);

CREATE TABLE IF NOT EXISTS notas (
    id_nota INT AUTO_INCREMENT PRIMARY KEY,
    id_aluno INT NOT NULL,
    nota FLOAT NOT NULL,
    FOREIGN KEY (id_aluno) REFERENCES alunos(id_aluno)
);



INSERT INTO usuarios (usuario, senha, tipo)
VALUES ('admin1', 'josefa', 'admin');

INSERT INTO usuarios (usuario, senha, tipo)
VALUES ('professor', 'zion', 'professor');

DESCRIBE notas;

SELECT * FROM alunos;

SELECT * FROM notas;