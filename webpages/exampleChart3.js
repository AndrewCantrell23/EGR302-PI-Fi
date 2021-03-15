var ctx = document.getElementById('exampleChart3');

var dataFigures = [152, 93.426, 134.624, 12.45, 130.331, 38.07];
var graphLabels = ['2:45:10', '10:30:58', '14:32:44', '18:30:50', '20:59:13', '23:20:05'];

var exampleChart1 = new Chart(ctx, {
        type: 'line',
        data: {
            labels: graphLabels,
            datasets: [{
                label: 'Point Speed in Mbps',
                data: dataFigures,
                fill: false,
                backgroundColor: [
                    'rgba(54, 162, 235, 0.2)',
                ],
                borderColor: [
                    'rgba(54, 162, 235, 1)',
                ],
                borderWidth: 1
            }]
        },
        options: {
            maintainAspectRatio: false,
            responsive: false,
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    }
);