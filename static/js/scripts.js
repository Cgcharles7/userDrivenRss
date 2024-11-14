// Sample RSS feed data to populate the page
const sampleFeeds = [
    { title: "Tech News Daily", url: "https://technews.com/rss" },
    { title: "Health Updates", url: "https://healthupdates.com/rss" },
    { title: "Sports News", url: "https://sportsnews.com/rss" }
];

// Sample recommended feeds
const recommendedFeeds = [
    { title: "AI and Machine Learning", url: "https://ai.com/rss" },
    { title: "Sustainable Living", url: "https://sustainableliving.com/rss" }
];

// Function to load user's RSS feeds
function loadUserFeeds() {
    const feedList = document.getElementById('feed-list');
    feedList.innerHTML = '';
    sampleFeeds.forEach(feed => {
        const listItem = document.createElement('li');
        listItem.textContent = feed.title;
        feedList.appendChild(listItem);
    });
}

// Function to load recommended RSS feeds
function loadRecommendedFeeds() {
    const recommendationsList = document.getElementById('recommendations-list');
    recommendationsList.innerHTML = '';
    recommendedFeeds.forEach(feed => {
        const listItem = document.createElement('li');
        listItem.textContent = feed.title;
        recommendationsList.appendChild(listItem);
    });
}

// Event listener for adding new feed (for simplicity, just logs a message)
document.getElementById('add-feed').addEventListener('click', function() {
    alert("Add new feed functionality goes here!");
});

// Initial load of feeds and recommendations
loadUserFeeds();
loadRecommendedFeeds();
