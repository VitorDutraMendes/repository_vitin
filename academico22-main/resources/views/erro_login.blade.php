@extends('layouts.base')

@section('conteudo')
<div class="w-auto col-md-4 centered container_login">
    <h5 class="row justify-content-center text-danger">ERRO DE LOGIN</h5>
    <div class="row justify-content-center">
        <img src="{{ asset('imgs/usuario.jpg') }}" id="imgUser" />
    </div>
    <!-- form action="http://10.100.16.33/logar.php" method="post" -->
    <form action="{{ route('/') }}" method="get" id="formLogin">
        @csrf
        <div class="row justify-content-center">
            <H1 align="center" class='text-danger'>Usuário ou senha inválidos!</H1>
        </div>
        <button type="submit" class="btn btn-outline-primary">Retornar</button>
    </form>
</div>
@endsection