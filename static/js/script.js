const charts = document.querySelectorAll(".chart");

charts.forEach(function (chart) {
  var ctx = chart.getContext("2d");
  var myChart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
      datasets: [
        {
          label: "# of Votes",
          data: [12, 19, 3, 5, 2, 3],
          backgroundColor: [
            "rgba(255, 99, 132, 0.2)",
            "rgba(54, 162, 235, 0.2)",
            "rgba(255, 206, 86, 0.2)",
            "rgba(75, 192, 192, 0.2)",
            "rgba(153, 102, 255, 0.2)",
            "rgba(255, 159, 64, 0.2)",
          ],
          borderColor: [
            "rgba(255, 99, 132, 1)",
            "rgba(54, 162, 235, 1)",
            "rgba(255, 206, 86, 1)",
            "rgba(75, 192, 192, 1)",
            "rgba(153, 102, 255, 1)",
            "rgba(255, 159, 64, 1)",
          ],
          borderWidth: 1,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
});

$(document).ready(function () {
  $(".data-table").each(function (_, table) {
    $(table).DataTable();
  });
});


// STEPPER 
document.getElementById('track-btn').addEventListener('click', function() {
  const trackingId = document.getElementById('tracking-id-input').value;

  if (trackingId) {
      fetch(`/track-shipment/?tracking_no=${trackingId}`)
      .then(response => response.json())
      .then(data => {
          const status = data.status;
          updateStepper(status);
      })
      .catch(error => {
          console.error('Error:', error);
      });
  } else {
      alert("Please enter a tracking ID.");
  }
});

function updateStepper(status) {
  const stepperContainer = document.getElementById('stepper-container');
  let stepperHTML = `
      <div class="stepper">
          <div class="step ${status === 'Picked Up' || status === 'Processing' || status === 'In Transit' || status === 'On Hold' || status === 'Delivered' ? 'completed' : ''}">
              <div class="circle"><i class="fa fa-cube"></i></div>
              <p>Picked Up</p>
          </div>
          <div class="step ${status === 'Processing' || status === 'In Transit' || status === 'On Hold' || status === 'Delivered' ? 'completed' : ''}">
              <div class="circle"><i class="fa fa-cogs"></i></div>
              <p>Processing</p>
          </div>
          <div class="step ${status === 'In Transit' || status === 'On Hold' || status === 'Delivered' ? 'completed' : ''}">
              <div class="circle"><i class="fa fa-truck"></i></div>
              <p>In Transit</p>
          </div>
          <div class="step ${status === 'On Hold' || status === 'Delivered' ? 'completed' : ''}">
              <div class="circle"><i class="fa fa-pause"></i></div>
              <p>On Hold</p>
          </div>
          <div class="step ${status === 'Delivered' ? 'completed' : ''}">
              <div class="circle"><i class="fa fa-check-circle"></i></div>
              <p>Delivered</p>
          </div>
      </div>
  `;
  stepperContainer.innerHTML = stepperHTML;
}