<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class CadastroController extends Controller
{
    public function lista_pessoas()
    {

        $pessoas = \App\Models\Pessoa::get();
        return view('lista_pessoas')->with(compact(['pessoas']));
    }
}
