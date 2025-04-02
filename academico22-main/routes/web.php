<?php

use App\Http\Controllers\CadastroController;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\LoginController;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/
/*
Route::get('/', function () {
    return view('welcome');
});
*/

Route::get('/', function () {
    return view('login');
})->name('/');

Route::post('/logar', [LoginController::class, 'logar'])->name('logar');

Route::get('/lista_pessoas', [CadastroController::class, 'lista_pessoas'])->name('/lista_pessoas');
