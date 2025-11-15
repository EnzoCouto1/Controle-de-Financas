import React, { useState, useEffect } from 'react';
import Login from './components/Login';
import Register from './components/Register';
import Home from './components/Home'; // 1. Garante a importação do componente Home
import './App.css'; 

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [showRegister, setShowRegister] = useState(false);

  useEffect(() => {
    // Verifica se o token já existe no localStorage ao carregar a página
    const token = localStorage.getItem('accessToken');
    if (token) {
      setIsLoggedIn(true);
    }
  }, []);

  const handleLogin = (token) => {
    // Chamado após o login ser bem-sucedido
    setIsLoggedIn(true);
  };
  
  const handleLogout = () => {
      localStorage.removeItem('accessToken');
      setIsLoggedIn(false);
  };

  if (isLoggedIn) {
    return (
        <div className="App">
            <h1>TESTE DE ATUALIZAÇÃO</h1>
            <Home onLogout={handleLogout} /> 
        </div>
    );
  }

  // MODO NÃO AUTENTICADO: Mostrar Login ou Cadastro
  const toggleView = () => setShowRegister(!showRegister);

  return (
    <div className="App">
        <h1>Sistema de Controle de Finanças</h1>
        
        {showRegister ? (
            <Register />
        ) : (
            <Login onLogin={handleLogin} />
        )}

        <button onClick={toggleView} style={{ marginTop: '20px' }}>
            {showRegister ? 'Voltar para Login' : 'Ir para Cadastro'}
        </button>
    </div>
  );
}

export default App;