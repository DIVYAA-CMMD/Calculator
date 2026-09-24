// ============================================================
// CONFIG — change this if your Flask backend runs elsewhere
// ============================================================
const API_BASE = "http://127.0.0.1:5000";

// ============================================================
// GALAXY STAR FIELD GENERATION
// ============================================================
function generateStars(containerId, count, sizeRange, durationRange) {
  const container = document.getElementById(containerId);
  const frag = document.createDocumentFragment();

  for (let i = 0; i < count; i++) {
    const star = document.createElement("div");
    star.className = "star";

    const size = (Math.random() * (sizeRange[1] - sizeRange[0]) + sizeRange[0]).toFixed(2);
    const top = Math.random() * 100;
    const left = Math.random() * 100;
    const duration = (Math.random() * (durationRange[1] - durationRange[0]) + durationRange[0]).toFixed(2);
    const delay = (Math.random() * 5).toFixed(2);

    star.style.width = `${size}px`;
    star.style.height = `${size}px`;
    star.style.top = `${top}%`;
    star.style.left = `${left}%`;
    star.style.animationDuration = `${duration}s`;
    star.style.animationDelay = `${delay}s`;
    star.style.boxShadow = `0 0 ${size * 2}px rgba(255,255,255,0.8)`;

    frag.appendChild(star);
  }
  container.appendChild(frag);
}

generateStars("stars", 120, [0.5, 1.5], [2, 5]);
generateStars("stars2", 70, [1, 2.2], [3, 7]);
generateStars("stars3", 40, [1.5, 3], [4, 9]);

// ============================================================
// CALCULATOR — calls the Flask API, no math done in JS
// ============================================================
const resultBox = document.getElementById("result");
const num1Input = document.getElementById("num1");
const num2Input = document.getElementById("num2");

function showResult(value) {
  resultBox.value = value;
}

function showError(msg) {
  resultBox.value = "Error";
  console.error(msg);
}

async function callApi(url) {
  try {
    const response = await fetch(url);

    if (!response.ok) {
      throw new Error(`Server responded with status ${response.status}`);
    }

    const data = await response.text();
    return data;

  } catch (err) {
    showError(
      err.message || "Could not reach backend. Is Flask running on " + API_BASE + " ?"
    );
    return null;
  }
}

function extractAndShow(data) {
  if (data === null || data === undefined) return;
  showResult(data);
}

document.querySelectorAll(".buttons-grid .btn").forEach((btn) => {
  btn.addEventListener("click", async () => {
    const op = btn.dataset.op;
    const num1 = num1Input.value;
    const num2 = num2Input.value;

    let url = "";

    switch (op) {
      case "add":
        url = `${API_BASE}/add?num1=${num1}&num2=${num2}`;
        break;
      case "subtract":
        url = `${API_BASE}/subtract?num1=${num1}&num2=${num2}`;
        break;
      case "multiply":
        url = `${API_BASE}/multiply?num1=${num1}&num2=${num2}`;
        break;
      case "divide":
        url = `${API_BASE}/divide?num1=${num1}&num2=${num2}`;
        break;
      case "square":
        url = `${API_BASE}/square?num=${num1}`;
        break;
      case "cube":
        url = `${API_BASE}/cube?num=${num1}`;
        break;
      case "percentage":
        // Number 1 = base number, Number 2 field = percent
        url = `${API_BASE}/percentage?num=${num1}&percent=${num2}`;
        break;
      case "average":
        url = `${API_BASE}/average?num1=${num1}&num2=${num2}`;
        break;
      default:
        return;
    }

    const data = await callApi(url);
    extractAndShow(data);
  });
});

document.getElementById("clearBtn").addEventListener("click", () => {
  num1Input.value = "";
  num2Input.value = "";
  document.getElementById("convValue").value = "";
  showResult("");
});

// ============================================================
// UNIT CONVERTER
// ============================================================
document.getElementById("convertBtn").addEventListener("click", async () => {
  const value = document.getElementById("convValue").value;
  const conversion = document.getElementById("convType").value;

  const url = `${API_BASE}/convert?conversion=${conversion}&value=${value}`;
  const data = await callApi(url);
  extractAndShow(data);
});
