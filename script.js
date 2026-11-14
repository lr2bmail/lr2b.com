const menuButton = document.querySelector("[data-menu-button]");
const mobileMenu = document.querySelector("[data-mobile-menu]");

if (menuButton && mobileMenu) {
  const topLine = menuButton.querySelector('[data-menu-line="top"]');
  const bottomLine = menuButton.querySelector('[data-menu-line="bottom"]');

  const setMenuState = (isOpen) => {
    mobileMenu.classList.toggle("hidden", !isOpen);
    menuButton.setAttribute("aria-expanded", String(isOpen));
    menuButton.setAttribute("aria-label", isOpen ? "Close menu" : "Open menu");
    topLine?.classList.toggle("rotate-45", isOpen);
    topLine?.classList.toggle("translate-y-0", isOpen);
    bottomLine?.classList.toggle("-rotate-45", isOpen);
    bottomLine?.classList.toggle("translate-y-0", isOpen);
  };

  menuButton.addEventListener("click", () => {
    setMenuState(menuButton.getAttribute("aria-expanded") !== "true");
  });

  mobileMenu.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      setMenuState(false);
    });
  });
}

const copyEmailButton = document.querySelector("[data-copy-email]");

if (copyEmailButton) {
  const copyLabel = copyEmailButton.querySelector("[data-copy-label]");
  const copyStatus = document.querySelector("[data-copy-status]");

  copyEmailButton.addEventListener("click", async () => {
    const email = copyEmailButton.dataset.email;

    try {
      await navigator.clipboard.writeText(email);
      copyLabel.textContent = "Copied";
      copyStatus.textContent = `${email} copied to clipboard`;

      window.setTimeout(() => {
        copyLabel.textContent = "Copy";
        copyStatus.textContent = "";
      }, 1800);
    } catch {
      window.location.href = `mailto:${email}`;
    }
  });
}

// Project enquiry form: no server here, so it opens the visitor's email app with the message filled in.
const enquiryForm = document.querySelector("[data-enquiry]");

if (enquiryForm) {
  enquiryForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const data = new FormData(enquiryForm);
    const name = String(data.get("name") || "").trim();
    const email = String(data.get("email") || "").trim();
    const brief = String(data.get("brief") || "").trim();
    const subject = `Project enquiry from ${name}`;
    const body = `${brief}\n\n${name}\n${email}`;
    window.location.href = `mailto:contact@lr2b.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
  });
}
