// ===== BUDGET BUDDY — ASSETS PAGE JS =====

// Flash auto-dismiss
setTimeout(() => {
    document.querySelectorAll('.flash-msg').forEach(el => {
        el.style.opacity = '0';
        el.style.transition = 'opacity 0.5s';
        setTimeout(() => el.remove(), 500);
    });
}, 4000);

// Sidebar toggle
function toggleSidebar() {
    document.getElementById('sidebar').classList.toggle('open');
}

// Close sidebar when clicking outside on mobile
document.addEventListener('click', function (e) {
    const sidebar = document.getElementById('sidebar');
    const toggle = document.querySelector('.sidebar-toggle');
    if (sidebar.classList.contains('open') &&
        !sidebar.contains(e.target) &&
        e.target !== toggle) {
        sidebar.classList.remove('open');
    }
});

// Show/hide custom label input
function toggleCustomLabel(selectEl, wrapperId) {
    const wrap = document.getElementById(wrapperId);
    const input = wrap.querySelector('input');
    if (selectEl.value === 'Other') {
        wrap.classList.add('show');
        input.required = true;
    } else {
        wrap.classList.remove('show');
        input.required = false;
        input.value = '';
    }
}

// Close modal on overlay click
document.querySelectorAll('.modal-overlay').forEach(overlay => {
    overlay.addEventListener('click', e => {
        if (e.target === overlay) overlay.classList.remove('open');
    });
});

// Close modal on Escape key
document.addEventListener('keydown', e => {
    if (e.key === 'Escape') {
        document.querySelectorAll('.modal-overlay.open').forEach(m => m.classList.remove('open'));
    }
});

function closeModal(id) {
    document.getElementById(id).classList.remove('open');
}

// Open Edit Asset Modal
function openEditAsset(id, category, amount, date) {
    document.getElementById('editAssetCategory').value = category;
    document.getElementById('editAssetAmount').value = amount;
    document.getElementById('editAssetDate').value = date;
    document.getElementById('editAssetForm').action = `/edit_asset/${id}`;
    document.getElementById('editAssetModal').classList.add('open');
}

// Open Edit Expense Modal
function openEditExpense(id, category, amount, date) {
    document.getElementById('editExpenseCategory').value = category;
    document.getElementById('editExpenseAmount').value = amount;
    document.getElementById('editExpenseDate').value = date;
    document.getElementById('editExpenseForm').action = `/edit_expense/${id}`;
    document.getElementById('editExpenseModal').classList.add('open');
}

// Open Edit Loan Modal
function openEditLoan(id, person, amount, due_date, description) {
    document.getElementById('editLoanPerson').value = person;
    document.getElementById('editLoanAmount').value = amount;
    document.getElementById('editLoanDueDate').value = due_date;
    document.getElementById('editLoanDescription').value = description;
    document.getElementById('editLoanForm').action = `/edit_loan/${id}`;
    document.getElementById('editLoanModal').classList.add('open');
}

// Chart builder
function makeChart(id, labels, data, colors) {
    const canvas = document.getElementById(id);
    if (!canvas) return;
    new Chart(canvas.getContext('2d'), {
        type: 'doughnut',
        data: {
            labels,
            datasets: [{
                data,
                backgroundColor: colors,
                borderColor: '#161616',
                borderWidth: 3,
                hoverBorderWidth: 4,
                hoverOffset: 8
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: '65%',
            plugins: {
                legend: {
                    position: 'right',
                    labels: {
                        color: '#f0ece4',
                        font: { family: 'DM Sans', size: 12 },
                        padding: 16,
                        boxWidth: 12,
                        borderRadius: 4
                    }
                },
                tooltip: {
                    callbacks: {
                        label: (ctx) => ` ₨ ${ctx.parsed.toLocaleString()}`
                    },
                    backgroundColor: '#1e1e1e',
                    borderColor: '#2a2a2a',
                    borderWidth: 1,
                    titleColor: '#f0ece4',
                    bodyColor: '#c8a96e',
                    padding: 12,
                    cornerRadius: 8
                }
            },
            animation: {
                animateRotate: true,
                animateScale: true,
                duration: 800,
                easing: 'easeOutQuart'
            }
        }
    });
}