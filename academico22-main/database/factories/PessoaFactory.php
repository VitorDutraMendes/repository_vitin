<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\Pessoa>
 */
class PessoaFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    public function definition()
    {
        return [
            'tipo' => fake()->randomElement(['A', 'F', 'P']),
            'matricula' => fake()->unique()->randomNumber(7, true),
            'nome' => fake()->name(),
            'cpf' => fake()->cpf(false),
            'senha' => "123456",
            'email' => fake()->unique()->safeEmail(),
            'telefone' => fake()->phoneNumber(),
        ];
    }
}
