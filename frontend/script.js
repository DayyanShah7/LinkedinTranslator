const inputText = document.getElementById("inputText");
const outputText = document.getElementById("outputText");
const translateBtn = document.getElementById("translateBtn");
const worseBtn = document.getElementById("worseBtn");
const clearBtn = document.getElementById("clearBtn");
const copyBtn = document.getElementById("copyBtn");
const modeSelect = document.getElementById("modeSelect");
const inputCount = document.getElementById("inputCount");
const statusText = document.getElementById("statusText");

const API_BASE = "http://127.0.0.1:5000";

inputText.addEventListener("input", () => {
  inputCount.textContent = `${inputText.value.length} / 1000`;
});

clearBtn.addEventListener("click", () => {
  inputText.value = "";
  outputText.value = "";
  inputCount.textContent = "0 / 1000";
  statusText.textContent = "Cleared";
});

copyBtn.addEventListener("click", async () => {
  if (!outputText.value.trim()) return;

  try {
    await navigator.clipboard.writeText(outputText.value);
    statusText.textContent = "Copied";
  } catch (error) {
    statusText.textContent = "Copy failed";
  }
});

translateBtn.addEventListener("click", async () => {
  await translateText(false);
});

worseBtn.addEventListener("click", async () => {
  await translateText(true);
});

async function translateText(makeWorse = false) {
  const text = inputText.value.trim();

  if (!text) {
    statusText.textContent = "Please enter text";
    return;
  }

  let mode = modeSelect.value;

  if (makeWorse) {
    mode = "ultra_cringe";
  }

  statusText.textContent = "Generating...";
  outputText.value = "";

  try {
    const response = await fetch(`${API_BASE}/api/translate`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        text: text,
        mode: mode
      })
    });

    const data = await response.json();

    if (!response.ok) {
      outputText.value = "";
      statusText.textContent = "Error";
      alert(data.error || "Something went wrong");
      return;
    }

    outputText.value = data.output;
    statusText.textContent = "Done";
  } catch (error) {
    statusText.textContent = "Server error";
    alert("Could not connect to backend.");
  }
}