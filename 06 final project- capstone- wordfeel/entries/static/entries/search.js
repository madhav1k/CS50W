let addFinished = false;
let entryobj = {};
let searchSug;
let searchTog;
let dropdown;
let num = 0;

function search_suggestions() {

    addFinished = false;

    let searchValue = searchTog.value;
    fetch(`/search_api?value=${searchValue}`)
    .then(response => response.json())
    .then(entries => {
        if (entries['num'] < num) {
            searchSug.style.height = `${searchSug.offsetHeight}px`;
        }
        searchSug.innerHTML = "";
        num = 0;
        for (let i = 0; i < entries['num']; i++) {
            entryobj['id'] = entries['ids'][i];
            entryobj['entry'] = entries['entries'][i];
            entryobj['latinized'] = entries['latinized'][i];
            entryobj['language'] = entries['languages'][i];
            add_entry_search(entryobj);
        }
        dropdown.style.height = `${32*num+20}px`;       
        setTimeout(() => {
            searchSug.style.height= "auto";
            if (num === 0) {
                dropdown.style.height = "0px";
            }
            else {
                dropdown.style.height = `${searchSug.offsetHeight+2}px`;
            }
        }, 250);
    })
    .then(() => addFinished = true)
    .then(() => {
        if ((searchSug.innerHTML === "") || searchValue === "") {
            dropdown.style.height = "0px";
        }
    });
}

function add_entry_search(entryobj) {

    const url = `/entry/${entryobj['id']}`;
    const entry = document.createElement('a');
    entry.className = 'dropdown-item';
    entry.setAttribute("href", url);
    if (entryobj['latinized'] != "" && entryobj['latinized'] != entryobj['entry']) {
        lat = " <i>(" + entryobj['latinized'] + ")</i>"
    }
    else {
        lat = ""
    }
    entry.innerHTML = `${entryobj['entry']}${lat} <strong>${entryobj['language']}</strong>`;
    searchSug.append(entry);
    num += 1;
};

document.addEventListener("DOMContentLoaded", () => {
    searchSug = document.querySelector("#searchSuggestions");
    searchTog = document.querySelector('#searchToggle');
    dropdown = document.querySelector('.dropdown');
    searchTog.addEventListener("input", search_suggestions);
    searchTog.addEventListener("click", () => {
        if (dropdown.style.height != "0px") {
            searchSug.style.display = "block";
            dropdown.style.height = "0px";
            
        } else if (dropdown.style.height === "0px" && num != 0){
            dropdown.style.height = `${searchSug.offsetHeight+2}px`;
        }
    });
    navbarToggler = document.querySelector('.navbar-toggler');

    if (searchTog.offsetWidth === 0 || searchTog.offsetHeight === 0) {
        navbarToggler.addEventListener("click", () => {
            if (navbarToggler.getAttribute('aria-expanded') === 'true') {
                width = searchTog.offsetWidth;
                dropdown.style.width = `${width}px`;
                document.querySelector('.dropdown-menu').style.width = `${width}px`;

                height = searchTog.offsetHeight;
                dropdown.style.top = `${height}px`;
            }
        });
    }
    else {
        width = searchTog.offsetWidth;
        dropdown.style.width = `${width}px`;
        document.querySelector('.dropdown-menu').style.width = `${width}px`;

        height = searchTog.offsetHeight;
        dropdown.style.top = `${height}px`;
    }
});

document.addEventListener('click', function(e){   
    if (!searchSug.contains(e.target) && !searchTog.contains(e.target)) {
        searchSug.style.display = "block";
        dropdown.style.height = "0px";
    }
  });