var ctx = document.getElementById('exampleChart1');

var dataFigures = [152, 93.426, 134.624, 130.331, 12.45, 38.07];
var graphLabels = ['Point', 'Lancer Arms', 'Engineering', 'Point-B-Testing', 'Smith', 'Village'];

var exampleChart1 = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: graphLabels,
            datasets: [{
                label: 'Speed in Mbps',
                data: dataFigures,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
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
        },
        style: {
            display: "block"

        }
    }

);


