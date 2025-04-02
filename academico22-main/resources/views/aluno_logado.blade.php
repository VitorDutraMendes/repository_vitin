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
          <a class="nav-link" href="{{ route('/') }}">Sair</a>
        </li>
      </ul>
      <div class="my-2 my-lg-0">
        Usuário: {{$usuario->nome}}
      </div>
    </div>
  </nav>
  @endsection

  @section('conteudo')
  <div class="w-auto container_login">
    <span class='titulo '> Aluno Logado com sucesso!</span>
  </div>
  @endsection