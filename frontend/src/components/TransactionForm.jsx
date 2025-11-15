// frontend/src/components/TransactionForm.jsx

import React, { useState, useEffect } from 'react';
import api from '../api';

const TransactionForm = ({ categories, onTransactionCreated }) => {
    // Estados do formulário
    const [description, setDescription] = useState('');
    const [amount, setAmount] = useState('');
    const [categoryId, setCategoryId] = useState('');
    const [message, setMessage] = useState('');

    // Define a primeira categoria como padrão
    useEffect(() => {
        if (categories.length > 0) {
            setCategoryId(categories[0].id);
        }
    }, [categories]);

    // Função para enviar o formulário
    const handleSubmit = async (e) => {
        e.preventDefault();
        setMessage('Salvando...');

        try {
            // 1. Faz a chamada POST (autenticada) para o backend
            const response = await api.post('/transactions/', {
                description: description,
                amount: parseFloat(amount),
                category_id: parseInt(categoryId),
                // O backend define a data
            });

            setMessage(`Transação salva! ID: ${response.data.id}`);
            
            // 2. Limpa o formulário
            setDescription('');
            setAmount('');
            
            // 3. Avisa o componente 'Home' que uma nova transação foi criada
            if (onTransactionCreated) {
                onTransactionCreated();
            }

        } catch (error) {
            console.error('Erro ao criar transação:', error);
            const detail = error.response?.data?.detail || 'Falha ao salvar.';
            setMessage(`Erro: ${detail}`);
        }
    };

    // Não renderiza o formulário se as categorias ainda não foram carregadas
    if (categories.length === 0) {
        return <p>Carregando categorias...</p>;
    }

    return (
        <div style={{ padding: '20px', border: '1px solid #eee', borderRadius: '5px', marginTop: '20px' }}>
            <h3>Registrar Nova Transação</h3>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Categoria:</label>
                    <select
                        value={categoryId}
                        onChange={(e) => setCategoryId(e.target.value)}
                        required
                    >
                        {categories.map(cat => (
                            <option key={cat.id} value={cat.id}>
                                {cat.name} ({cat.type})
                            </option>
                        ))}
                    </select>
                </div>
                <br />
                <div>
                    <label>Descrição:</label>
                    <input
                        type="text"
                        placeholder="Ex: Almoço, Salário"
                        value={description}
                        onChange={(e) => setDescription(e.target.value)}
                        required
                    />
                </div>
                <br />
                <div>
                    <label>Valor (R$):</label>
                    <input
                        type="number"
                        placeholder="Ex: 50.00"
                        value={amount}
                        onChange={(e) => setAmount(e.target.value)}
                        min="0.01"
                        step="0.01"
                        required
                    />
                </div>
                <br />
                <button type="submit">Adicionar Transação</button>
            </form>
            {message && <p style={{ color: message.startsWith('Erro') ? 'red' : 'green', marginTop: '10px' }}>{message}</p>}
        </div>
    );
};

export default TransactionForm;