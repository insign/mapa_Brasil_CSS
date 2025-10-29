document.addEventListener('DOMContentLoaded', function() {
    fetch('assets/map.svg')
        .then(response => response.text())
        .then(svgData => {
            const mapContainer = document.getElementById('map-container');
            mapContainer.innerHTML = svgData;
            const svg = mapContainer.querySelector('svg');
            const states = svg.querySelectorAll('path');
            states.forEach(state => {
                if(state.id){
                    state.classList.add('state');
                    state.addEventListener('click', () => {
                        alert(`State ID: ${state.id}`);
                    });
                }
            });
        });
});
