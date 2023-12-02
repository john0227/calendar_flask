function zeroPad2(num) {
    return ('00' + num).slice(-2);
}

document.addEventListener("DOMContentLoaded", function() {
    var cells = document.querySelectorAll(".calendar-cell");
    var scheduleForm = document.getElementById("schedule-form");
    var dateInput = scheduleForm.querySelector("#date-input");
    var schStartTime = scheduleForm.querySelector("#sch-start");
    var schEndTime = scheduleForm.querySelector("#sch-end");

    cells.forEach(function(cell) {
        cell.addEventListener("click", function() {
            var date = this.getAttribute("data-date");
            dateInput.value = date;
            schStartTime.value = "08:00";
            schEndTime.value = "09:00";
            scheduleForm.style.display = "block";
        });
    });

    scheduleForm.addEventListener("submit", function(event) {
        const buttonName = event.submitter.name;
        if (buttonName == "cancel") {
            // Prevent the default form submission
            event.preventDefault();
            scheduleForm.reset();
        }
        // Perform any additional actions you need on form submission
        // For now, just hide the form
        scheduleForm.style.display = "none";
    });

    // Add listeners for start and end time
    schStartTime.addEventListener("input", handleTimeInput);
    schEndTime.addEventListener("input", handleTimeInput);

    function handleTimeInput(event) {
        var startTime = schStartTime.value.split(":");
        var startHour = parseInt(startTime[0]);
        var startMin = parseInt(startTime[1]);

        var endTime = schEndTime.value.split(":");
        var endHour = parseInt(endTime[0]);
        var endMin = parseInt(endTime[1]);

        if (startHour < endHour || (startHour == endHour && startMin <= endMin)) return;

        if (event.target == schStartTime) {
            // Adjust endTime to startTime + 1 hour
            endHour = startHour + 1;
            if (endHour > 23) {
                endHour = 23;
                endMin = 59;
            }
            schEndTime.value = zeroPad2(endHour) + ":" + zeroPad2(endMin);
        } else {
            // Adjust startTime to endTime - 1 hour
            startHour = endHour - 1;
            if (startHour < 0) {
                startHour = 0;
                startMin = 0;
            }
            schStartTime.value = zeroPad2(startHour) + ":" + zeroPad2(startMin);
        }
    }
});
  