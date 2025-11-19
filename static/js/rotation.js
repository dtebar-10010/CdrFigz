// Rotation Prompt Handler
(function() {
  const prompt = document.getElementById('mobile-rotation-prompt');
  
  if (!prompt) return;

  function checkOrientation() {
    const isMobile = window.innerWidth <= 620;
    const isPortrait = window.matchMedia('(orientation: portrait)').matches;
    
    // Show prompt if mobile device is in portrait (encourage rotation to landscape)
    if (isMobile && isPortrait) {
      prompt.classList.remove('rotation-hidden');
    } else {
      prompt.classList.add('rotation-hidden');
    }
  }

  // Check on load
  checkOrientation();

  // Check on resize
  window.addEventListener('resize', checkOrientation);

  // Check on orientation change
  window.addEventListener('orientationchange', function() {
    setTimeout(checkOrientation, 100); // Small delay for orientation change
  });

  // Modern API - listen for orientation changes
  const portraitQuery = window.matchMedia('(orientation: portrait) and (max-width: 620px)');
  
  if (portraitQuery.addEventListener) {
    portraitQuery.addEventListener('change', checkOrientation);
  } else {
    // Fallback for older browsers
    portraitQuery.addListener(checkOrientation);
  }
})();
