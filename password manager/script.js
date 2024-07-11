document.getElementById('passwordForm').addEventListener('submit', function (e) {
    e.preventDefault();

    let username = document.getElementById('username').value;
    let email = document.getElementById('email').value;
    let password = document.getElementById('password').value;

    let passwords = JSON.parse(localStorage.getItem('passwords')) || [];
    let id = passwords.length ? Math.max(...passwords.map(p => p.id || 0)) + 1 : 1; // Generate a new ID
    passwords.push({ id, username, email, password });
    localStorage.setItem('passwords', JSON.stringify(passwords));

    document.getElementById('passwordForm').reset();
    displayPasswords();
});

function displayPasswords() {
    let passwords = JSON.parse(localStorage.getItem('passwords')) || [];
    let tableBody = document.querySelector('#passwordTable tbody');
    tableBody.innerHTML = '';

    passwords.forEach(function (item) {
        let row = tableBody.insertRow();
        row.insertCell(0).textContent = item.id;
        row.insertCell(1).textContent = item.username;
        row.insertCell(2).textContent = item.email;
        
        let passwordCell = row.insertCell(3);
        passwordCell.textContent = '*****';
        passwordCell.dataset.password = item.password;

        let eyeCell = row.insertCell(4);
        let eyeIcon = document.createElement('i');
        eyeIcon.className = 'fas fa-eye';
        eyeIcon.style.cursor = 'pointer';
        eyeIcon.onclick = function () {
            if (passwordCell.textContent === '*****') {
                passwordCell.textContent = passwordCell.dataset.password;
                eyeIcon.className = 'fas fa-eye-slash';
            } else {
                passwordCell.textContent = '*****';
                eyeIcon.className = 'fas fa-eye';
            }
        };
        eyeCell.appendChild(eyeIcon);
    });
}

function deletePassword() {
    let deleteId = parseInt(document.getElementById('deleteId').value);
    let passwords = JSON.parse(localStorage.getItem('passwords')) || [];
    passwords = passwords.filter(item => item.id !== deleteId);
    localStorage.setItem('passwords', JSON.stringify(passwords));

    document.getElementById('deleteForm').reset();
    displayPasswords();
}

function showPage(pageId) {
    document.querySelectorAll('.page').forEach(page => {
        page.classList.remove('active');
    });
    document.getElementById(pageId).classList.add('active');
}

function assignIds() {
    let passwords = JSON.parse(localStorage.getItem('passwords')) || [];
    let maxId = passwords.length ? Math.max(...passwords.map(p => p.id || 0)) : 0;
    let nextId = maxId + 1;

    passwords = passwords.map((item, index) => {
        if (!item.id) {
            item.id = nextId++;
        }
        return item;
    });

    localStorage.setItem('passwords', JSON.stringify(passwords));
    displayPasswords();
}

// Display passwords on page load
displayPasswords();
