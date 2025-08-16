document.addEventListener('DOMContentLoaded', (e) => {
    
    const newsBtn = document.getElementById("btn_get_news");
    const responseText = document.getElementById("response_text");

    vercelApiUrl = "https://news-git-main-bodhits-projects-327eb862.vercel.app/api/app"
    
    newsBtn.addEventListener('click', () => {
        responseText.textContent = '...calling backend...';
        fetch(vercelApiUrl, {
            method: 'GET',
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success: ', data);
            responseText.textContent = ""
            for (i = 0; i < data.articles.length; i++) {
                const newParagraph = document.createElement('p');
                newParagraph.textContent = data.articles[i].content;
                responseText.appendChild(newParagraph);
            }
        })
        .catch((error) => {
            console.error("Error: ", error);
            responseText.textContent = "Error calling backend.";
        });
    });
});