<?php

namespace Database\Seeders;

// use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class DatabaseSeeder extends Seeder
{
    /**
     * Seed the application's database.
     *
     * @return void
     */
    public function run()
    {
        \App\Models\User::factory(10)->create();

        \App\Models\User::factory()->create([
            'name' => 'Test User',
            'email' => 'test@example.com',
        ]);

        \App\Models\Pessoa::factory()->create([
            'nome' => 'Aluno Teste',
            'tipo' => 'A',
            'matricula' => '1111111',
        ]);
        \App\Models\Pessoa::factory()->create([
            'nome' => 'Professor Teste',
            'tipo' => 'P',
            'matricula' => '2222222',
        ]);
        \App\Models\Pessoa::factory()->create([
            'nome' => 'Funcionario Teste',
            'tipo' => 'F',
            'matricula' => '3333333',
        ]);

        \App\Models\Pessoa::factory(5)->create();
    }
}
