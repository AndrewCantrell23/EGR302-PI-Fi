var ctx = document.getElementById('exampleChart1');
var frameworks = ['React', 'Angular', 'Vue', 'Hyperapp', 'Omi'];

var exampleChart1 = new Chart(ctx, {
        type: 'bar',
        data: {
            label: frameworks,
            datasets: [{
                label: 'Test1',
                data: [135850, 52122, 148825, 16939, 9763],
                backgroundColor: [
                    "rgba(255, 99, 132, 0.2)",
                    "rgba(54, 162, 235, 0.2)",
                    "rgba(255, 206, 86, 0.2)",
                    "rgba(75, 192, 192, 0.2)",
                    "rgba(153, 102, 255, 0.2)"
                ],
                borderColor: [
                    "rgba(255, 99, 132, 1)",
                    "rgba(54, 162, 235, 1)",
                    "rgba(255, 206, 86, 1)",
                    "rgba(75, 192, 192, 1)",
                    "rgba(153, 102, 255, 1)",
                ],
                borderWidth: 1
            }]
        },
        options: {
            maintainAspectRatio: false,
            responsive: false,
        }
    }
);