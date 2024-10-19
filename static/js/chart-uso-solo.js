document.addEventListener('DOMContentLoaded', function () {
    const ctx = document.getElementById('graficoUsoSolo').getContext('2d');
    const graficoUsoSolo = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['Agricultável', 'Vegetação'],
            datasets: [{
                data: [area_agricultavel, area_vegetacao],
                backgroundColor: ['#FF6384', '#36A2EB'],
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
                    text: 'Uso de Solo'
                }
            }
        }
    });
});
