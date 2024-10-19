document.addEventListener('DOMContentLoaded', function () {
    // Verifica se o elemento existe
    const estadoDataElement = document.getElementById('estado-data');
    if (!estadoDataElement) {
        console.error('Elemento estado-data não encontrado!');
        return;
    }
    
    // Recupera os dados do script JSON
    const estadoCountData = JSON.parse(estadoDataElement.textContent);

    // Cria arrays para os rótulos e dados
    const labels = estadoCountData.map(item => item.estado);
    const dataCounts = estadoCountData.map(item => item.count);

    // Cria o gráfico
    const ctx = document.getElementById('graficoUsoSolo').getContext('2d');
    const graficoUsoSolo = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: labels,
            datasets: [{
                data: dataCounts,
                backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40'],
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: 'Distribuição dos Estados'
                }
            }
        }
    });
});