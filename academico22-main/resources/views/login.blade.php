@extends('layouts.base')

@section('conteudo')
<div class="w-auto col-md-4 centered container_login">
    <h5 class="row justify-content-center">LOGIN</h5>
    <div class="row justify-content-center">
        <img src="{{ asset('imgs/usuario.png') }}" id="imgUser" />
    </div>
    <!-- form action="http://10.100.16.33/logar.php" method="post" -->
    <form action="{{ route('logar') }}" method="post" id="formLogin">
        @csrf
        <div class="form-group">
            <label for="usuario">Matrícula:</label>
            <input type="text" class="form-control" id="matricula" name="matricula" placeholder="Matrícula do Usuário">
        </div>

        <div class="form-group">
            <label for="senha">Senha:</label>
            <input type="password" class="form-control" id="senha" name="senha" placeholder="Senha do usuário">
        </div>
        <button type="submit" class="btn btn-outline-primary">Entrar</button>
    </form>
</div>
@endsection