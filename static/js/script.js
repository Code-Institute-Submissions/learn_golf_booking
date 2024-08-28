let calendar;

document.addEventListener('DOMContentLoaded', function () {
    const calendarEl = document.getElementById('calendar');
    const nameInput = document.querySelector('input[name="name"]');
    const emailInput = document.querySelector('input[name="email"]');
    const phoneInput = document.querySelector('input[name="phone"]');
    const calendarContainer = document.getElementById('calendar');

    function initializeCalendar() {
        if (calendarEl && !calendar) { // Initialize calendar if it hasn't been already
            calendar = new FullCalendar.Calendar(calendarEl, {
                initialView: 'dayGridMonth',
                dateClick: function (info) {
                    document.getElementById('selected_date').value = info.dateStr;
                    fetchAvailableSlots(info.dateStr);
                    highlightSelectedDate(info.dateStr);
                }
            });
            calendar.render();
        }
    }

    function fetchAvailableSlots(date) {
        console.log('Fetching available slots for date:', date); // Debugging log
        fetch(`/lessons/available-slots/?date=${encodeURIComponent(date)}`)
            .then(response => response.json())
            .then(data => {
                console.log('Received data:', data); // Log the received data
                const timeSlotList = document.getElementById('time-slot-list');
                timeSlotList.innerHTML = ''; // Clear previous slots
                if (data.length > 0) {
                    data.forEach(slot => {
                        const li = document.createElement('li');
                        li.textContent = slot;
                        li.onclick = function () { selectTimeSlot(slot, date); };
                        timeSlotList.appendChild(li);
                    });
                } else {
                    timeSlotList.innerHTML = '<li>No available slots for this date.</li>';
                }
            })
            .catch(error => console.error('Error fetching time slots:', error));
    }

    function highlightSelectedDate(dateStr) {
        const selectedDateElement = document.querySelector('.fc-daygrid-day[data-date="' + dateStr + '"]');
        if (selectedDateElement) {
            document.querySelectorAll('.fc-day-selected').forEach(el => el.classList.remove('fc-day-selected'));
            selectedDateElement.classList.add('fc-day-selected');
        }
    }

    function checkInputs() {
        const allFilled = nameInput && nameInput.value.trim() && emailInput && emailInput.value.trim() && phoneInput && phoneInput.value.trim();
        if (allFilled) {
            calendarContainer.style.display = 'block'; 
            initializeCalendar(); 
        } else {
            calendarContainer.style.display = 'none'; 
        }
    }

    const isEditing = window.location.href.includes('edit');

    if (isEditing) {
        calendarContainer.style.display = 'block';
        initializeCalendar();
    } else {
        if (nameInput && emailInput && phoneInput) {
            nameInput.addEventListener('input', checkInputs);
            emailInput.addEventListener('input', checkInputs);
            phoneInput.addEventListener('input', checkInputs);
        } else {
            console.error("One or more input fields are missing from the page.");
        }
        calendarContainer.style.display = 'none';
    }
});

function selectTimeSlot(time, date) {
    document.getElementById('selected_time').value = time;
    document.getElementById('selected_date').value = date;
    document.getElementById('bookingForm').submit();
}

function openModal(bookingId) {
    // Construct the correct delete URL with the booking ID
    const deleteForm = document.getElementById('deleteForm');
    deleteForm.action = `/lessons/booking/${bookingId}/delete/`; // Adjust if needed based on your URL patterns
    document.getElementById('deleteModal').style.display = 'block';
}

function closeModal() {
    document.getElementById('deleteModal').style.display = 'none';
}

window.onclick = function (event) {
    const modal = document.getElementById('deleteModal');
    if (event.target === modal) {
        closeModal();
    }
}