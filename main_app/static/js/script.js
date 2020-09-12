<script>
    const bodyEl = document.getElementByTagName('body');

    const plBtnEl = document.getElementById('pl-btn')
    plBtnEl.addEventListener("click", function() {
        pollEl = document.createElementById('pollingLocations');
        bodyEl.appendChild(pollEl);
    });

    const evsBtnEl = document.getElementById('evs-btn')
    evsBtnEl.addEventListener("click", function() {
        siteEl = document.createElementById('earlyVotingSites');
        bodyEl.appendChild(siteEl);
    });

    const dolBtnEl = document.getElementById('dol-btn')
    dolBtnEl.addEventListener("click", function() {
        dropEl = document.createElementById('dropOffLocations');
        bodyEl.appendChild(dropEl);
    })
</script>