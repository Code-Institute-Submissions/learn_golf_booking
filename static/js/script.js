document.addEventListener('DOMContentLoaded', function () {
    let calendar;

    const calendarEl = document.getElementById('calendar');
    const timeSlotList = document.getElementById('time-slot-list');
    const timeSlotsSection = document.getElementById('time-slots');
    const selectedDateInput = document.getElementById('date');
    const selectedTimeInput = document.getElementById('time');
    const nameInput = document.querySelector('input[name="name"]');
    const emailInput = document.querySelector('input[name="email"]');
    const phoneInput = document.querySelector('input[name="phone"]');
    const bookingForm = document.getElementById('bookingForm');
    const isEditing = window.location.href.includes('edit');

    function initializeCalendar() {
        if (!calendarEl || calendar) return;
        calendar = new FullCalendar.Calendar(calendarEl, {
            initialView: 'dayGridMonth',
            validRange: {
                start: new Date().toISOString().split('T')[0]
            },
            dateClick: function (info) {
                selectedDateInput.value = info.dateStr;
                fetchAvailableSlots(info.dateStr);
                highlightSelectedDate(info.dateStr);
                timeSlotsSection.style.display = 'block';
            }
        });
        calendar.render();
    }

    function checkInputs() {
        const allFilled = nameInput.value.trim() && emailInput.value.trim() && phoneInput.value.trim();
        if (allFilled) {
            calendarContainer.style.display = 'block';
            initializeCalendar();
        } else {
            hideCalendarAndSlots();
        }
    }

    function hideCalendarAndSlots() {
        calendarContainer.style.display = 'none';
        timeSlotsSection.style.display = 'none';
    }

    nameInput.addEventListener('input', checkInputs);
    emailInput.addEventListener('input', checkInputs);
    phoneInput.addEventListener('input', checkInputs);

    // editing mode
    if (isEditing) {
        initializeCalendar();
        if (selectedDateInput.value) {
            highlightSelectedDate(selectedDateInput.value);
            fetchAvailableSlots(selectedDateInput.value);
        }
    } else {
        hideCalendarAndSlots();
    }

    function fetchAvailableSlots(date) {
        fetch(`/lessons/available-slots/?date=${encodeURIComponent(date)}`)
            .then(response => response.json())
            .then(data => {
                timeSlotList.innerHTML = '';
                if (data.length > 0) {
                    data.forEach(slot => {
                        const li = document.createElement('li');
                        li.textContent = slot;
                        li.onclick = function () {
                            selectTimeSlot(slot, date);
                        };
                        timeSlotList.appendChild(li);
                    });
                } else {
                    timeSlotList.innerHTML = '<li>No available slots for this date.</li>';
                }
            })
            .catch(() => {
                timeSlotList.innerHTML = '<li>Error loading available slots. Please try again later.</li>';
            });
    }

    function selectTimeSlot(time, date) {
        selectedTimeInput.value = time;
        selectedDateInput.value = date;
        setTimeout(() => {
            bookingForm.submit();
        }, 100);
    }

    function highlightSelectedDate(dateStr) {
        const selectedDateElement = document.querySelector(`.fc-daygrid-day[data-date="${dateStr}"]`);
        if (selectedDateElement) {
            document.querySelectorAll('.fc-day-selected').forEach(el => el.classList.remove('fc-day-selected'));
            selectedDateElement.classList.add('fc-day-selected');
        }
    }
});

// Delete Booking Modal
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
    if (event.target == document.getElementById('deleteModal')) {
        closeModal();
    }
};
