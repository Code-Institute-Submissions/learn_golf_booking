document.addEventListener('DOMContentLoaded', function () {
    let calendar;

    const calendarEl = document.getElementById('calendar');
    const timeSlotList = document.getElementById('time-slot-list');
    const timeSlotsSection = document.getElementById('time-slots');
    const nameInput = document.querySelector('input[name="name"]');
    const emailInput = document.querySelector('input[name="email"]');
    const phoneInput = document.querySelector('input[name="phone"]');
    const calendarContainer = document.getElementById('calendar');
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
                const selectedDateInput = document.getElementById('date');

                try {
                    if (selectedDateInput) {
                        selectedDateInput.value = info.dateStr;
                        fetchAvailableSlots(info.dateStr);
                        highlightSelectedDate(info.dateStr);
                        timeSlotsSection.style.display = 'block';
                    }
                } catch (error) {
                    console.error('Error setting date input value:', error);
                }
            }
        });
        calendar.render();
    }

    function checkInputs() {
        const allFilled = nameInput?.value.trim() !== '' && emailInput?.value.trim() !== '' && phoneInput?.value.trim() !== '';
        if (allFilled) {
            calendarContainer.style.display = 'block';
            initializeCalendar();
        } else {
            calendarContainer.style.display = 'none'; 
            timeSlotsSection.style.display = 'none'; 
        }
    }

    function hideCalendarAndSlots() {
        calendarContainer.style.display = 'none';
        timeSlotsSection.style.display = 'none';
    }

    if (nameInput) nameInput.addEventListener('input', checkInputs);
    if (emailInput) emailInput.addEventListener('input', checkInputs);
    if (phoneInput) phoneInput.addEventListener('input', checkInputs);

    if (isEditing) {
        initializeCalendar();
        const selectedDateInput = document.getElementById('date');
        if (selectedDateInput?.value) {
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
        const selectedTimeInput = document.getElementById('time');
        const selectedDateInput = document.getElementById('date');

        if (selectedTimeInput && selectedDateInput) {
            selectedTimeInput.value = time;
            selectedDateInput.value = date;
            setTimeout(() => {
                if (bookingForm) bookingForm.submit();
            }, 100);
        } else {
            console.error('Selected time or date input elements not found.');
        }
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
    const deleteBookingId = document.getElementById('delete_booking_id');
    const deleteForm = document.getElementById('deleteForm');
    const deleteModal = document.getElementById('deleteModal');

    if (deleteBookingId && deleteForm && deleteModal) {
        deleteBookingId.value = bookingId;
        deleteForm.action = `/bookings/delete/${bookingId}/`;
        deleteModal.style.display = 'block';
    } else {
        console.error('Delete modal elements not found.');
    }
}

function closeModal() {
    const deleteModal = document.getElementById('deleteModal');
    if (deleteModal) {
        deleteModal.style.display = 'none';
    } else {
        console.error('Delete modal element not found.');
    }
}

function submitDeleteForm() {
    const deleteForm = document.getElementById('deleteForm');
    if (deleteForm) {
        deleteForm.submit();
    } else {
        console.error('Delete form element not found.');
    }
}

window.onclick = function (event) {
    const deleteModal = document.getElementById('deleteModal');
    if (event.target === deleteModal) {
        closeModal();
    }
};
