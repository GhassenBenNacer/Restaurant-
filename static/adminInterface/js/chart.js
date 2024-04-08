$(function() {
  /* ChartJS
   * -------
   * Data and config for chartjs
   */
  'use strict';

  // Modify the data and labels for daily and hourly histograms
  var dailyHistogramData = JSON.parse('{{ daily_histogram|escapejs }}');
  var hourlyHistogramData = JSON.parse('{{ hourly_histogram|escapejs }}');

  // Chart configuration for daily histogram
  var dailyHistogramConfig = {
    type: 'bar',
    data: {
      labels: dailyHistogramData.map(item => item.day_of_week), // Assuming day_of_week is the label for daily histogram
      datasets: [{
        label: 'Reservations per Day',
        data: dailyHistogramData.map(item => item.reservation_count),
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        borderColor: 'rgba(255,99,132,1)',
        borderWidth: 1,
        fill: false
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: true
          }
        }]
      },
      legend: {
        display: false
      },
      elements: {
        point: {
          radius: 0
        }
      }
    }
  };

  // Chart configuration for hourly histogram
  var hourlyHistogramConfig = {
    type: 'bar',
    data: {
      labels: hourlyHistogramData.map(item => item.hour), // Assuming hour is the label for hourly histogram
      datasets: [{
        label: 'Reservations per Hour',
        data: hourlyHistogramData.map(item => item.reservation_count),
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1,
        fill: false
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: true
          }
        }]
      },
      legend: {
        display: false
      },
      elements: {
        point: {
          radius: 0
        }
      }
    }
  };

  // Render daily histogram
  var dailyHistogramCanvas = $("#dailyHistogramChart").get(0).getContext("2d");
  var dailyHistogramChart = new Chart(dailyHistogramCanvas, dailyHistogramConfig);

  // Render hourly histogram
  var hourlyHistogramCanvas = $("#hourlyHistogramChart").get(0).getContext("2d");
  var hourlyHistogramChart = new Chart(hourlyHistogramCanvas, hourlyHistogramConfig);

  // Other chart configurations...
});
