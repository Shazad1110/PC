// Load app data from JSON file
async function loadAppData() {
    try {
        const response = await fetch('app-data.json');
        const data = await response.json();
        
        // Update app icon
        const appIcon = document.getElementById('appIcon');
        appIcon.src = data.appIcon;
        appIcon.alt = data.appName;
        
        // Update app title
        document.getElementById('appTitle').textContent = data.appName;
        
        // Update app description
        document.getElementById('appDescription').textContent = data.appDescription;
        
        // Update download link
        document.getElementById('downloadLink').href = data.downloadLink;
        
        // Update tutorial link
        document.getElementById('tutorialLink').href = data.tutorialLink;
        
    } catch (error) {
        console.error('Error loading app data:', error);
        // Set default values if JSON fails to load
        setDefaultValues();
    }
}

// Set default values if JSON loading fails
function setDefaultValues() {
    document.getElementById('appIcon').src = 'https://via.placeholder.com/150';
    document.getElementById('appTitle').textContent = 'ناوی ئەپڵیکەیشن';
    document.getElementById('appDescription').textContent = 'دەربارەی ئەپڵیکەیشنەکە لێرە بنووسە.';
    document.getElementById('downloadLink').href = '#';
    document.getElementById('tutorialLink').href = '#';
}

// Initialize app when page loads
document.addEventListener('DOMContentLoaded', loadAppData);

// Add smooth scroll behavior
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});