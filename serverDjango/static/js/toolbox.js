// Toolbox of reuseable js functions

// Toggle visibility of the next dom
function toggleVisibilityNext(dom) {
    // Report click event
    console.log(dom, "is clicked");

    // Find the next dom,
    // noted by [j]
    let par = dom.parentElement;
    for (var j = 0; j < par.childElementCount; j++) {
        if (par.children[j] == dom) {
            break;
        }
    }

    if (dom.innerHTML.startsWith("[-]")) {
        dom.innerHTML = dom.innerHTML.replace("-", "+");
    } else if (dom.innerHTML.startsWith("[+]")) {
        dom.innerHTML = dom.innerHTML.replace("+", "-");
    }

    // Toggle visibility
    toggleVisibility(par.children[j + 1]);
}

// Toggle visibility of the [dom]
function toggleVisibility(dom) {
    if (dom.style.display === "none") {
        // If currently it is invisible
        // Restore the visibility as defaultDisplay,
        // if failed, use "" instead
        if (dom.style.hasOwnProperty("defaultDisplay")) {
            dom.style.display = dom.style.defaultDisplay;
            return 0;
        } else {
            dom.style.display = "";
        }
    } else {
        // If currently it is not invisible
        // Save current state as default option,
        // set the visibility as "none"
        dom.style.defaultDisplay = dom.style.display;
        dom.style.display = "none";
    }
}

// Say something to debugger
console.log("Toolbox is loaded.");