// ---------------- PARALLAX ----------------

const hero = document.getElementById("hero");
const layers = document.querySelectorAll(".parallax");

hero.addEventListener("mousemove", (e) => {
    let x = (window.innerWidth / 2 - e.pageX) / 40;
    let y = (window.innerHeight / 2 - e.pageY) / 40;

    layers[0].style.transform = `translate(${x}px, ${y}px) scale(1.1)`;
    layers[1].style.transform = `translate(${x * 2}px, ${y * 2}px) scale(1.15)`;
});

// ---------------- RAIN EFFECT ----------------

const canvas = document.getElementById("rainCanvas");
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let rainDrops = [];

for (let i = 0; i < 500; i++) {
    rainDrops.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        length: Math.random() * 20,
        speed: Math.random() * 4 + 4
    });
}

function drawRain() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.strokeStyle = "rgba(255,255,255,0.3)";
    ctx.lineWidth = 1;

    for (let i = 0; i < rainDrops.length; i++) {
        let drop = rainDrops[i];
        ctx.beginPath();
        ctx.moveTo(drop.x, drop.y);
        ctx.lineTo(drop.x, drop.y + drop.length);
        ctx.stroke();

        drop.y += drop.speed;

        if (drop.y > canvas.height) {
            drop.y = -20;
            drop.x = Math.random() * canvas.width;
        }
    }

    requestAnimationFrame(drawRain);
}

drawRain();

// ---------------- LIGHTNING + THUNDER ----------------

const lightning = document.getElementById("lightning");
const thunderSound = document.getElementById("thunderSound");

function triggerLightning() {
    lightning.style.opacity = 0.8;
    thunderSound.play();

    setTimeout(() => {
        lightning.style.opacity = 0;
    }, 100);
}

setInterval(() => {
    if (Math.random() > 0.7) {
        triggerLightning();
    }
}, 3000);

// ---------------- TRAILER TEXT ----------------

const trailerText = document.getElementById("trailerText");

const lines = [
    "IN A WORLD",
    "WHERE HONOR IS LOST",
    "ONLY ONE WARRIOR",
    "WILL STAND..."
];

let index = 0;

function showNextLine() {
    if (index < lines.length) {
        trailerText.style.opacity = 0;
        setTimeout(() => {
            trailerText.innerText = lines[index];
            trailerText.style.opacity = 1;
            index++;
        }, 500);
    }
}

setInterval(showNextLine, 4000);
showNextLine();