function toggleCard(button) {
    const cardInner = button.closest('.card-inner');
    cardInner.classList.toggle('is-flipped');
}

function positionCircle() {
    const bars = document.querySelectorAll('.toxicity-bar');
    bars.forEach(bar => {
        const percentage = parseFloat(bar.dataset.percentage);
        const circle = bar.querySelector('.circle');
        const barWidth = bar.clientWidth;
        const circlePosition = (barWidth * percentage) / 100;
        circle.style.left = `${circlePosition}px`;
    });
}

document.addEventListener('DOMContentLoaded', function() {
    var modal = document.getElementById("config-modal");
    var btn = document.getElementById("config-button");
    var span = document.getElementsByClassName("close-button")[0];
    var form = document.querySelector('form');
    var slider = document.getElementById("thresholdRange");
    var defaultConfigButton = document.getElementById("default-config-button");
    var okButton = document.getElementById("ok-button");
    var clearButton = document.getElementById("clear-button");
    var textarea = document.getElementById("text");
    var cardsContainer = document.getElementById("cards-container");

    const defaultConfig = {
        function1: false,
        function2: true,
        function3: true,
        function4: false,
        function5: false,
        function6: false,
        level: 5
    };

    function setConfig(config) {
        document.getElementById("toggleFunction1").checked = config.function1;
        document.getElementById("toggleFunction2").checked = config.function2;
        document.getElementById("toggleFunction3").checked = config.function3;
        document.getElementById("toggleFunction4").checked = config.function4;
        document.getElementById("toggleFunction5").checked = config.function5;
        document.getElementById("toggleFunction6").checked = config.function6;
        slider.value = config.level;
        document.getElementById("level").value = config.level;
    }

    // Abrir el modal
    btn.onclick = function() {
        modal.style.display = "block";
    }

    // Cerrar el modal
    span.onclick = function() {
        modal.style.display = "none";
    }

    // Cerrar el modal con el botón OK
    okButton.onclick = function() {
        modal.style.display = "none";
    };

    // Cerrar el modal al hacer clic fuera de él
    //window.onclick = function(event) {
    //    if (event.target == modal) {
    //        modal.style.display = "none";
    //    }
    //}

    // Limpiar el textarea y ocultar el cards-container
    clearButton.onclick = function() {
        window.location.href = "/";
    };

    // Actualizar los valores de los toggles antes de enviar el formulario
    form.addEventListener("submit", function(event) {
        var textArea = document.getElementById("text");
        var textLabel = document.querySelector("label[for='text']");
        if (textArea.value.trim() === '') {
            // Evitar el envío del formulario si el campo de texto está vacío
            event.preventDefault();
            textLabel.classList.add("highlight");
            setTimeout(function() {
                textLabel.classList.remove("highlight");
            }, 400); // Remover la clase después 0.4 segundos
            return;
        }
        document.getElementById("function1").value = document.getElementById("toggleFunction1").checked;
        document.getElementById("function2").value = document.getElementById("toggleFunction2").checked;
        document.getElementById("function3").value = document.getElementById("toggleFunction3").checked;
        document.getElementById("function4").value = document.getElementById("toggleFunction4").checked;
        document.getElementById("function5").value = document.getElementById("toggleFunction5").checked;
        document.getElementById("function6").value = document.getElementById("toggleFunction6").checked;
        document.getElementById("level").value = slider.value;
    });

    // Inicializar los toggles con los valores actuales solo si no hay valores almacenados
    if (!document.getElementById("function1").value &&
        !document.getElementById("function2").value &&
        !document.getElementById("function3").value &&
        !document.getElementById("function4").value &&
        !document.getElementById("function5").value &&
        !document.getElementById("function6").value) {
        setConfig(defaultConfig);
    } else {
        document.getElementById("toggleFunction1").checked = document.getElementById("function1").value === 'true';
        document.getElementById("toggleFunction2").checked = document.getElementById("function2").value === 'true';
        document.getElementById("toggleFunction3").checked = document.getElementById("function3").value === 'true';
        document.getElementById("toggleFunction4").checked = document.getElementById("function4").value === 'true';
        document.getElementById("toggleFunction5").checked = document.getElementById("function5").value === 'true';
        document.getElementById("toggleFunction6").checked = document.getElementById("function6").value === 'true';
        document.getElementById("thresholdRange").value = document.getElementById("level").value;
    }

    // Actualizar el valor del slider en tiempo real
    slider.addEventListener("input", function() {
        document.getElementById("level").value = slider.value;
    });

    // Restaurar la configuración por defecto
    defaultConfigButton.onclick = function() {
        setConfig(defaultConfig);
    };

    // Posicionar el círculo
    positionCircle();

    textarea.focus();
    textarea.setSelectionRange(textarea.value.length, textarea.value.length);
});
