// frontend/src/components/FinancialSummary.jsx

import React from 'react';

const FinancialSummary = ({ transactions }) => {

    // 1. PROTEÇÃO: Se não houver transações, não renderiza nada ou mostra zeros
    if (!transactions) {
        return null;
    }

    // 2. Cálculos de Totais (Com proteção extra para transações sem categoria)
    const totalIncome = transactions
        .filter(t => t.category && t.category.type === 'INCOME') // Verifica se t.category existe
        .reduce((acc, t) => acc + t.amount, 0);

    const totalOutcome = transactions
        .filter(t => t.category && t.category.type === 'OUTCOME')
        .reduce((acc, t) => acc + t.amount, 0);

    const balance = totalIncome - totalOutcome;

    // Função auxiliar para formatar dinheiro (R$)
    const formatCurrency = (value) => {
        return value.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
    };

    // Estilos (mantidos iguais)
    const tableStyle = {
        width: '100%',
        borderCollapse: 'collapse',
        marginBottom: '20px',
        backgroundColor: '#fff',
        borderRadius: '8px',
        overflow: 'hidden',
        boxShadow: '0 2px 4px rgba(0,0,0,0.1)'
    };

    const thStyle = {
        backgroundColor: '#f8f9fa',
        padding: '15px',
        textAlign: 'center',
        borderBottom: '1px solid #ddd',
        color: '#666'
    };

    const tdStyle = {
        padding: '15px',
        textAlign: 'center',
        fontSize: '1.2em',
        fontWeight: 'bold'
    };

    return (
        <div style={{ marginBottom: '30px' }}>
            <h3 style={{ textAlign: 'center' }}>Resumo Financeiro</h3>
            <table style={tableStyle}>
                <thead>
                    <tr>
                        <th style={thStyle}>Receitas (Entradas)</th>
                        <th style={thStyle}>Despesas (Saídas)</th>
                        <th style={thStyle}>Saldo Final</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td style={{ ...tdStyle, color: '#2ecc71' }}>
                            {formatCurrency(totalIncome)}
                        </td>
                        <td style={{ ...tdStyle, color: '#e74c3c' }}>
                            {formatCurrency(totalOutcome)}
                        </td>
                        <td style={{ ...tdStyle, color: balance >= 0 ? '#2980b9' : '#e74c3c' }}>
                            {formatCurrency(balance)}
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    );
};

export default FinancialSummary;