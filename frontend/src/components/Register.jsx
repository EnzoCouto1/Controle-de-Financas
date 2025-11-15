// frontend/src/components/Register.jsx

import React, { useState } from 'react';
import api from '../api';

const Register = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage('Aguarde...');

    try {
      // Faz a chamada POST para o endpoint de cadastro no Backend
      const response = await api.post('/users/', { 
        email, 
        password 
      });

      setMessage(`Sucesso! Usuário cadastrado: ID ${response.data.id}`);
      setEmail('');
      setPassword('');

    } catch (error) {
      console.error(error);
      const detail = error.response?.data?.detail || 'Erro ao conectar com a API.';
      setMessage(`Erro: ${detail}`);
    }
  };

  return (
    <div>
      <h2>Cadastro de Usuário</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="email"
          placeholder="E-mail"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <br />
        <input
          type="password"
          placeholder="Senha"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <br />
        <button type="submit">Cadastrar</button>
      </form>
      {message && <p style={{ color: message.startsWith('Sucesso') ? 'green' : 'red' }}>{message}</p>}
    </div>
  );
};

export default Register;