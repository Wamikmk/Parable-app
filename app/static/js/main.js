function getExplanation() {
    const query = document.getElementById('query').value;
    
    fetch('/explain', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({query: query}),
    })
    .then(response => response.json())
    .then(data => {
        // Format the explanation text
        const formattedExplanation = formatExplanation(data.explanation);
        document.getElementById('explanation').innerHTML = formattedExplanation;
        document.getElementById('diagram').innerHTML = `<img src="data:image/png;base64,${data.diagram}" alt="Diagram">`;
        document.getElementById('results').classList.remove('hidden');
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function formatExplanation(text) {
    // Replace **text** with <strong>text</strong>
    return text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
}