$(document).ready(function () {
    // Handle the rent button click event
    $('.rent-btn').click(function () {
        var carPk = $(this).data('car-pk');
        var rentUrl = $('#rentModal').data('rent-url');
        $('#rentForm').attr('action', rentUrl.replace('0', carPk));

        // Clear previous input values and errors
        $('#rentForm').find('input[type="date"]').val('').removeClass('is-invalid');
        $('#dateFromValidationMessage').text(''); // Clear date from error message
        $('#dateToValidationMessage').text('');   // Clear date to error message

        // Set the car_id value in the form
        $('#rentForm').find('input[name="car_id"]').val(carPk);

        // Show the modal
        $('#rentModal').modal('show');
    });

    // Attach the submit event listener to the form after the modal is shown
    $('#rentModal').on('shown.bs.modal', function () {
        var form = $('#rentForm');
        var dateFromInput = $('input[name="date_from"]');
        var dateToInput = $('input[name="date_to"]');
        var errorMessageDiv = $('#error-message');

        form.on('submit', function (event) {
            // Parse the date inputs to Date objects
            var dateFrom = new Date(dateFromInput.val());
            var dateTo = new Date(dateToInput.val());

            // Get the current date
            var currentDate = new Date();

            // Check if the dates have already passed
            if (dateFrom < currentDate || dateTo < currentDate) {
                // Prevent the form from submitting
                event.preventDefault();

                // Display the validation message
                var validationMessage = "The selected dates have already passed.";
                dateFromInput.addClass('is-invalid');
                dateToInput.addClass('is-invalid');

                // Update error messages
                if (dateFrom < currentDate) {
                    $('#dateFromValidationMessage').text(validationMessage);
                }
                if (dateTo < currentDate) {
                    $('#dateToValidationMessage').text(validationMessage);
                }
            } else {
                // If the dates are valid, check if the car is available for rental
                let checkCarUrl = $('#rentModal').data('check-car-url');
                $.ajax({
                    type: 'POST',
                    url: checkCarUrl, // Replace with the URL of the view to check car availability
                    data: form.serialize(), // Serialize the form data to include the car_id
                    success: function (response) {
                        if (response.available) {
                            // Car is available, allow the form to be submitted
                            form.off('submit').submit();
                        } else {
                            // Car is already rented, display an error message
                            errorMessageDiv.text('This car is already rented for the selected dates.');
                        }
                    },
                    error: function () {
                        // Error handling in case the AJAX request fails
                        console.error('Error checking car availability.');
                    },
                });
                event.preventDefault();
            }
        });
    });
});