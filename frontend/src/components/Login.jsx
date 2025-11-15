// frontend/src/components/Login.jsx

import React, { useState } from 'react';
import api from '../api'; // Usamos a instância Axios configurada

const Login = ({ onLogin }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage('Aguarde...');

    try {
      // O FastAPI espera o formato x-www-form-urlencoded no endpoint /token
      const formData = new URLSearchParams();
      formData.append('username', email); // O FastAPI usa 'username' para o email
      formData.append('password', password);
      
      // Faz a chamada POST para o endpoint de login
      const response = await api.post('/token', formData, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      });

      const token = response.data.access_token;
      
      // 1. Armazenar o token no navegador
      localStorage.setItem('accessToken', token);
      
      // 2. Avisar o App.jsx que o login foi bem-sucedido
      onLogin(token); 

      setMessage('Login bem-sucedido! Token salvo.');

    } catch (error) {
      console.error('Erro de Login:', error);
      const detail = error.response?.data?.detail || 'Credenciais inválidas ou erro de rede.';
      setMessage(`Erro: ${detail}`);
    }
  };

  return (
    <div>
      <h2>Login</h2>
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
        <button type="submit">Entrar</button>
      </form>
      {message && <p style={{ color: message.startsWith('Sucesso') || message.startsWith('Login') ? 'green' : 'red' }}>{message}</p>}
      <p>Ainda não tem conta? Clique em **Cadastrar**.</p>
    </div>
  );
};

export default Login;