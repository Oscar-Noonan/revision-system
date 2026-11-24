const list = document.getElementById("user-list");

async function loadusers() {
    try {
        const response = await fetch("/api/users");

        if (!response.ok) {
            throw new Error("Failed to fetch users");
        }

        const users = await response.json();

        list.innerHTML = "";

        users.forEach(user => {
            const li = document.createElement("li");
            li.className = "user";

            const span = document.createElement("span");
            span.textContent = user.email;

            li.appendChild(span);
            list.appendChild(li);
        });

    } catch (error) {
        console.error("Error loading users:", error);
    }
}

loadusers();