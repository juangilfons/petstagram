document.addEventListener('click', e => {
    const isDropDownButton = e.target.matches("[data-dropdown-button]");
    const isDropdownContent = e.target.closest("[data-dropdown]") != null;

    if (isDropDownButton) {
        const currentDropdown = e.target.closest("[data-dropdown]");
        currentDropdown.classList.toggle("active");

        document.querySelectorAll("[data-dropdown].active").forEach(dropdown => {
            if (dropdown !== currentDropdown) {
                dropdown.classList.remove("active");
            }
        });
    } else if (!isDropdownContent) {
        // Clicked outside any dropdown, close all dropdowns
        document.querySelectorAll("[data-dropdown].active").forEach(dropdown => {
            dropdown.classList.remove("active");
        });
    }
});