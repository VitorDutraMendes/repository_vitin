-- phpMyAdmin SQL Dump
-- version 5.3.0-dev
-- https://www.phpmyadmin.net/
--
-- Host: 192.168.30.23
-- Tempo de geração: 11/10/2022 às 15:07
-- Versão do servidor: 8.0.18SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `academico22`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `alunos`
--

CREATE TABLE `alunos` (
  `id` int(11) NOT NULL,
  `matricula` varchar(7) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `cpf` varchar(11) NOT NULL,
  `email` varchar(30) NOT NULL,
  `telefone` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Despejando dados para a tabela `alunos`
--

INSERT INTO `alunos` (`id`, `matricula`, `nome`, `cpf`, `email`, `telefone`) VALUES
(1, '234567', 'José da Silva', '11111111111', 'jose.silva@gmail.com', '1111111'),
(2, '0065978', 'Marcos Davi Carneiro Lima', '16485889647', 'mdclima12005@gmail.com', '995019116'),
(3, '0000000', 'Fulano de Tal', '12345678900', 'fulanodeta@gmail.com', '111111111111'),
(47, '', '', '', '', ''),
(5, '5220', 'Kleber Do Pneu', '0636542120', 'Kleberdopneu@gmail.com', '31999718730'),
(6, '1345673', 'Maya Andrade Saraiva dos Santos ', '98654398732', 'mayasantos@gmail.com', '986543987'),
(7, '0065986', 'Maria Eduarda de Souza', '11111111111', 'fulana2013@hotmail.com', '98765678'),
(8, '0051041', 'kid bengala delas', '25815115278', 'flavindopneu@hotmail.com', '031969694444'),
(9, '666666', 'smt smt smt smt smt smt smt smt', '11223358888', 'mrflufyy@gmail.com', '31 3673-2769'),
(10, '0066137', 'Xandão Lana Rola', '12345678701', 'mauriocio@gmail.com', '031963735139'),
(11, '2424242', '♍︎□︎❍︎♓︎ □︎ ♍︎◆︎ ♎︎♏︎ ❑︎◆︎♏︎❍︎ ●︎♏︎◆︎', '24242424242', 'ninguem@gmail.com', '031994653212'),
(12, '0065736', 'Cremilda Silva Rego', '16916916969', 'jairbolsonaro@gmail.com', '190'),
(13, '0065736', 'Soca Fofo', '6969696969', 'batemeigo@yahoo.com.br', '696969');

-- --------------------------------------------------------

--
-- Estrutura para tabela `faltas`
--

CREATE TABLE `faltas` (
  `id` int(11) NOT NULL,
  `id_aluno` int(11) NOT NULL,
  `mes` int(11) NOT NULL,
  `faltas` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Despejando dados para a tabela `faltas`
--

INSERT INTO `faltas` (`id`, `id_aluno`, `mes`, `faltas`) VALUES
(1, 1, 2, 5),
(2, 7, 5, 2);

-- --------------------------------------------------------

--
-- Estrutura para tabela `notas`
--

CREATE TABLE `notas` (
  `id` int(11) NOT NULL,
  `id_aluno` int(11) NOT NULL,
  `nota_1` decimal(3,1) DEFAULT NULL,
  `nota_2` decimal(3,1) DEFAULT NULL,
  `nota_3` decimal(3,1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Despejando dados para a tabela `notas`
--

INSERT INTO `notas` (`id`, `id_aluno`, `nota_1`, `nota_2`, `nota_3`) VALUES
(1, 2, '5.0', NULL, NULL);

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `alunos`
--
ALTER TABLE `alunos`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `faltas`
--
ALTER TABLE `faltas`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `notas`
--
ALTER TABLE `notas`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `alunos`
--
ALTER TABLE `alunos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=317641653;

--
-- AUTO_INCREMENT de tabela `faltas`
--
ALTER TABLE `faltas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de tabela `notas`
--
ALTER TABLE `notas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
