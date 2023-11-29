document.addEventListener("DOMContentLoaded", function() {
    var cells = document.querySelectorAll(".calendar-cell");
    var scheduleForm = document.getElementById("schedule-form");
    var dateInput = scheduleForm.querySelector("#date-input");

    cells.forEach(function(cell) {
        cell.addEventListener("click", function() {
            var date = this.getAttribute("data-date");
            dateInput.value = date;
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
});
  