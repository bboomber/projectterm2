function showGraph(months, insure_list) {
    var ctx = document.getElementById('predictChart').getContext('2d');
        var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'line',

        // The data for our dataset
        data: {
            labels: months,
            datasets: [{
                label: 'ยอดขายปี 2015',
                borderColor: 'rgb(255, 99, 132)',
                data: insure_list
            }]
        },

        // Configuration options go here
        options: {}
    });
}