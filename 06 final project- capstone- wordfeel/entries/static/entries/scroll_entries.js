let loadStart = 0;
const quantity = 40;
let finishedLoading = true;
let finished_api = false;
let headtext;

document.addEventListener('DOMContentLoaded', () => {
    headtext = document.querySelector('.headtext');
    headtext.style.display = 'none';
    load_entries();
});

window.onscroll = () => {
    if ((window.innerHeight + window.scrollY >= document.body.offsetHeight) && finishedLoading === true) {
        finishedLoading = false;
        load_entries();
    }
};

entryobj = {}
function load_entries() {

    const start = loadStart;
    const end = start + quantity - 1;
    loadStart = end + 1;

    if (finished_api === false) {
        fetch(`/scroll_entries_api?start=${start}&end=${end}&q=${quantity}`)
        .then(response => response.json())
        .then(data => {
            for (let i = 0; i < data['num']; i++) {
                entryobj['id'] = data['ids'][i];
                entryobj['entry'] = data['entries'][i];
                entryobj['latinized'] = data['latinized'][i];
                entryobj['language'] = data['languages'][i];
                add_entry_scroll(entryobj);
            }
            if (headtext.style.display === 'none') {
                headtext.style.display = 'block';
            }
            if (data['finished'] === "true") {
                finished_api = true;
            }
            if (finished_api === true) {
                document.querySelector('.loading').remove();
            }
        })
        .then(() => finishedLoading = true);
    }
};

function add_entry_scroll(entryobj) {

    const url = `/entry/${entryobj['id']}`;
    const entry = document.createElement('div');
    if (entryobj['latinized'] != "" && entryobj['latinized'] != entryobj['entry']) {
        lat = " <i>(" + entryobj['latinized'] + ")</i>"
    }
    else {
        lat = ""
    }
    entry.innerHTML = `<p><strong>${entryobj['language']}</strong> <a href="${url}">${entryobj['entry']}</a>${lat}</p>`;
    document.querySelector('.body').append(entry);
};