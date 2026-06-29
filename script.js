// Load All Records
async function loadRecords() {

    const response = await fetch("http://127.0.0.1:8000/records");
    let records = await response.json();

    const search = document.getElementById("search").value.toLowerCase();

    records = records.filter(record =>
        record.name.toLowerCase().includes(search) ||
        record.email.toLowerCase().includes(search)
    );

    document.getElementById("totalRecords").innerText = records.length;

    const tbody = document.querySelector("#recordTable tbody");
    tbody.innerHTML = "";

    records.forEach(record => {

        tbody.innerHTML += `
            <tr>
                <td>${record.name}</td>
                <td>${record.email}</td>
                <td>
                    <button onclick="deleteRecord('${record.email}')">
                        🗑 Delete
                    </button>
                </td>
            </tr>
        `;

    });

}

// Add Record
async function addRecord() {

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();

    if (name === "" || email === "") {

        document.getElementById("message").innerHTML =
            "❌ Name and Email are required.";

        return;
    }

    const response = await fetch("http://127.0.0.1:8000/add-record", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            name,
            email
        })

    });

    const data = await response.json();

    document.getElementById("message").innerHTML = data.message;

    document.getElementById("name").value = "";
    document.getElementById("email").value = "";

    loadRecords();

}

// Delete Record
async function deleteRecord(email) {

    const confirmDelete = confirm(
        "Are you sure you want to delete this record?"
    );

    if (!confirmDelete) return;

    await fetch(`http://127.0.0.1:8000/delete-record/${email}`, {

        method: "DELETE"

    });

    document.getElementById("message").innerHTML =
        "✅ Record Deleted Successfully!";

    loadRecords();

}

// Export CSV
document.getElementById("exportBtn").addEventListener("click", async () => {

    const response = await fetch("http://127.0.0.1:8000/records");
    const records = await response.json();

    let csv = "Name,Email\n";

    records.forEach(record => {

        csv += `${record.name},${record.email}\n`;

    });

    const blob = new Blob([csv], {

        type: "text/csv"

    });

    const url = window.URL.createObjectURL(blob);

    const a = document.createElement("a");

    a.href = url;
    a.download = "records.csv";

    a.click();

    window.URL.revokeObjectURL(url);

});

// Initial Load
loadRecords();