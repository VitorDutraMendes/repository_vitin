<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class LoginController extends Controller
{
    //

    public function logar(Request $request)
    {
        $dados = $request->all();
        //dd($dados);
        //$senha = bcrypt($dados['senha']);
        $senha = $dados['senha'];
        //dd($senha);
        $usuario = \App\Models\Pessoa::where('matricula', $dados['matricula'])->first();
        //dd([$dados['senha'], $senha, $usuario->senha]);
        if ($usuario) {
            if ($usuario->senha == $senha) {
                $tipo = $usuario->tipo;
                switch ($tipo) {
                    case 'A':
                        return view('aluno_logado')->with(compact(['usuario']));
                        break;
                    case 'F':
                        return view('funcionario_logado')->with(compact(['usuario']));
                        break;
                    case 'P':
                        return view('professor_logado')->with(compact(['usuario']));
                        break;
                }
            } else return view('erro_login');
        } else return view('erro_login');
    }
}
