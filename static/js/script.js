let calendar;

document.addEventListener('DOMContentLoaded', function () {
    const calendarEl = document.getElementById('calendar');
    const nameInput = document.querySelector('input[name="name"]');
    const emailInput = document.querySelector('input[name="email"]');
    const phoneInput = document.querySelector('input[name="phone"]');
    const calendarContainer = document.getElementById('calendar');
    const timeSlotList = document.getElementById('time-slot-list'); 
    const timeSlotsSection = document.getElementById('time-slots'); 

    timeSlotsSection.style.display = 'none';

    function initializeCalendar() {
        if (calendarEl && !calendar) {
            console.log('Initializing calendar...');
            calendar = new FullCalendar.Calendar(calendarEl, {
                initialView: 'dayGridMonth',
                validRange: {
                    start: new Date().toISOString().split('T')[0]
                },
                dateClick: function (info) {
                    console.log('Date clicked:', info.dateStr);
                    document.getElementById('selected_date').value = info.dateStr;
                    fetchAvailableSlots(info.dateStr);
                    highlightSelectedDate(info.dateStr);
                    timeSlotsSection.style.display = 'block';
                }
            });
            calendar.render();
        }
    }

    function fetchAvailableSlots(date) {
        console.log(`Fetching available slots for date: ${date}`);
        fetch(`/lessons/available-slots/?date=${encodeURIComponent(date)}`)
            .then(response => response.json())
            .then(data => {
                console.log(`Available slots received: `, data);
                timeSlotList.innerHTML = '';
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
            .catch(error => {
                console.error('Error fetching time slots:', error);
                timeSlotList.innerHTML = '<li>Error loading available slots. Please try again later.</li>';
            });
    }

    function selectTimeSlot(time, date) {
        console.log(`Selected time slot: ${time} on date: ${date}`);
        document.getElementById('selected_time').value = time;
        document.getElementById('selected_date').value = date;
        document.getElementById('bookingForm').submit();
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

function openModal(bookingId) {
    document.getElementById('delete_booking_id').value = bookingId;
    document.getElementById('deleteForm').action = `/bookings/delete/${bookingId}/`;
    document.getElementById('deleteModal').style.display = 'block'; 
}

function closeModal() {
    document.getElementById('deleteModal').style.display = 'none'; 
}

function submitDeleteForm() {
    document.getElementById('deleteForm').submit(); 
}

window.onclick = function (event) {
    const modal = document.getElementById('deleteModal');
    if (event.target == modal) {
        closeModal();
    }
}