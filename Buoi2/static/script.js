document.addEventListener("DOMContentLoaded", function () {
    // === Caesar Cipher ===
    const caesarForm = document.getElementById('caesar-form');
    if (caesarForm) {
        caesarForm.addEventListener('submit', handleCaesarFormSubmission);
    }
    const caesarDecryptButton = document.getElementById('caesar-decrypt-button');
    if (caesarDecryptButton) {
        caesarDecryptButton.addEventListener('click', handleCaesarDecryption);
    }

    // === vingenere Cipher ===
    const vingenereForm = document.getElementById('vingenere-form');
    if (vingenereForm) {
        vingenereForm.addEventListener('submit', handlevingenereFormSubmission);
    }
    const vingenereDecryptButton = document.getElementById('vingenere-decrypt-button');
    if (vingenereDecryptButton) {
        vingenereDecryptButton.addEventListener('click', handlevingenereDecryption);
    }

    // === Playfair Cipher ===
    const playfairForm = document.getElementById('playfair-form');
    if (playfairForm) {
        playfairForm.addEventListener('submit', handlePlayfairFormSubmission);
    }
    const playfairDecryptButton = document.getElementById('playfair-decrypt-button');
    if (playfairDecryptButton) {
        playfairDecryptButton.addEventListener('click', handlePlayfairDecryption);
    }

    // === Rail Fence Cipher ===
    const railFenceForm = document.getElementById('rail-fence-form');
    if (railFenceForm) {
        railFenceForm.addEventListener('submit', handleRailFenceFormSubmission);
    }
    const railFenceDecryptButton = document.getElementById('rail-fence-decrypt-button');
    if (railFenceDecryptButton) {
        railFenceDecryptButton.addEventListener('click', handleRailFenceDecryption);
    }

    // === Transposition Cipher ===
    const transpositionForm = document.getElementById('transposition-form');
    if (transpositionForm) {
        transpositionForm.addEventListener('submit', handleTranspositionFormSubmission);
    }
    const transpositionDecryptButton = document.getElementById('transposition-decrypt-button');
    if (transpositionDecryptButton) {
        transpositionDecryptButton.addEventListener('click', handleTranspositionDecryption);
    }
});

// ===== Functions for Caesar Cipher =====
function handleCaesarFormSubmission(event) {
    event.preventDefault();
    const text = document.getElementById('caesar-text').value;
    const shift = document.getElementById('caesar-shift').value;
    
    fetch('/api/caesar/encrypt', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text, shift })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('caesar-result').innerText = `Encrypted: ${data.encrypted_text}`;
    })
    .catch(error => console.error('Error:', error));
}

function handleCaesarDecryption() {
    const text = document.getElementById('caesar-text').value;
    const shift = document.getElementById('caesar-shift').value;
    
    fetch('/api/caesar/decrypt', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text, shift })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('caesar-result').innerText = `Decrypted: ${data.decrypted_text}`;
    })
    .catch(error => console.error('Error:', error));
}

// ===== Functions for vingenere Cipher =====
function handlevingenereFormSubmission(event) {
    event.preventDefault();
    const text = document.getElementById('vingenere-text').value;
    const key = document.getElementById('vingenere-key').value;
    
    fetch('/api/vingenere/encrypt', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text, key })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('vingenere-result').innerText = `Encrypted: ${data.encrypted_text}`;
    })
    .catch(error => console.error('Error:', error));
}

function handlevingenereDecryption() {
    const text = document.getElementById('vingenere-text').value;
    const key = document.getElementById('vingenere-key').value;
    
    fetch('/api/vingenere/decrypt', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text, key })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('vingenere-result').innerText = `Decrypted: ${data.decrypted_text}`;
    })
    .catch(error => console.error('Error:', error));
}

// ===== Functions for Playfair Cipher =====
function handlePlayfairFormSubmission(event) {
    event.preventDefault();
    const text = document.getElementById('playfair-text').value;
    const key = document.getElementById('playfair-key').value;
    
    fetch('/api/playfair/encrypt', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text, key })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('playfair-result').innerText = `Encrypted: ${data.encrypted_text}`;
    })
    .catch(error => console.error('Error:', error));
}

function handlePlayfairDecryption() {
    const text = document.getElementById('playfair-text').value;
    const key = document.getElementById('playfair-key').value;
    
    fetch('/api/playfair/decrypt', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text, key })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('playfair-result').innerText = `Decrypted: ${data.decrypted_text}`;
    })
    .catch(error => console.error('Error:', error));
}

// ===== Functions for Rail Fence Cipher =====
function handleRailFenceFormSubmission(event) {
    event.preventDefault();
    const text = document.getElementById('rail-fence-text').value;
    const rails = document.getElementById('rail-fence-rails').value;
    
    fetch('/api/rail_fence/encrypt', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text, rails })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('rail-fence-result').innerText = `Encrypted: ${data.encrypted_text}`;
    })
    .catch(error => console.error('Error:', error));
}

function handleRailFenceDecryption() {
    const text = document.getElementById('rail-fence-text').value;
    const rails = document.getElementById('rail-fence-rails').value;
    
    fetch('/api/rail_fence/decrypt', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text, rails })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('rail-fence-result').innerText = `Decrypted: ${data.decrypted_text}`;
    })
    .catch(error => console.error('Error:', error));
}

// ===== Functions for Transposition Cipher =====
function handleTranspositionFormSubmission(event) {
    event.preventDefault();
    const text = document.getElementById('transposition-text').value;
    const key = document.getElementById('transposition-key').value;
    
    fetch('/api/transposition/encrypt', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text, key })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('transposition-result').innerText = `Encrypted: ${data.encrypted_text}`;
    })
    .catch(error => console.error('Error:', error));
}

function handleTranspositionDecryption() {
    const text = document.getElementById('transposition-text').value;
    const key = document.getElementById('transposition-key').value;
    
    fetch('/api/transposition/decrypt', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text, key })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('transposition-result').innerText = `Decrypted: ${data.decrypted_text}`;
    })
    .catch(error => console.error('Error:', error));
}
