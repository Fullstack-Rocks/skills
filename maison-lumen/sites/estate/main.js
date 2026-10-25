// Copy-email button. Without JavaScript the button stays hidden and the
// visible mailto link remains the way to reach the house.
const button = document.getElementById("copy-email");
const status = document.getElementById("copy-status");
const address = "iria@orrisvane.example";

if (button && status && navigator.clipboard) {
  button.hidden = false;
  button.addEventListener("click", async () => {
    // Clear first so a repeated copy is announced again.
    status.textContent = "";
    let message = "Email address copied.";
    try {
      await navigator.clipboard.writeText(address);
    } catch {
      message = `Please select and copy ${address}.`;
    }
    requestAnimationFrame(() => { status.textContent = message; });
  });
}
