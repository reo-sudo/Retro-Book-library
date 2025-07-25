function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}

searchInput.addEventListener('keydown', function(event){
    const query = searchInput.value;
    const url = `/search-books/?q=${encodeURIComponent(query)}`;
    if (event.key === 'Enter') {
        fetch(url)
            .then(response => response.json())
            .then(data => {
                const results = data.items;
                const resultsDiv = document.getElementById('Results');
                resultsDiv.innerHTML = '';
                if (results) {
                    results.forEach(item => {
                        const book = item.volumeInfo;
                        const title = book.title;
                        const authors = book.authors ? book.authors.join(', ') : 'Unknown';
                        const description = book.description || 'No description';
                        const thumbnail = book.imageLinks?.thumbnail || '';

                        const html = `
                            <div class="book-card">
                                <h3>${title}</h3>
                                <p><strong>By:</strong> ${authors}</p>
                                <p>${description}</p>
                                ${thumbnail ?`<img src="${thumbnail}" alt="cover">` : ''}
                                <form method="POST" action="/add-book/">
                                    <input type="hidden" name="csrfmiddlewaretoken" value="${getCSRFToken()}">
                                    <input type="hidden" name="title" value="${title}">
                                    <input type="hidden" name="authors" value="${authors}">
                                    <input type="hidden" name="description" value="${description}">
                                    <input type="hidden" name="google_id" value="${item.id}">
                                    <button type="submit">Add to Library</button>
                                </form>
                            </div>
                        `;

                        resultsDiv.insertAdjacentHTML('beforeend', html);
                    });
                }
            });
         
    }
})