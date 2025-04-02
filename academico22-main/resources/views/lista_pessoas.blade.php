@extends('layouts.base')

@section('navbar')
<div class="menu">
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item">
          <a class="nav-link" href="#">opc1</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">opc2</a>
        </li>

        <li class="nav-item">
          <a class="nav-link" href="{{ route('/') }}">Voltar</a>
        </li>
      </ul>
      <div class="my-2 my-lg-0">
        Usuário:
      </div>
    </div>
  </nav>
  @endsection

  @section('conteudo')
  <div class="w-auto container_login">
    <table class="table table-striped ">
      <thead class="thead-dark">
        <tr>
          <th>Nome</th>
          <th>Matrícula</th>
          <th>Tipo</th>
          <th>Cpf</th>
          <th>Email</th>
          <th>Telefone</th>
          <th>Senha</th>
        </tr>
      </thead>
      <tbody>
        @foreach ($pessoas as $pessoa)
        <tr>
          <td> {{ $pessoa->nome}}</td>
          <td> {{ $pessoa->matricula}}</td>
          <td> {{ $pessoa->tipo}} </td>
          <td> {{ $pessoa->cpf}} </td>
          <td> {{ $pessoa->email}} </td>
          <td> {{ $pessoa->telefone}} </td>
          <td> {{ $pessoa->senha}} </td>
        </tr>
        @endforeach
      </tbody>
    </table>
  </div>
  @endsection