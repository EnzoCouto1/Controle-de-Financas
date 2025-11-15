// frontend/src/components/EditTransactionModal.jsx

import React, { useState, useEffect } from 'react';
import api from '../api';

// --- Estilos CSS para o Modal (simples) ---
const modalStyles = {
    position: 'fixed',
    top: 0,
    left: 0,
    width: '100%',
    height: '100%',
    backgroundColor: 'rgba(0, 0, 0, 0.5)',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    zIndex: 1000,
};

const modalContentStyles = {
    backgroundColor: 'white',
    padding: '25px',
    borderRadius: '8px',
    boxShadow: '0 4px 8px rgba(0,0,0,0.1)',
    width: '90%',
    maxWidth: '500px',
};
// --- Fim dos Estilos ---


const EditTransactionModal = ({ transaction, categories, onClose, onUpdateSuccess }) => {
    
    // 1. Estado do formulário, inicializado com os dados da transação
    const [formData, setFormData] = useState({
        description: '',
        amount: '',
        category_id: '',
    });
    const [message, setMessage] = useState('');

    // 2. Popula o formulário quando a 'transaction' (prop) muda
    useEffect(() => {
        if (transaction) {
            setFormData({
                description: transaction.description,
                amount: transaction.amount,
                category_id: transaction.category.id, // Pega o ID da categoria da transação
            });
        }
    }, [transaction]);

    // 3. Handler para mudanças no input
    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prev => ({ ...prev, [name]: value }));
    };

    // 4. Handler para salvar (Submit)
    const handleSubmit = async (e) => {
        e.preventDefault();
        setMessage('Salvando...');

        try {
            // 5. Chama a API PATCH (autenticada)
            await api.patch(`/transactions/${transaction.id}`, {
                description: formData.description,
                amount: parseFloat(formData.amount),
                category_id: parseInt(formData.category_id),
            });

            setMessage('Atualizado com sucesso!');
            
            // 6. Atraso para o usuário ver a mensagem antes de fechar
            setTimeout(() => {
                onUpdateSuccess(); // Recarrega os dados no Home
                onClose(); // Fecha o modal
            }, 1000);

        } catch (error) {
            console.error('Erro ao atualizar:', error);
            setMessage(`Erro: ${error.response?.data?.detail || 'Falha ao salvar.'}`);
        }
    };

    if (!transaction) return null; // Não renderiza nada se não houver transação

    return (
        <div style={modalStyles} onClick={onClose}>
            <div style={modalContentStyles} onClick={(e) => e.stopPropagation()}>
                <h3>Editar Transação (ID: {transaction.id})</h3>
                <form onSubmit={handleSubmit}>
                    <div>
                        <label>Categoria:</label>
                        <select
                            name="category_id"
                            value={formData.category_id}
                            onChange={handleChange}
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
                            name="description"
                            value={formData.description}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <br />
                    <div>
                        <label>Valor (R$):</label>
                        <input
                            type="number"
                            name="amount"
                            value={formData.amount}
                            onChange={handleChange}
                            min="0.01"
                            step="0.01"
                            required
                        />
                    </div>
                    <br />
                    <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                        <button type="submit">Salvar Alterações</button>
                        <button type="button" onClick={onClose} style={{ backgroundColor: '#6c757d', color: 'white' }}>
                            Cancelar
                        </button>
                    </div>
                </form>
                {message && <p style={{ color: message.startsWith('Erro') ? 'red' : 'green', marginTop: '10px' }}>{message}</p>}
            </div>
        </div>
    );
};

export default EditTransactionModal;