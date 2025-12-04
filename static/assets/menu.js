document.addEventListener('DOMContentLoaded', function () {
  const checkbox = document.querySelector('.menu-toggle');
  const menuBtn = document.querySelector('.menu-btn');
  const sidebar = document.querySelector('.sidebar');

  if (!checkbox || !menuBtn || !sidebar) return;

  // Ensure menu button has appropriate attributes
  menuBtn.setAttribute('role', 'button');
  menuBtn.setAttribute('aria-label', menuBtn.getAttribute('aria-label') || 'Toggle menu');
  menuBtn.tabIndex = 0;
  menuBtn.setAttribute('aria-expanded', checkbox.checked ? 'true' : 'false');

  // Ensure sidebar has an id for aria-controls
  if (!sidebar.id) sidebar.id = 'sidebar';
  menuBtn.setAttribute('aria-controls', sidebar.id);

  function sync() {
    const expanded = checkbox.checked;
    menuBtn.setAttribute('aria-expanded', expanded ? 'true' : 'false');
  }

  // Initial sync
  sync();

  // When checkbox changes (via label click), update aria-expanded
  checkbox.addEventListener('change', sync);

  // Keyboard activation on the label/button (support Enter and Space)
  menuBtn.addEventListener('keydown', function (e) {
    if (e.key === ' ' || e.key === 'Enter') {
      e.preventDefault();
      checkbox.checked = !checkbox.checked;
      checkbox.dispatchEvent(new Event('change'));
      // keep focus on the menu button
      menuBtn.focus();
    }
  });

  // Close menu on Escape
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && checkbox.checked) {
      checkbox.checked = false;
      checkbox.dispatchEvent(new Event('change'));
      menuBtn.focus();
    }
  });

  // Close the menu when navigation links are clicked (useful on mobile)
  document.querySelectorAll('nav a').forEach(function (a) {
    a.addEventListener('click', function () {
      if (checkbox.checked) {
        checkbox.checked = false;
        checkbox.dispatchEvent(new Event('change'));
      }
    });
  });

  // Close the menu when mobile shortcut links are clicked
  document.querySelectorAll('.mobile-shortcut').forEach(function (a) {
    a.addEventListener('click', function () {
      if (checkbox.checked) {
        checkbox.checked = false;
        checkbox.dispatchEvent(new Event('change'));
      }
    });
  });

  // Allow clicking outside the sidebar (on overlay area) to close if open on small screens
  document.addEventListener('click', function (e) {
    if (!checkbox.checked) return;
    // If click target is inside sidebar or is the menu button, ignore
    if (sidebar.contains(e.target) || menuBtn.contains(e.target) || e.target === checkbox) return;
    // Otherwise close
    checkbox.checked = false;
    checkbox.dispatchEvent(new Event('change'));
  });
});
