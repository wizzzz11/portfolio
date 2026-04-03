// Replace with your actual profile links
document.getElementById("githubLink").href = "https://github.com/wizzzz11";
document.getElementById("linkedinLink").href = "https://www.linkedin.com/in/sourabrata-saha-207a51309";
document.getElementById("emailLink").href = "mailto:2006sourabratasaha@gmail.com";
const menuToggle = document.getElementById("menu-toggle");
const nav = document.getElementById("nav");

menuToggle.addEventListener("click", () => {
    nav.classList.toggle("active");
});