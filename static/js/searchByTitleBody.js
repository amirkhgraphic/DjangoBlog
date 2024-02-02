function fill(data) {
    const container = document.getElementById('container');
    container.innerHTML = '';

    if (data.length > 0) {
        data.forEach(function(post) {
            let djangoFormattedDate = new Date(post['created_at']).toLocaleString('en-US', {
              year: 'numeric',
              month: 'short',
              day: 'numeric',
              hour: 'numeric',
              minute: 'numeric',
              second: 'numeric',
              hour12: true,
              timeZoneName: 'short'
            });
            let card = document.createElement('div');
            card.className = 'card mx-5 mt-5';
            card.innerHTML = `
            <div class="card-header">Author: ${post['author']['user_name']}</div>
            <div class="card-body">
              <h5 class="card-title">${post['title']}</h5>
              <p class="card-text">${post['body'].slice(0, 10)}...</p>
              <a href="/posts/detail/${post['id']}" class="btn btn-primary">See Detail</a>
            </div>
            <div class="card-footer text-muted">${djangoFormattedDate}</div>
            `;
            container.appendChild(card);
        });
    } else {
        let noPostMessage = document.createElement('p');
        noPostMessage.className = 'text-center';
        noPostMessage.textContent = 'No post is available';
        container.appendChild(noPostMessage);
    }
}

const SearchAPILink = 'http://127.0.0.1:8000/api/search-title/?Key=';
const searchBar = document.getElementById('search-bar');

searchBar.addEventListener(
    "input", () => {
        fetch(SearchAPILink + searchBar.value.trim())
            .then(response => response.json())
            .then(data => {
                fill(data['results']);
            })
    }
)