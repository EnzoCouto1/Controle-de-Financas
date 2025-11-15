// frontend/src/components/CategoryForm.jsx

import React, { useState } from 'react';
import api from '../api';

const CategoryForm = ({ onCategoryCreated }) => {
    // Estados do formulário
    const [name, setName] = useState('');
    const [type, setType] = useState('OUTCOME'); // Padrão: Despesa
    const [message, setMessage] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        setMessage('Salvando...');

        try {
            // 1. Chama a API POST (autenticada) para criar a categoria
            const response = await api.post('/categories/', {
                name: name,
                type: type,
            });

            setMessage(`Categoria '${response.data.name}' salva com sucesso!`);
            
            // 2. Limpa o formulário
            setName('');
            setType('OUTCOME');
            
            // 3. Avisa o 'Home' que uma nova categoria foi criada
            if (onCategoryCreated) {
                onCategoryCreated();
            }

        } catch (error) {
            console.error('Erro ao criar categoria:', error);
            const detail = error.response?.data?.detail || 'Falha ao salvar.';
            setMessage(`Erro: ${detail}`);
        }
    };

    return (
        <div style={{ padding: '20px', border: '1px solid #eee', borderRadius: '5px', marginTop: '20px', backgroundColor: '#f9f9f9' }}>
            <h3>Registrar Nova Categoria</h3>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Tipo:</label>
                    <select
                        value={type}
                        onChange={(e) => setType(e.target.value)}
                        required
                    >
                        <option value="OUTCOME">Despesa (Gasto)</option>
                        <option value="INCOME">Receita (Ganho)</option>
                    </select>
                </div>
                <br />
                <div>
                    <label>Nome da Categoria:</label>
                    <input
                        type="text"
                        placeholder="Ex: Lazer, Moradia, Salário"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                        required
                    />
                </div>
                <br />
                <button type="submit">Adicionar Categoria</button>
            </form>
            {message && <p style={{ color: message.startsWith('Erro') ? 'red' : 'green', marginTop: '10px' }}>{message}</p>}
        </div>
    );
};

export default CategoryForm;