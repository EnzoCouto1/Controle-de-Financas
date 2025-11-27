// frontend/src/components/ExpensePieChart.jsx

import React from 'react';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import { Pie } from 'react-chartjs-2';

// Registra os componentes necessários do Chart.js
ChartJS.register(ArcElement, Tooltip, Legend);

const ExpensePieChart = ({ transactions, categories }) => {
    
    // 1. Processar os dados: Somar despesas por categoria
    const processData = () => {
        // Filtra apenas saídas (Despesas)
        const expenses = transactions.filter(t => t.category && t.category.type === 'OUTCOME');
        
        // Mapa para somar valores: { "Alimentação": 150.00, "Lazer": 50.00 }
        const categoryTotals = {};

        expenses.forEach(t => {
            const catName = t.category.name;
            if (categoryTotals[catName]) {
                categoryTotals[catName] += t.amount;
            } else {
                categoryTotals[catName] = t.amount;
            }
        });

        const labels = Object.keys(categoryTotals);
        const dataValues = Object.values(categoryTotals);

        // Cores para o gráfico
        const backgroundColors = [
            'rgba(255, 99, 132, 0.6)', 
            'rgba(54, 162, 235, 0.6)', 
            'rgba(255, 206, 86, 0.6)', 
            'rgba(75, 192, 192, 0.6)', 
            'rgba(153, 102, 255, 0.6)', 
            'rgba(255, 159, 64, 0.6)', 
        ];

        return {
            labels: labels,
            datasets: [
                {
                    label: 'Total (R$)',
                    data: dataValues,
                    backgroundColor: backgroundColors,
                    borderColor: backgroundColors.map(c => c.replace('0.6', '1')),
                    borderWidth: 1,
                },
            ],
        };
    };

    const data = processData();

    // Se não houver despesas, mostra mensagem
    if (!data.labels || data.labels.length === 0) {
        return (
            <div style={{ textAlign: 'center', padding: '20px', color: '#666' }}>
                <p>Cadastre despesas para ver o gráfico.</p>
            </div>
        );
    }

    return (
        <div style={{ width: '100%', maxWidth: '350px', margin: '0 auto 30px auto' }}>
            <h3 style={{ textAlign: 'center', marginBottom: '15px' }}>Despesas por Categoria</h3>
            <Pie data={data} />
        </div>
    );
};

export default ExpensePieChart;