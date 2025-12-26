// Hlavní JavaScript pro dashboard asistentů

// Inicializace dashboardu po načtení stránky
document.addEventListener('DOMContentLoaded', () => {
    initializeDashboard();
    setupModalHandlers();
});

// Vykreslení všech asistentů na dashboard
function initializeDashboard() {
    const grid = document.getElementById('assistants-grid');

    assistants.forEach(assistant => {
        const card = createAssistantCard(assistant);
        grid.appendChild(card);
    });
}

// Vytvoření karty asistenta
function createAssistantCard(assistant) {
    const card = document.createElement('div');
    card.className = 'assistant-card';
    card.style.setProperty('--card-color-start', assistant.colorStart);
    card.style.setProperty('--card-color-end', assistant.colorEnd);

    card.innerHTML = `
        <span class="assistant-status ${assistant.status}"></span>
        <span class="assistant-icon">${assistant.icon}</span>
        <h3>${assistant.name}</h3>
        <p>${assistant.description}</p>
        <div class="assistant-tags">
            ${assistant.tags.map(tag => `<span class="tag">${tag}</span>`).join('')}
        </div>
    `;

    // Přidání click handleru pro otevření detailu
    card.addEventListener('click', () => openAssistantModal(assistant));

    return card;
}

// Otevření modalu s detailem asistenta
function openAssistantModal(assistant) {
    const modal = document.getElementById('assistant-modal');
    const modalBody = document.getElementById('modal-body');

    // Vytvoření obsahu modalu
    modalBody.innerHTML = `
        <div class="modal-icon">${assistant.icon}</div>
        <h2>${assistant.name}</h2>
        <div class="modal-description">
            <p>${assistant.detailedDescription}</p>
        </div>

        <div class="modal-features">
            <h3>Klíčové schopnosti:</h3>
            <ul>
                ${assistant.features.map(feature => `<li>${feature}</li>`).join('')}
            </ul>
        </div>

        <div class="modal-tags">
            <h3>Technologie:</h3>
            <div class="assistant-tags">
                ${assistant.tags.map(tag => `<span class="tag">${tag}</span>`).join('')}
            </div>
        </div>

        <button class="action-button" onclick="startAssistantSession('${assistant.id}')">
            Spustit asistenta
        </button>
    `;

    // Zobrazení modalu
    modal.classList.remove('hidden');
}

// Uzavření modalu
function closeModal() {
    const modal = document.getElementById('assistant-modal');
    modal.classList.add('hidden');
}

// Nastavení handlerů pro modal
function setupModalHandlers() {
    const modal = document.getElementById('assistant-modal');
    const closeBtn = document.querySelector('.close-modal');

    // Zavření při kliknutí na křížek
    closeBtn.addEventListener('click', closeModal);

    // Zavření při kliknutí mimo modal
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            closeModal();
        }
    });

    // Zavření pomocí ESC klávesy
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
            closeModal();
        }
    });
}

// Spuštění session s asistentem
function startAssistantSession(assistantId) {
    const assistant = assistants.find(a => a.id === assistantId);

    if (!assistant) {
        console.error('Asistent nenalezen:', assistantId);
        return;
    }

    // Zde by byla logika pro skutečné spuštění asistenta
    // Zatím jen zobrazíme upozornění
    alert(`Spouštím asistenta: ${assistant.name}\n\nTato funkce bude implementována v další fázi projektu.`);

    console.log('Spouštím asistenta:', assistant.name);
    console.log('ID:', assistant.id);
    console.log('Schopnosti:', assistant.features);

    closeModal();
}

// Vyhledávání asistentů (pro budoucí implementaci)
function searchAssistants(query) {
    const normalizedQuery = query.toLowerCase();

    return assistants.filter(assistant => {
        const nameMatch = assistant.name.toLowerCase().includes(normalizedQuery);
        const descMatch = assistant.description.toLowerCase().includes(normalizedQuery);
        const tagMatch = assistant.tags.some(tag => tag.toLowerCase().includes(normalizedQuery));

        return nameMatch || descMatch || tagMatch;
    });
}

// Filtrace podle statusu
function filterByStatus(status) {
    return assistants.filter(assistant => assistant.status === status);
}

// Filtrace podle tagu
function filterByTag(tag) {
    return assistants.filter(assistant =>
        assistant.tags.some(t => t.toLowerCase() === tag.toLowerCase())
    );
}

// Export funkcí pro použití v konzoli nebo dalších skriptech
window.assistantDashboard = {
    search: searchAssistants,
    filterByStatus: filterByStatus,
    filterByTag: filterByTag,
    assistants: assistants
};
