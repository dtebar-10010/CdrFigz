document.addEventListener("DOMContentLoaded", function () {
    // Initialize stackedCards if available
    if (typeof stackedCards !== 'undefined') {
        let stackedCardSlide = new stackedCards({
            selector: ".stacked-cards-slide",
            layout: "slide",
            transformOrigin: "center"
        });
        stackedCardSlide.init();
    } else {
        console.error("stackedCards is not defined. Please ensure the library is loaded.");
    }

    // Adjust phase selection container
    const phaseSelectionContainer = document.querySelector("#phase-selection-container");
    if (phaseSelectionContainer) {
        window.addEventListener("load", function() {
            phaseSelectionContainer.classList.remove("hide-initially");
            // Let CSS handle width, margin, display, and centering
        });
    }

    // Video Controls Logic
    const videos = document.querySelectorAll(".video-slide");
    let activeVideo = videos[0]; // Initially, assume the first video is the active one

    function setActiveVideo(newActiveVideo) {
        // Pause and reset all videos
        videos.forEach((video) => {
            video.pause();
            video.currentTime = 0; // Reset video to start
            video.removeAttribute("controls"); // Remove controls from inactive videos
            video.load(); // Reload the video to show the cover poster
        });

        // Ensure the new active video is paused and has controls
        newActiveVideo.pause(); // Explicitly pause to prevent auto-play
        newActiveVideo.setAttribute("controls", "controls"); // Show controls on the active video
        activeVideo = newActiveVideo; // Update the active video reference
    }

    // Initial setup: only show controls on the top video, do not play it
    setActiveVideo(activeVideo); // Assuming the first video is on top initially

    videos.forEach(function (video) {
        video.addEventListener("click", function () {
            if (video === activeVideo) {
                if (video.paused) {
                    video.play(); // Only play the video if it's paused and it's the active one
                }
            } else {
                // If the clicked video is not the active one, bring it to the top and pause it
                setActiveVideo(video);
            }
        });

        video.addEventListener("play", function () {
            if (video !== activeVideo) {
                video.pause(); // Ensure that only the active video can play
            }
        });
    });

    // Handle the active phase button color and textContainer styling
    // const textContainer = document.querySelector(".text-container");
    // if (textContainer) {
    //     const maxAllowedHeight = 111;
    //     const activeButton = document.querySelector(".btn.active");
    //     let currentPhaseColor;
    //
    //     if (activeButton) {
    //         currentPhaseColor = window.getComputedStyle(activeButton).backgroundColor;
    //         textContainer.style.borderColor = currentPhaseColor;
    //     } else {
    //         console.warn("No active button found. Defaulting phase color.");
    //         currentPhaseColor = "#000"; // Default color if no active button is found
    //         textContainer.style.borderColor = currentPhaseColor;
    //     }
    //
    //     function adjustTextContainer() {
    //         textContainer.style.maxHeight = "none"; // Reset max-height
    //         textContainer.style.overflowY = "hidden"; // Reset overflow
    //
    //         if (textContainer.scrollHeight > maxAllowedHeight) {
    //             textContainer.style.maxHeight = maxAllowedHeight + "px";
    //             textContainer.style.overflowY = "auto";
    //         }
    //     }
    //
    //     adjustTextContainer();
    //     window.addEventListener("resize", adjustTextContainer);
    // }

    // Handle the active class for phase buttons
    const phaseButtons = document.querySelectorAll('#phase-selection-container .btn-group .btn');

    // Apply the active class based on URL parameter on page load, default to phase 1
    const urlParams = new URLSearchParams(window.location.search);
    let currentPhase = urlParams.get('phase');

    if (!currentPhase) {
        currentPhase = '1'; // Default to phase 1 if no phase parameter is present
    }

    phaseButtons.forEach(button => {
        const phase = button.getAttribute('href').split('=')[1];
        if (phase === currentPhase) {
            button.classList.add('active');
        }

        button.addEventListener('click', function () {
            phaseButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
        });
    });
});
