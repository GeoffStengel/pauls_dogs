const banners = [
    { text: "Adopt a Pet Today!", color: "#007bff", link: "https://example.com/adopt" },
    { text: "Special Adoption Discounts!", color: "#28a745", link: "https://example.com/discounts" },
    { text: "Find Your Perfect Companion!", color: "#dc3545", link: "https://example.com/find" },
    { text: "Support Local Shelters!", color: "#ffc107", link: "https://example.com/support" },
];

let currentIndex = 0;

function changeBanner() {
    const banner = document.getElementById('banner');

    banner.textContent = banners[currentIndex].text;
    banner.style.backgroundColor = banners[currentIndex].color;
    
    // Set up a click event directly to the banner
    banner.onclick = () => window.location.href = banners[currentIndex].link;

    currentIndex = (currentIndex + 1) % banners.length; // Loop back to the start
}

// Change banner every 3 seconds
setInterval(changeBanner, 4000);
changeBanner(); // Initial call






