import React, { useState, useEffect } from 'react';
import api from '../api';
import TransactionForm from './TransactionForm'; 
import EditTransactionModal from './EditTransactionModal';
import CategoryForm from './CategoryForm'; 
import ExpensePieChart from './ExpensePieChart';
import FinancialSummary from './FinancialSummary';

const Home = ({ onLogout }) => {
    const [categories, setCategories] = useState([]);
    const [transactions, setTransactions] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [message, setMessage] = useState(''); // Mensagem global (exclusão, etc.)

    const [editingTransaction, setEditingTransaction] = useState(null); 

    // Função para buscar TODOS os dados
    const fetchData = async () => {
        setLoading(true);
        try {
            const [categoriesResponse, transactionsResponse] = await Promise.all([
                api.get('/categories/'),
                api.get('/transactions/')
            ]);
            
            setCategories(categoriesResponse.data);
            setTransactions(transactionsResponse.data);
            setError(null);

        } catch (err) {
            // ... (código de tratamento de erro existente) ...
            if (err.response && err.response.status === 401) {
                setError('Sessão expirada. Faça login novamente.');
                onLogout();
            } else {
                setError('Falha ao carregar os dados.');
            }
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchData();
    }, [onLogout]);

    // Callback para quando uma transação é CRIADA ou ATUALIZADA
    const handleUpdate = () => {
        setMessage(''); // Limpa mensagens antigas
        fetchData(); // Busca os dados novamente
        setEditingTransaction(null); // Fecha o modal de edição
    };

    const handleDelete = async (transactionId) => {
        // ... (código de exclusão existente) ...
        if (!window.confirm(`Tem certeza que deseja excluir a transação ID ${transactionId}?`)) return;

        try {
            await api.delete(`/transactions/${transactionId}`);
            setMessage('Transação excluída com sucesso!');
            fetchData(); // Recarrega os dados
        } catch (error) {
            // ... (tratamento de erro) ...
            setMessage(`Erro ao excluir: ${error.response?.data?.detail || 'Falha.'}`);
        }
    };

    if (loading) {
        return <p>Carregando dados...</p>;
    }

    return (
        <div className="home-dashboard">
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <h2>Dashboard de Finanças 💰</h2>
                <button onClick={onLogout} style={{ padding: '8px 15px', backgroundColor: '#dc3545', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer' }}>
                    Sair
                </button>
            </div>

            {error && <p style={{ color: 'red', border: '1px solid red', padding: '10px' }}>{error}</p>}
            {message && <p style={{ color: 'green' }}>{message}</p>}
            
            <hr />

            <FinancialSummary transactions={transactions} />

            {/* Passamos 'categories' também para ele poder calcular as cores corretamente se quiser */}
            <div style={{ marginBottom: '40px' }}>
                <ExpensePieChart transactions={transactions} categories={categories} />
            </div>

            {/* Formulário de Nova Transação */}
            <TransactionForm 
                categories={categories} 
                onTransactionCreated={handleUpdate} 
            />

            {/* 2. FORMULÁRIO DE CATEGORIA ADICIONADO */}
            <CategoryForm 
                onCategoryCreated={handleUpdate} // Reutiliza a função de recarregar
            />

            <hr style={{ marginTop: '30px' }}/>

            {/* Lista de Transações */}
            <h3>Histórico de Transações</h3>
            <ul style={{ listStyle: 'none', padding: 0 }}>
                {transactions.map((t) => (
                    <li key={t.id} style={{ borderBottom: '1px solid #eee', padding: '10px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                        <div>
                            <strong>{t.description}</strong>: R$ {t.amount.toFixed(2)}
                            <br />
                            <small>Categoria: {t.category.name}</small>
                        </div>
                        <div>
                            {/* --- BOTÃO DE EDITAR --- */}
                            <button 
                                onClick={() => setEditingTransaction(t)} 
                                style={{ backgroundColor: '#007bff', color: 'white', border: 'none', padding: '5px 10px', borderRadius: '4px', cursor: 'pointer', marginRight: '5px' }}
                            >
                                Editar
                            </button>
                            {/* --- BOTÃO DE EXCLUIR --- */}
                            <button 
                                onClick={() => handleDelete(t.id)}
                                style={{ backgroundColor: '#ff4d4d', color: 'white', border: 'none', padding: '5px 10px', borderRadius: '4px', cursor: 'pointer' }}
                            >
                                Excluir
                            </button>
                        </div>
                    </li>
                ))}
            </ul>

            {/* --- RENDERIZAÇÃO CONDICIONAL DO MODAL --- */}
            {editingTransaction && (
                <EditTransactionModal 
                    transaction={editingTransaction}
                    categories={categories}
                    onClose={() => setEditingTransaction(null)} 
                    onUpdateSuccess={handleUpdate} 
                />
            )}
        </div>
    );
};

export default Home;